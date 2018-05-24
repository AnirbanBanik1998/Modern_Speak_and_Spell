import time
import threading
import wave
import sys
import os
from array import array
from queue import Queue, Full
import pyaudio
audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE=int(sys.argv[1])
CHUNK_SIZE=int(sys.argv[2])
MIN_VOLUME=int(sys.argv[3])
WAVE_OUTPUT_FILENAME = "./wav/test"
lock=threading.Lock()
def main():
	stopped=threading.Event()
	q=Queue()
	global frames
	frames = []
	listen_t=threading.Thread(target=listen, args=(stopped, q))
	listen_t.start()
	record_t=threading.Thread(target=record, args=(stopped, q))
	record_t.start()
	
	try:
		while True:
			listen_t.join(0.1)
			record_t.join(0.1)
	except KeyboardInterrupt:
		stopped.set()
		
		listen_t.join()
		record_t.join()

def record(stopped, q):
	start=0
	t=start
	k=0
	while True:
		
		if stopped.wait(timeout=0):
			break
		chunk=q.get()
		vol=max(chunk)
		if vol >=MIN_VOLUME:
			if len(frames)>0:
				k=0
			start=int(round(time.time()))
			t=start
			print("O"),
			frames.append(chunk)
		elif len(frames)>0:
			print("-"),
			if k==0:
				frames.append(chunk)
				k=k+1
			t=int(round(time.time()))
			if(int(t-start)>=3) and start>0:
				string=WAVE_OUTPUT_FILENAME+"1"+".wav"
				waveFile = wave.open(string, 'wb')
				waveFile.setnchannels(CHANNELS)
				waveFile.setsampwidth(audio.get_sample_size(FORMAT))
				waveFile.setframerate(RATE)
				waveFile.writeframes(b''.join(frames))
				waveFile.close()
				del frames[:]
				k=0
				with lock:
					os.system("./lock.sh "+ sys.argv[1]+ " "+ sys.argv[2])
				print("You may again start recording...")
			
def listen(stopped, q):
	global stream
	stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK_SIZE)
	while True:
		if stopped.wait(timeout=0):
			break
		try:
			q.put(array('h', stream.read(CHUNK_SIZE)))
		except Full:
			pass
if __name__=="__main__":
	main()
