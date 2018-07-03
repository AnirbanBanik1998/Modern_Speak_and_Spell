'''
Updated Version of Hangman Game
'''
import sys
sys.path.insert(0, "../../../")
import random
import subprocess
import time
import os
import threading
from API import recorder, edit
<<<<<<< HEAD

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
		'''
		Displays the word in form of dashes.
		
		:param r: Random word generated.
		'''
		str1=""
		for i in range(0, len(r)):
			self.string=self.string+"-"
		for i in range(0,len(self.string)):
			str1=str1+self.string[i]+" "
		return(str1)
		
	def check(self, str1, l, r):
		'''
		Function to check if input letter is present anywhere in the word
		
		:param str1: To compute the updated string.
		:param l: The input letter.
		:param r: The word generated using rand().
		
		:return: The updated word after insertion of the input letter, if present in the actual word.
		'''
		print(" Input is "+l)
		for j in range(0, len(self.string)):
			if l==r[j] and self.string[j]=="-":
				str1=str1+l
			else:
				str1=str1+self.string[j]
		return str1
		
	def terminal(self, word):
		'''
		Calls the other functions to run the entire terminal version of the game.
		
		:param word: The word which is generated randomly using function rand()
		'''
		self.str1=self.initialize(word)
		print(self.str1)
		self.str1=""
		while self.counter<20:
			self.counter=self.counter+1
			self.str1=""
=======
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
	
def main():
	'''
	The main block of the program which runs the entire display.
	'''
	pygame.init() #Initialize pygame
	hangman=Hangman.Hangman()
	global m
	m=""
	while True:
		try:
			random_word=hangman.rand()
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
	pygame.display.set_caption("Hangman")
	pygame.display.update()	#Update the specific modification
	clock=pygame.time.Clock()
	gameExit= False
	while not gameExit:
		message("Hangman", blue, display_width/7, display_height/7, 50)
		pygame.display.update()
		message("Deduce the word...", white, display_width/4, display_height/4, 30)
		pygame.display.update()
		hangman.str1=hangman.initialize(random_word)
		message(hangman.str1, white, display_width/2, display_height/2, 40, True)
		pygame.display.update()
		m=hangman.str1
		hangman.str1=""
		while hangman.counter<20:
			hangman.counter=hangman.counter+1
			hangman.str1=""
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
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
<<<<<<< HEAD
				self.string=str(self.check(self.str1,lt, word))
=======
				hangman.string=str(hangman.check(hangman.str1, lt, random_word))
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
						
			except Exception as e:
				print(e)
			
<<<<<<< HEAD
			self.str1=""
			for j in range(0, len(self.string)):
				self.str1=self.str1+self.string[j]+" "
			print(self.str1)
			if self.string==word:
=======
			hangman.str1=""
			for j in range(0, len(hangman.string)):
				hangman.str1=hangman.str1+hangman.string[j]+" "
			message(m, black, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			message(hangman.str1, white, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			m=hangman.str1
			if hangman.string==random_word:
				message("You Win", green, display_width/2, (3*display_height)/4, 45, True)
				pygame.display.update()
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
				subprocess.call(["espeak","You win"])
				break
			elif self.counter==20:
				subprocess.call(["espeak","You lose"])
<<<<<<< HEAD
				with self.lock:
					subprocess.call(["espeak","The answer is "+word])
				print(" Answer is: "+word)
				
=======
				with hangman.lock:
					subprocess.call(["espeak","The answer is "+random_word])
				message("You Lose...Answer is: "+random_word, red, display_width/2, (3*display_height)/4, 45, True)
				pygame.display.update()
				gameExit=True
		clock.tick(20)
	subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
	pygame.quit()
	quit()

if __name__=="__main__":
	main()
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
