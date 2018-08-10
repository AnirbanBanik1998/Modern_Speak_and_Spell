import time
import threading
import wave
import sys
from array import array
from queue import Queue, Full
import pyaudio
import os
from API import edit


class Recorder:
    def __init__(self, DEFAULT_LM_PATH, DEFAULT_AM_PATH, CHANNELS=1, RATE=16000, CHUNK_SIZE=1024, MIN_VOLUME=1600,
                 OUTPUT_DIR="wav", SILENCE=3, TRIALS=None, MULTI=False, DECODE=False, L_LIB=None, A_LIB=None,
                 TRANSCRIBE=False, OUTPUT_SHELL=None):

        """Class which contains the inner functions of the recorder script."""

        self.dlp = DEFAULT_LM_PATH
        self.dap = DEFAULT_AM_PATH
        self.audio = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.CHUNK_SIZE = CHUNK_SIZE
        self.MIN_VOLUME = MIN_VOLUME
        self.WAVE_OUTPUT = OUTPUT_DIR
        self.lock = threading.Lock()
        self.frames = []
        self.silence_time = SILENCE
        self.trials = TRIALS
        self.multi = MULTI
        self.decode = DECODE
        self.l = L_LIB
        self.ac = A_LIB
        self.transcribe = TRANSCRIBE
        self.shell = OUTPUT_SHELL
        self.lang = ""
        self.dic = ""
        if self.WAVE_OUTPUT not in os.listdir():
            os.system("mkdir " + self.WAVE_OUTPUT)
        self.set_library(self.dlp, self.dap)
        self.i = 0
        self.counter = 0
        self.flag = 0

    def set_library(self, lmpath, ampath):
        """Function which sets the library paths in order to make it easy for every user to use.
		
		:param lmpath: It contains the default language model path.
		:param ampath: It contains the default acoustic model path.
		
		"""
        if self.l is not None:
            self.lang = lmpath + (self.l).lower() + ".lm"
            self.dic = lmpath + (self.l).lower() + ".dic"
        else:
            x = input("Enter Language Model")
            type(x)
            y = input("Enter Dictionary")
            type(y)
            self.lang = lmpath + x
            self.dic = lmpath + y
        if self.ac is not None:
            self.acoustic = ampath + self.ac
        else:
            x = input("Enter Acoustic Model")
            type(x)
            self.acoustic = ampath + x

    def start(self):
        """
		Main function which starts the entire process.
		"""
        self.stopped = threading.Event()
        self.q = Queue()
        self.listen_t = threading.Thread(target=self.listen, args=(self.stopped, self.q))
        self.listen_t.start()
        self.record_t = threading.Thread(target=self.record, args=(self.stopped, self.q))
        self.record_t.start()

        try:
            while not self.flag == 1:
                self.listen_t.join(0.1)
                self.record_t.join(0.1)
        except KeyboardInterrupt:  # Stops the entire process if Keyboard Interrupt is pressed.
            self.stopped.set()
            self.listen_t.join()
            self.record_t.join()

    def record(self, stopped, q):
        """
		Function which records when volume of a chunk is greater than a particular threshold value.
		
		:param stopped: Same as in listen()
		:param q: Same as in listen()
		
		"""
        start = 0
        t = start
        k = 0
        while True:

            if stopped.wait(timeout=0):
                break
            chunk = q.get()  # Extracts a chunk out of the queue
            vol = max(chunk)
            if vol >= self.MIN_VOLUME:
                if len(self.frames) > 0:
                    k = 0
                start = int(round(time.time()))
                t = start
                print("O"),
                self.frames.append(chunk)
            elif len(self.frames) > 0:
                print("-"),
                if k == 0:
                    self.frames.append(chunk)

                    # Appends one chunk of silence to help recognize the words more clearly

                    k = k + 1
                t = int(round(time.time()))

                # If silence duration is more than input seconds... writes the frames to an audio file.

                if (int(t - start) >= int(self.silence_time)) and start > 0:
                    string = self.WAVE_OUTPUT + "/test" + str(self.i + 1) + ".wav"
                    waveFile = wave.open(string, 'wb')
                    waveFile.setnchannels(self.CHANNELS)
                    waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
                    waveFile.setframerate(self.RATE)
                    waveFile.writeframes(b''.join(self.frames))
                    waveFile.close()
                    if self.multi:
                        self.i += 1
                    self.counter += 1
                    del self.frames[:]
                    k = 0

                    # Pauses the recording process for further operations on the audio file generated
                    if self.decode:
                        with self.lock:
                            self.decoder()
                            if self.shell is not None:
                                os.system(self.shell)
                    if self.trials is not None and self.trials == self.counter:
                        stopped.set()
                        self.flag = 1
                    else:
                        print("You may again start recording...")

    def listen(self, stopped, q):
        """
		Function which listens to the audio stream and puts the chunks in a queue to be operated later on.
		
		:param stopped: The threading event flag.
		:param q: A queue to put all the required chunks into so that they can be processed later.
		
		"""
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      frames_per_buffer=self.CHUNK_SIZE)
        while True:
            if stopped.wait(timeout=0):
                break
            try:
                q.put(array('h', self.stream.read(self.CHUNK_SIZE)))
            except Full:
                pass

    def decoder(self):
        """
		Function to decode using the pocketsphinx batch command.
		"""
        if self.transcribe:
            edit.fileids(str(self.i + 1))
            edit.transcription(str(self.i + 1))
        else:
            edit.fileids(str(self.i + 1))
        os.system("pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm " + str(
            self.lang) + " -dict " + str(self.dic) + " -hmm " + str(self.acoustic) + " -samprate " + str(self.RATE) +
                  " -nfft " + str(self.CHUNK_SIZE) + " -hyp test.hyp")
