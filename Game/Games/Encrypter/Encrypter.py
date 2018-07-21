import sys
sys.path.insert(0, "../../../")
import threading 
import os
import subprocess
import random
from API import recorder, edit

class Encrypter:
	def __init__(self):
		self.lock=threading.Lock()
		self.f= open("../Wordlist.csv",'r')
		self.rows=self.f.read().split("\n")
		self.f.close()
		self.counter=0
		
	def rand_word(self):
		'''
		Generates a random word from Wordlist.csv
		'''
		self.my_randoms=random.sample(range(0, len(self.rows)), 1)
		self.column=self.rows[self.my_randoms[0]].split(",")
		self.randcolumn=random.sample(range(0, (len(self.column)-1)), 1)
		self.column[self.randcolumn[0]]=self.column[self.randcolumn[0]].strip()
		return self.column[self.randcolumn[0]]
		
	def choose(self):
		'''
		Module to help take the user input for the chosen option. The valid inputs are 1, 2 and 3.
		'''
		subprocess.call(["espeak"," Choose your option 1 Encode 2 Decode 3 Guess "])
		with self.lock:
			record=recorder.Recorder("../../../Language_Models/", LIB_FILE="num", TRIALS=1, DECODE=True, SILENCE=1)
			record.start()
		r=open('./test.hyp','r')					
		arr=r.read().split(" ")
		letter=arr[0]
		r.close()
		return letter
		
	def shift(self, word, n):
		'''
		Used to shift each letter in a word by n...in order to encrypt or decrypt the word...the sequence is cyclic...that is a to z and then back to a.
		
		:param word: The word to be encrypted or decrypted.
		:param n: The shifting key.
		
		:return: The word with all the letters shifted, as a list type value.
		'''
		f = ["" for x in range(len(word))]
		for i in range(0,len(word)):
			if ord(word[i])+n > 122:
				f[i]=chr(97+ord(word[i])+n-123)
			else:
				f[i]=chr(ord(word[i])+n)
		return f
		
	def rand_int(self):
		'''
		Picks up a random integer between 1 and 25, including both.
		'''
		ran=random.randint(1,25)
		return ran
		
	def test(self, string, w):
		'''
		Function to take the recording and check if it matches with the letters.
		
		:param string: The string to be formed as the result.
		:param w: The specific letter to be checked.
		
		:return: Returns string, improvised by the function itself.
		'''
		self.counter+=1
		with self.lock:
			record=recorder.Recorder("../../../Language_Models/", SILENCE=1, TRIALS=1, DECODE=True, LIB_FILE="characters", OUTPUT_SHELL="./decoder.sh")
			record.start()
		f=open("./file.txt", "r")
		letter=f.read().strip()
		if letter.lower()==w:
			string=string+w
			return string
		else:
			return "-"
			
	def check(self, word):
		'''
		The number of trials being 20, the user is allowed to try to encrypt or decrypt the given word correctly.
		
		:param word: Takes the randomly generated word from rand_word() as input parameter.
		'''
		w=""
		i=0
		while i<len(word) and self.counter<=20:
			w1=self.test(w, word[i])
			if w1 is not "-":
				w=w1
				print(w.upper())
				i+=1
			else:
				print((w+w1).upper())
			if w==word:
				subprocess.call(["espeak","-s","125"," Good!"])
				break
			if self.counter>20:
				subprocess.call(["espeak","-s","125"," No you are wrong...the answer will be "])
				for j in word:
					subprocess.call(["espeak","-s","100", j])
					
	def score(self, output=None, word=None, trials=0, choice=None):
		'''
		Finds out the user's score after comparing with the original word.
		
		:param output: The part of the word formed due to user input.
		:param word: The original word.
		:param trials: The number of trials taken to get to the right answer.
		:param choice: The gaming option chosen as user-input.
		
		:return: The user's score out of 10
		'''
		if choice in {"1","2"}:
			score=(len(output)/len(word))*10
			return score
		else:
			score=10-trials
			return score
		
	def terminal(self, choice, random_word):
		'''
		Main module to run the entire game in terminal
		
		:param choice: Choice 1, 2 or 3 as user input.
		:param random_word: Random word generated using rand_word()
		'''
		if choice=="1":
			s=self.rand_int()
			hint=self.shift("anirban", s)
			with self.lock:
				subprocess.call(["espeak"," If anirban is encoded as "+str(hint)])
			hint_str=""
			for h in hint:
				hint_str=hint_str+h
			print("anirban -> "+hint_str)
			encode=self.shift(random_word, s)
			with self.lock:
				subprocess.call(["espeak"," Then encode "+random_word])
			print(random_word+ " ->" +" ?")
			self.check(encode)
			
		elif choice=="2":
			s=self.rand_int()
			hint=self.shift("anirban", s)
			hint_str=""
			for h in hint:
				hint_str=hint_str+h
			with self.lock:
				subprocess.call(["espeak"," If "+str(hint)+ "is decoded as anirban"])
			print(hint_str+" -> anirban")
			encode=self.shift(random_word, s)
			with self.lock:
				subprocess.call(["espeak"," Then decode "+str(encode)])
			encode_str=""
			for h in encode:
				encode_str=encode_str+h
			print(encode_str+ " ->" +" ?")
			self.check(random_word)
			
		elif choice=="3":
			s=self.rand_int()
			e=""
			encode=self.shift(random_word, s)
			encode_str=""
			for p in encode:
				encode_str=encode_str+p
			print(random_word+"-> "+encode_str)
			for k in range(10):
				subprocess.call(["espeak"," Enter shifting key"])
				with self.lock:
					rec=recorder.Recorder("../../../Language_Models/", LIB_FILE="num", TRIALS=1, DECODE=True, SILENCE=1)
					rec.start()
				r=open('./test.hyp','r')					
				arr=r.read().split(" ")
				num=arr[0]
				r.close()
				try:
					e=encrypter.shift(random_word, int(num))
				except Exception as z:
					print(z)
				e_str=""
				for p in e:
					e_str=e_str+p
				print(e_str)
				if e_str==encode_str:
					subprocess.call(["espeak","-s","120"," Good!"])
				elif k==9:
					subprocess.call(["espeak","-s","120"," No you are wrong...the answer will be "])
					for j in random_word:
						subprocess.call(["espeak","-s","100", j])
						
		else:
			subprocess.call(["espeak"," Wrong choice"])
			

