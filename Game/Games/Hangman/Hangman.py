import random
import subprocess
import time
import os
import threading
from API import recorder, edit
lock=threading.Lock()
f= open("../Wordlist.csv",'r')
rows=f.read().split("\n")
k=0
print("Enter one letter in a single try:")
string=""
str1=""
my_randoms=random.sample(range(0, len(rows)), 1)
column=rows[my_randoms[0]].split(",")
randcolumn = random.sample(range(0, (len(column) - 1)), 1)
column[randcolumn[0]]=column[randcolumn[0]].strip()
for i in range(0, len(column[randcolumn[0]])):
	string=string+"-"
for i in range(0,len(string)):
	str1=str1+string[i]+" "
print (str1)
		
str1=""
def check(str1,l):
	print(" Input is "+l)
	for j in range(0, len(string)):
		if l==column[randcolumn[0]][j] and string[j]=="-":
			str1=str1+l
		else:
			str1=str1+string[j]
	return str1
while k<20:
	k=k+1
	str1=""
	letter=""
	print("Enter letter: ")
	with lock:
		record=recorder.Recorder("../../../Language_Models/", LIB_FILE="characters", SILENCE=1, TRIALS=1, DECODE=True)
		record.start()
	r=open('./test.hyp','r')					
	arr=r.read().split(" ")
	letter=arr[0]
	print(letter)
	lt=letter.lower()
	r.close()				
	try:
		string=str(check(str1,lt))
						
	except:
		print("Not Possible")
			
	str1=""
	for j in range(0, len(string)):
		str1=str1+string[j]+" "
	print(str1)
	if string==column[randcolumn[0]]:
		subprocess.call(["espeak","You win"])
		break
	elif k==20:
		subprocess.call(["espeak","You lose"])
		with lock:
			subprocess.call(["espeak","The answer is "+column[randcolumn[0]]])
		print(" Answer is: "+column[randcolumn[0]])
	
subprocess.call(["espeak","-s","125"," Options are 1: Resume and 2: Start another game"])
f.close()
