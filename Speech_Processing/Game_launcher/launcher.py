import threading
import time
lock=threading.Lock()
f=open("./test.hyp","r")
arr=f.read().split(" ")
start=0
for i in range(0, len(arr)):
	if arr[i] in ("START", "start"):
		start=1
		break
if start==1:
	for i in range(0, len(arr)):
		if arr[i] in ("SPELL", "spell"):
			time.sleep(2)
			with lock:
				print("Start Spell It!...")
			break
		elif arr[i] in ("HANGMAN", "hangman"):
			time.sleep(2)
			with lock:
				print("Start Hangman...")
			break
		elif arr[i] in ("ENCRYPTER", "encrypter"):
			time.sleep(2)
			with lock:
				print("Start Encrypter...")
			break
		elif arr[i] in ("CROSSWORD", "crossword"):
			time.sleep(2)
			with lock:
				print("Start Crossword...")
			break

