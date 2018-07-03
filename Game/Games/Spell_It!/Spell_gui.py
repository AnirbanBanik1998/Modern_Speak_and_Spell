<<<<<<< HEAD
# Spell It!

## Introduction

This is a very simple game...a game in which the user has to spell a word given out and based on whether the word is spelt correct or wrong the results are generated accordingly.

## How to Play

* Open a terminal and move to this directory.
* Run the entire process:
```
python3 Spell_It.py
```
* Now the entire process is automated...spell out the word given to you and the results will be generated.

## Documentation

### `Spell_It.py`

Main program...takes out words at random from the wordlist and asks to spell them out. It can be used to play the terminal version of the game.

* `Spell`: Main class containing all the core functionality of the game.
* `random()`: Generates a random word from Wordlist.csv.
* `test(string, w)`: Function to take the recording and check if it matches with the letters.
1. **string** -> The string to be formed as the result of the operations performed.
2. **w** -> The specific letter to be checked.
* `terminal(word)`: Main function to take care of the whole process, and generate the terminal version of the game, often calling the test() function to aid in the process.
1. **word** -> The randomly generated word from rand().

### `Spell_gui.py`

Generates GUI using pygame, for Spell It!, using core functionality from Spell_It.py script.

* `message(msg, color, width, height, font_size)`: Function to display a specific message in a specific position with a specific color. Is also used for overwriting the previously displayed messages.
1. **msg** -> The text to be displayed.
2. **color** -> The font color.
3. **width** -> The horizontal position of the text on the screen.
4. **height** -> The vertical position of the text on the screen.
5. **font_size** -> The font size of the text.
* `main`: The main block of code to generate the GUI using pygame.

### `decoder.sh`

Automating the running of file.py

### `file.py`

Operates on the hypothesis file.
=======
import pygame
import Spell_It
import subprocess
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
	global m
	m=""
	spell=Spell_It.Spell()
	pygame.init() #Initialize pygame
	white=(255,255,255)
	red=(255,0,0)
	black=(0,0,0)
	global gameDisplay
	gameDisplay=pygame.display.set_mode((800,600)) #Pass a tuple as a parameter
	display_width=800
	display_height=600
	pygame.display.set_caption("Spell_It!")
	pygame.display.update()	#Update the specific modification
	clock=pygame.time.Clock()
	gameExit= False
	while True:
		try:
			random_word=spell.rand()
			break
		except Exception as e:
			print(e)
	while not gameExit:
		message("Spell It...", red, display_width/7, display_height/7, 50)
		pygame.display.update()
		w=""
		i=0
		while i<len(random_word) and spell.counter<=20:
			
			w1=spell.test(w, random_word[i])
			message(m, black, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			
			if w1 is not "-":
				w=w1
				message(w.upper(), white, display_width/2, display_height/2, 45, True)
				pygame.display.update()
				m=w.upper()
				i+=1
			else:
				message((w+w1).upper(), white, display_width/2, display_height/2, 45, True)
				pygame.display.update()
				m=(w+w1).upper()
			if w==random_word:
				subprocess.call(["espeak","-s","125"," Good!"])
				gameExit=True
				break
			if spell.counter>20:
				subprocess.call(["espeak","-s","125"," No you are wrong...the answer will be "])
				for j in random_word:
					subprocess.call(["espeak","-s","100", j])
				gameExit=True
		clock.tick(20)
	subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
	pygame.quit()
	quit()
	
if __name__=="__main__":
	main()
>>>>>>> bcc0d509e1c312fb688b9ba0cd6cdb74bd38bae7
