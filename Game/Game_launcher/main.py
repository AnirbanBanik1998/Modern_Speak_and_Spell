import threading
import time
import os

lock = threading.Lock()
f = open("./test.hyp", "r")
arr = f.read().split(" ")
start = 0
resume = 0
for i in range(0, len(arr)):
    if arr[i] in ("START", "start", "GENERATE", "generate"):
        start = 1
        break
if not start:
    for i in range(0, len(arr)):
        if arr[i] in ("RESUME", "resume"):
            resume = 1
            break
if start:
    for i in range(0, len(arr)):
        g = open("./previous.txt", "w+")
        g.write(arr[i])
        g.close()
        if arr[i] in ("SPELL", "spell"):
            with lock:
                '''
				Starts Spell_It! game
				'''
                cwd = os.getcwd()
                os.chdir("../Games/Spell_It!/")
                os.system("python3 Spell_gui.py")
                os.chdir(cwd)
            break
        elif arr[i] in ("HANGMAN", "hangman"):
            with lock:
                '''
				Starts Hangman game
				'''
                cwd = os.getcwd()
                os.chdir("../Games/Hangman/")
                os.system("python3 Hangman_gui.py")
                os.chdir(cwd)
            break
        elif arr[i] in ("ENCRYPTER", "encrypter"):
            with lock:
                '''
				Starts Encrypter game
				'''
                cwd = os.getcwd()
                os.chdir("../Games/Encrypter/")
                os.system("python3 Encrypter_gui.py")
                os.chdir(cwd)
            break
        elif arr[i] in ("CROSSWORD", "crossword"):
            with lock:
                '''
				Starts Crossword game
				'''
                cwd = os.getcwd()
                os.chdir("../Games/Crossword/")
                os.system("python3 Crossword.py")
                os.chdir(cwd)
            break
elif resume:
    g = open("./previous.txt", "r+")
    ar = g.read().split(" ")
    if ar[0] in ("SPELL", "spell"):
        with lock:
            cwd = os.getcwd()
            os.chdir("../Games/Spell_It!/")
            os.system("python3 Spell_gui.py")
            os.chdir(cwd)

    elif ar[0] in ("HANGMAN", "hangman"):
        with lock:
            cwd = os.getcwd()
            os.chdir("../Games/Hangman/")
            os.system("python3 Hangman_gui.py")
            os.chdir(cwd)
    elif ar[0] in ("ENCRYPTER", "encrypter"):
        with lock:
            cwd = os.getcwd()
            os.chdir("../Games/Encrypter/")
            os.system("python3 Encrypter_gui.py")
            os.chdir(cwd)
    elif ar[0] in ("CROSSWORD", "crossword"):
        with lock:
            cwd = os.getcwd()
            os.chdir("../Games/Crossword/")
            os.system("python3 Crossword.py")
            os.chdir(cwd)
