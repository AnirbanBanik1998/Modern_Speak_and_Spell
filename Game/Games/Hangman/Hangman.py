import sys
sys.path.insert(0, "../../../")
import random
import subprocess
import time
import os
import threading
from API import recorder, edit

class Hangman:
	def __init__(self):
		self.lock=threading.Lock()
		self.f= open("../Wordlist.csv",'r')
		self.rows=self.f.read().split("\n")
		self.f.close()
		self.k=0
		self.string=""
		self.str1=""
		self.counter=0
		
	def rand(self):
		'''
		Generates a random word from Wordlist.csv
		'''
		self.my_randoms=random.sample(range(0, len(self.rows)), 1)
		self.column=self.rows[self.my_randoms[0]].split(",")
		self.randcolumn=random.sample(range(0, (len(self.column)-1)), 1)
		self.column[self.randcolumn[0]]=self.column[self.randcolumn[0]].strip()
		return self.column[self.randcolumn[0]]
	
	def initialize(self, r):
		str1=""
		for i in range(0, len(r)):
			self.string=self.string+"-"
		for i in range(0,len(self.string)):
			str1=str1+self.string[i]+" "
		return(str1)
		
	def check(self, str1, l, r):
		print(" Input is "+l)
		for j in range(0, len(self.string)):
			if l==r[j] and self.string[j]=="-":
				str1=str1+l
			else:
				str1=str1+self.string[j]
		return str1
		
	def terminal(self, word):
		self.str1=self.initialize(word)
		print(self.str1)
		self.str1=""
		while self.counter<20:
			self.counter=self.counter+1
			self.str1=""
			letter=""
			print("Enter letter: ")
			with self.lock:
				record=recorder.Recorder("../../../Language_Models/", LIB_FILE="characters", SILENCE=1, TRIALS=1, DECODE=True)
				record.start()
			r=open('./test.hyp','r')					
			arr=r.read().split(" ")
			letter=arr[0]
			print(letter)
			lt=letter.lower()
			r.close()				
			try:
				self.string=str(self.check(self.str1,lt, word))
						
			except Exception as e:
				print(e)
			
			self.str1=""
			for j in range(0, len(self.string)):
				self.str1=self.str1+self.string[j]+" "
			print(self.str1)
			if self.string==word:
				subprocess.call(["espeak","You win"])
				break
			elif self.counter==20:
				subprocess.call(["espeak","You lose"])
				with self.lock:
					subprocess.call(["espeak","The answer is "+word])
				print(" Answer is: "+word)
				
obj=Hangman()
random=obj.rand()
obj.terminal(random)
