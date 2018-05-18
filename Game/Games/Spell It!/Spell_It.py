import random
import threading
import subprocess
import time
import os
lock=threading.Lock()
f= open("./Wordlist.csv",'r')
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
	os.system("./echo.sh "+str(len(column[randcolumn[0]])))
f=open("./file.txt", "r+")
word=f.read().split(" ")
string = ""
for i in range(0, len(word)):
	string=string + word[i]
if string==column[randcolumn[0]]:
	subprocess.call(["espeak","-s","150"," Good!"])

else:
	subprocess.call(["espeak","-s","150"," No you are wrong...the answer will be "])
	for i in range(0, len(column[randcolumn[0]])):
		subprocess.call(["espeak","-s","100", column[randcolumn[0]][i]])
subprocess.call(["espeak","-s","150"," Options are 1: Quit or 2: Resume"])
os.system("truncate -s 0 file.txt")
	
