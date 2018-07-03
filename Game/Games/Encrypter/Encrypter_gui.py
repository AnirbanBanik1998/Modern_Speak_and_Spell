<<<<<<< HEAD
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
				f[i]=chr(97+ord(word[i])+n-122)
			else:
				f[i]=chr(ord(word[i])+n)
		return f
		
	def rand_int(self):
		'''
		Picks up a random integer between 1 and 25, including both.
		'''
		ran=random.randint(1,26)
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
=======
import pygame
import Encrypter
import subprocess
import sys
sys.path.insert(0, "../../../")
from API import recorder, edit
def message(msg, color, width, height, font_size, center=False):
	'''
	Function to display a specific message in a specific position with a specific color.
	
	:param msg: The text to be displayed.
	:param color: The font color.
	:param width: The horizontal position of the text on the screen.
	:param height: The vertical position of the text on the screen.
	:param font_size: The font size of the text.
	:param center: Boolean value to determine if text will be aligned to the center or not.
	'''
	font=pygame.font.SysFont(None, font_size)
	screen_text=font.render(msg, True, color)
	if center==True:
		text_rect=screen_text.get_rect(center=(width, height))
		gameDisplay.blit(screen_text, text_rect)
	else:
		gameDisplay.blit(screen_text, [width, height])
	
def check(word):
	'''
	Performs the same function as that of check() function of class Encrypter..except that the messages are displayed to the GUI rather than being printed out to the console.
	
	:param word: The input word to be operated on.
	'''
	w=""
	i=0
	m=""
	while i<len(word) and encrypter.counter<=20:
		w1=encrypter.test(w, word[i])
		message(m, black, display_width/2, display_height/2, 40, True)
		pygame.display.update()
		if w1 is not "-":
			w=w1
			message(w.upper(), white, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			m=w.upper()
			i+=1
		else:
			message((w+w1).upper(), white, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			m=(w+w1).upper()
		if w==word:
			subprocess.call(["espeak","-s","125"," Good!"])
			message("Good", green, display_width/2, (3*display_height)/4, 45, True)
			pygame.display.update()
			break
		if encrypter.counter>20:
			subprocess.call(["espeak","-s","125"," No you are wrong...the answer will be "])
			for j in word:
				subprocess.call(["espeak","-s","100", j])
			message("Answer-> "+word, red, display_width/2, (3*display_height)/4, 45, True)
			pygame.display.update()
					
def main():	
	'''
	The main block of the program which runs the entire display.
	'''
	pygame.init() #Initialize pygame
	global encrypter
	encrypter=Encrypter.Encrypter()
	global m, black, white, green, blue, red, display_width, display_height
	choice=""
	m=""
	while True:
		try:
			random_word=encrypter.rand_word()
			break
		except Exception as e:
			print(e)
	white=(255,255,255)
	red=(255,0,0)
	black=(0,0,0)
	blue=(0,0,255)
	green=(0,255,0)
	global gameDisplay
	gameDisplay=pygame.display.set_mode((800,600)) #Pass a tuple as a parameter
	display_width=800
	display_height=600
	pygame.display.set_caption("Encrypter")
	pygame.display.update()	#Update the specific modification
	clock=pygame.time.Clock()
	gameExit= False
	while not gameExit:
		message("Encrypter", blue, display_width/7, display_height/7, 50)
		pygame.display.update()
		while True:
			choice=encrypter.choose()
			if choice is not "":
				break
		if choice=="1":
		
			# Runs Encode Game
			
			s=encrypter.rand_int()
			hint=encrypter.shift("anirban", s)
			with encrypter.lock:
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
				subprocess.call(["espeak"," If anirban is encoded as "+str(hint)])
			hint_str=""
			for h in hint:
				hint_str=hint_str+h
<<<<<<< HEAD
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
=======
			message("anirban -> "+hint_str , white, display_width/4, display_height/4, 30)
			pygame.display.update()
			encode=encrypter.shift(random_word, s)
			with encrypter.lock:
				subprocess.call(["espeak"," Then encode "+random_word])
			message(random_word+ " ->" +" ?", white, display_width/4, display_height/3, 30)
			pygame.display.update()
			encode_str=""
			for h in encode:
				encode_str=encode_str+h
			check(encode_str)
						
		elif choice=="2":
		
			# Runs Decode Game
			
			s=encrypter.rand_int()
			hint=encrypter.shift("anirban", s)
			hint_str=""
			for h in hint:
				hint_str=hint_str+h
			with encrypter.lock:
				subprocess.call(["espeak"," If "+str(hint)+ "is decoded as anirban"])
			message(hint_str+" -> anirban", white, display_width/4, display_height/4, 30)
			pygame.display.update()
			encode=encrypter.shift(random_word, s)
			with encrypter.lock:
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
				subprocess.call(["espeak"," Then decode "+str(encode)])
			encode_str=""
			for h in encode:
				encode_str=encode_str+h
<<<<<<< HEAD
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
=======
			message(encode_str+ " ->" +" ?", white, display_width/4, display_height/3, 30)
			pygame.display.update()
			check(random_word)
			
		elif choice=="3":
		
			# Runs Guessing Game to guess the shifting key for arriving at the correct answer
			
			s=encrypter.rand_int()
			encode=encrypter.shift(random_word, s)
			for k in range(10):
				subprocess.call(["espeak"," Enter shifting key"])
				with encrypter.lock:
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
					rec=recorder.Recorder("../../../Language_Models/", LIB_FILE="num", TRIALS=1, DECODE=True, SILENCE=1)
					rec.start()
				r=open('./test.hyp','r')					
				arr=r.read().split(" ")
				num=arr[0]
				r.close()
				try:
<<<<<<< HEAD
					e=encrypter.shift(random_word, int(num))
				except Exception as z:
					print(z)
				e_str=""
				for p in e:
					e_str=e_str+p
				print(e_str)
				if e_str==encode_str:
=======
					e=encrypter.shift(encode, int(num))
				except Exception as z:
					print(z)
				message(m.upper(), black, display_width/2, display_height/2, 40, True)
				pygame.display.update()
				e_str=""
				for p in e:
					e_str=e_str+p
				message(e_str.upper(), white, display_width/2, display_height/2, 40, True)
				pygame.display.update()
				m=e_str
				if e_str==random_word:
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
					subprocess.call(["espeak","-s","120"," Good!"])
				elif k==9:
					subprocess.call(["espeak","-s","120"," No you are wrong...the answer will be "])
					for j in random_word:
						subprocess.call(["espeak","-s","100", j])
<<<<<<< HEAD
						
		else:
			subprocess.call(["espeak"," Wrong choice"])
			

=======
					message("Answer-> "+random_word, red, display_width/2, (3*display_height)/4, 45, True)
					pygame.display.update()
		else:
			message("Wrong Choice", red, display_width/2, display_height/2, 45, True)
			pygame.display.update()
		gameExit=True
		clock.tick(20)
	subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
	pygame.quit()
	quit()
if __name__=="__main__":
	main()
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
