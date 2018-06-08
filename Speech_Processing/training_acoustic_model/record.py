import time
import threading
import wave
import sys
import os
import subprocess
from array import array
from queue import Queue, Full
import pyaudio
audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE=int(sys.argv[1])
CHUNK_SIZE=int(sys.argv[2])
MIN_VOLUME=int(sys.argv[3])
WAVE_OUTPUT_FILENAME = "./test"
lock=threading.Lock()
fr=open("test.transcription", "r")
lines=fr.read().split("\n")
length=len(lines)
fr.close()
def main():
	stopped=threading.Event()
	q=Queue()
	global frames
	frames = []
	#global listen_t
	#global record_t
	
	listen_t=threading.Thread(target=listen, args=(stopped, q))
	listen_t.start()
	record_t=threading.Thread(target=record, args=(stopped, q))
	record_t.start()
	
	try:
		subprocess.call(["espeak", "Speak out the letter below"])
		word=lines[record.i].split(" ")
		print(word[0])
		while record.flag==0:
			listen_t.join(0.1)
			record_t.join(0.1)
	except :			#Stops the entire process if the recording has been done the required number of times.
		stopped.set()
		
		listen_t.join()
		record_t.join()
	
def record(stopped, q):
	record.flag=0
	start=0
	t=start
	k=0
	while True:
		
		if stopped.wait(timeout=0):
			break
		chunk=q.get()	#Extracts a chunk out of the queue
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
				frames.append(chunk)	#Appends one chunk of silence to help recognize the words more clearly
				k=k+1
			t=int(round(time.time()))
			
			#If silence duration is more than 1 second... writes the frames to an audio file.
			
			if(int(t-start)>=1) and start>0:
				string=WAVE_OUTPUT_FILENAME+str(record.i + 1)+".wav"
				waveFile = wave.open(string, 'wb')
				waveFile.setnchannels(CHANNELS)
				waveFile.setsampwidth(audio.get_sample_size(FORMAT))
				waveFile.setframerate(RATE)
				waveFile.writeframes(b''.join(frames))
				waveFile.close()
				record.i += 1
				del frames[:]
				k=0
				if (length-1)>record.i:
					word=lines[record.i].split(" ")
					print(word[0])
				#Checking if number of times the recording process has operated equals the length of word.
				
				else:
					stopped.set()
					record.flag=1
record.i=0
			
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
