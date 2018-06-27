import pygame
import Hangman
import subprocess
import sys
sys.path.insert(0, "../../../")
from API import recorder, edit
def message(msg, color, width, height, font_size):
	'''
	Function to display a specific message in a specific position with a specific color.
	
	:param msg: The text to be displayed.
	:param color: The font color.
	:param width: The horizontal position of the text on the screen.
	:param height: The vertical position of the text on the screen.
	:param font_size: The font size of the text.
	'''
	font=pygame.font.SysFont(None, font_size)
	screen_text=font.render(msg, True, color)
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
		message("Deduce the word...", blue, display_width/4, display_height/4, 50)
		pygame.display.update()
		hangman.str1=hangman.initialize(random_word)
		message(hangman.str1, white, display_width/2, display_height/2, 45)
		pygame.display.update()
		m=hangman.str1
		hangman.str1=""
		while hangman.counter<20:
			hangman.counter=hangman.counter+1
			hangman.str1=""
			letter=""
			print("Enter letter: ")
			with hangman.lock:
				record=recorder.Recorder("../../../Language_Models/", LIB_FILE="characters", SILENCE=1, TRIALS=1, DECODE=True)
				record.start()
			r=open('./test.hyp','r')					
			arr=r.read().split(" ")
			letter=arr[0]
			print(letter)
			lt=letter.lower()
			r.close()				
			try:
				hangman.string=str(hangman.check(hangman.str1,lt, random_word))
						
			except Exception as e:
				print(e)
			
			hangman.str1=""
			for j in range(0, len(hangman.string)):
				hangman.str1=hangman.str1+hangman.string[j]+" "
			message(m, black, display_width/2, display_height/2, 45)
			pygame.display.update()
			message(hangman.str1, white, display_width/2, display_height/2, 45)
			pygame.display.update()
			m=hangman.str1
			if hangman.string==random_word:
				message("You Win", green, display_width/4, (3*display_height)/4, 45)
				pygame.display.update()
				subprocess.call(["espeak","You win"])
				break
			elif hangman.counter==20:
				subprocess.call(["espeak","You lose"])
				with hangman.lock:
					subprocess.call(["espeak","The answer is "+random_word])
				message("You Lose...Answer is: "+random_word, red, display_width/4, (3*display_height)/4, 45)
				pygame.display.update()
				gameExit=True
		clock.tick(20)
	subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
	pygame.quit()
	quit()

if __name__=="__main__":
	main()