import threading
import time
import os
lock=threading.Lock()
f=open("./test.hyp","r")
arr=f.read().split(" ")
start=0
resume=0
for i in range(0, len(arr)):
	if arr[i] in ("START", "start"):
		start=1
		break
	elif arr[i] in ("RESUME", "resume"):
		resume=1
		break
if start==1:
	for i in range(0, len(arr)):
		g=open("./previous.txt", "w+")
		g.write(arr[i])
		g.close()
		if arr[i] in ("SPELL", "spell"):
			with lock:
				cwd=os.getcwd()
				os.chdir("../Games/Spell_It!/")
				os.system("python3 Spell_gui.py")
				os.chdir(cwd)
			break
		elif arr[i] in ("HANGMAN", "hangman"):
			with lock:
				cwd=os.getcwd()
				os.chdir("../Games/Hangman/")
				os.system("python3 Hangman.py")
				os.chdir(cwd)
			break
		elif arr[i] in ("ENCRYPTER", "encrypter"):
			with lock:
				cwd=os.getcwd()
				os.chdir("../Games/Encrypter/")
				os.system("python3 Enrypter.py")
				os.chdir(cwd)
			break
		elif arr[i] in ("CROSSWORD", "crossword"):
			with lock:
				cwd=os.getcwd()
				os.chdir("../Games/Crossword/")
				os.system("python3 Crossword.py")
				os.chdir(cwd)
			break
elif resume==1:
	g=open("./previous.txt", "r+")
	ar=g.read().split(" ")
	if ar[0] in ("SPELL", "spell"):
		with lock:
			cwd=os.getcwd()
			os.chdir("../Games/Spell_It!/")
			os.system("python3 Spell_It.py")
			os.chdir(cwd)
			
	elif ar[0] in ("HANGMAN", "hangman"):
		with lock:
			cwd=os.getcwd()
			os.chdir("../Games/Hangman/")
			os.system("python3 Hangman.py")
			os.chdir(cwd)
	elif ar[0] in ("ENCRYPTER", "encrypter"):
		with lock:
			cwd=os.getcwd()
			os.chdir("../Games/Encrypter/")
			os.system("python3 Encrypter.py")
			os.chdir(cwd)
	elif ar[0] in ("CROSSWORD", "crossword"):
		with lock:
			cwd=os.getcwd()
			os.chdir("../Games/Crossword/")
			os.system("python3 Crossword.py")
			os.chdir(cwd)
