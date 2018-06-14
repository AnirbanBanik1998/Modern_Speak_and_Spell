import random
import threading
import subprocess
import time
import os
from API import recorder, edit
lock=threading.Lock()
f= open("../Wordlist.csv",'r')
rows=f.read().split("\n")
k=0
j=0
print("Spell It!")
string=""
str1=""
answer=""
my_randoms=random.sample(range(0, len(rows)), 1)
column=rows[my_randoms[0]].split(",")
randcolumn=random.sample(range(0, (len(column)-1)), 1)
column[randcolumn[0]]=column[randcolumn[0]].strip()
subprocess.call(["espeak","-s","100"," Spell "+column[randcolumn[0]]])
with lock:
	record=recorder.Recorder("../../../Language_Models/", SILENCE=1, TRIALS=len(column[randcolumn[0]]), DECODE=True, OUTPUT_SHELL="./decoder.sh")
	record.start()
r=open("./file.txt", "r+")
word=r.read().split(" ")
string = ""
for i in range(0, len(word)):
	string=string + word[i]
if string==column[randcolumn[0]]:
	subprocess.call(["espeak","-s","150"," Good!"])

else:
	subprocess.call(["espeak","-s","150"," No you are wrong...the answer will be "])
	for i in range(0, len(column[randcolumn[0]])):
		subprocess.call(["espeak","-s","100", column[randcolumn[0]][i]])
subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
os.system("truncate -s 0 file.txt")
f.close()
r.close()
