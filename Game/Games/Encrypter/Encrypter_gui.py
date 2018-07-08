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
	
def check(word, choice):
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
	message("Score out of 10: "+str(encrypter.score(w, word, choice=choice)), green, display_width/2, (5*display_height)/6, 40, True)
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
				subprocess.call(["espeak"," If anirban is encoded as "+str(hint)])
			hint_str=""
			for h in hint:
				hint_str=hint_str+h
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
			check(encode_str, choice)
						
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
				subprocess.call(["espeak"," Then decode "+str(encode)])
			encode_str=""
			for h in encode:
				encode_str=encode_str+h
			message(encode_str+ " ->" +" ?", white, display_width/4, display_height/3, 30)
			pygame.display.update()
			check(random_word, choice)
			
		elif choice=="3":
		
			# Runs Guessing Game to guess the shifting key for arriving at the correct answer
			e=""
			s=encrypter.rand_int()
			encode=encrypter.shift(random_word, s)
			encode_str=""
			for p in encode:
				encode_str=encode_str+p
			message(random_word+"->"+encode_str, white, display_width/4, display_height/4, 30)
			pygame.display.update()
			message(random_word.upper(), white, display_width/2, display_height/2, 40, True)
			pygame.display.update()
			m=random_word
			for k in range(10):
				subprocess.call(["espeak"," Enter shifting key"])
				with encrypter.lock:
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
				message(m.upper(), black, display_width/2, display_height/2, 40, True)
				pygame.display.update()
				e_str=""
				for p in e:
					e_str=e_str+p
				message(e_str.upper(), white, display_width/2, display_height/2, 40, True)
				pygame.display.update()
				m=e_str
				if e_str==encode_str:
					subprocess.call(["espeak","-s","120"," Good!"])
					break
				elif k==9:
					subprocess.call(["espeak","-s","120"," No you are wrong...the answer will be "+str(s)])
					message("Answer-> "+str(s), red, display_width/2, (3*display_height)/4, 45, True)
					pygame.display.update()
					k+=1
			message("Score out of 10: "+str(encrypter.score(trials=k, choice=choice)), green, display_width/2, (5*display_height)/6, 40, True)
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
