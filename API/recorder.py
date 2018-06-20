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
	def __init__(self, DEFAULT_LIB_PATH, CHANNELS=1, RATE=16000, CHUNK_SIZE=1024, MIN_VOLUME=1600, OUTPUT_DIR="wav", 			SILENCE=3, TRIALS=None, MULTI=False, DECODE=False, LIB_FILE=None, TRANSCRIBE=False, OUTPUT_SHELL=None):
		
		"""Class which contains the inner functions of the recorder script."""
		
		self.dlp = DEFAULT_LIB_PATH
		self.audio = pyaudio.PyAudio()
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = CHANNELS
		self.RATE=RATE
		self.CHUNK_SIZE=CHUNK_SIZE
		self.MIN_VOLUME=MIN_VOLUME
		self.WAVE_OUTPUT = OUTPUT_DIR
		self.lock=threading.Lock()
		self.frames = []
		self.silence_time=SILENCE
		self.trials=TRIALS
		self.multi=MULTI
		self.decode=DECODE
		self.l=LIB_FILE
		self.transcribe=TRANSCRIBE
		self.shell=OUTPUT_SHELL
		self.lang=""
		self.dic =""
		if self.WAVE_OUTPUT not in os.listdir():
			os.system("mkdir "+self.WAVE_OUTPUT)
		self.set_library(self.dlp)
		self.i=0
		self.counter=0
		self.flag=0
		
	def set_library(self, path):
		"""Function which sets the library paths in order to make it easy for every user to use.
		
		:param path: It contains the default library path.
		
		"""
		if self.l in ["commands", "Commands", "COMMANDS"]:
			self.lang = path + "commands.lm"
			self.dic = path + "commands.dic"
		elif self.l in ["characters", "Characters", "COMMANDS"]:
			self.lang = path + "characters.lm"
			self.dic = path + "characters.dic"
		elif self.l in ["num", "Num", "NUM"]:
			self.lang = path + "num.lm"
			self.dic = path + "num.dic"
		elif self.l is None:
			self.x=input("Enter Language Model")
			type(self.x)
			self.y=input("Enter Dictionary")
			type(self.y)
			self.lang = path + self.x
			self.dic = path + self.y
			
	def start(self):
		"""
		Main function which starts the entire process.
		"""
		self.stopped=threading.Event()
		self.q=Queue()
		self.listen_t=threading.Thread(target=self.listen, args=(self.stopped, self.q))
		self.listen_t.start()
		self.record_t=threading.Thread(target=self.record, args=(self.stopped, self.q))
		self.record_t.start()
	
		try:
			while not self.flag==1:
				self.listen_t.join(0.1)
				self.record_t.join(0.1)
		except KeyboardInterrupt:	#Stops the entire process if Keyboard Interrupt is pressed.
			self.stopped.set()
			self.listen_t.join()
			self.record_t.join()

	def record(self, stopped, q):
		"""
		Function which records when volume of a chunk is greater than a particular threshold value.
		
		:param stopped: Same as in listen()
		:param q: Same as in listen()
		
		""" 
		self.start=0
		self.t=self.start
		self.k=0
		while True:
		
			if stopped.wait(timeout=0):
				break
			self.chunk=q.get()	#Extracts a chunk out of the queue
			self.vol=max(self.chunk)
			if self.vol >=self.MIN_VOLUME:
				if len(self.frames)>0:
					self.k=0
				self.start=int(round(time.time()))
				self.t=self.start
				print("O"),
				self.frames.append(self.chunk)
			elif len(self.frames)>0:
				print("-"),
				if self.k==0:
					self.frames.append(self.chunk)	
					
					#Appends one chunk of silence to help recognize the words more clearly
					
					self.k=self.k+1
				self.t=int(round(time.time()))
			
			#If silence duration is more than input seconds... writes the frames to an audio file.
			
				if(int(self.t-self.start)>=int(self.silence_time)) and self.start>0:
					self.string=self.WAVE_OUTPUT+"/test"+str(self.i+1)+".wav"
					self.waveFile = wave.open(self.string, 'wb')
					self.waveFile.setnchannels(self.CHANNELS)
					self.waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
					self.waveFile.setframerate(self.RATE)
					self.waveFile.writeframes(b''.join(self.frames))
					self.waveFile.close()
					if self.multi:
						self.i += 1
					self.counter += 1
					del self.frames[:]
					self.k=0
				
				#Pauses the recording process for further operations on the audio file generated
					if self.decode:
						with self.lock:
							self.decoder()
							if self.shell is not None:
								os.system(self.shell)
					if self.trials is not None and self.trials==self.counter:
						stopped.set()
						self.flag=1
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
			edit.fileids(str(self.i +1))
			edit.transcription(str(self.i +1))
		else:
			edit.fileids(str(self.i +1))
		os.system("pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm "+str(self.lang)+" -dict "+str(self.dic)+" -samprate "+str(self.RATE)+" -nfft "+str(self.CHUNK_SIZE)+" -hyp test.hyp")

