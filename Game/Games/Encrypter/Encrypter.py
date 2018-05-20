import threading 
import os
import subprocess
import random
lock=threading.Lock()
f= open("../Wordlist.csv",'r')
rows=f.read().split("\n")
my_randoms=random.sample(range(0, len(rows)), 1)
column=rows[my_randoms[0]].split(",")
randcolumn=random.sample(range(0, (len(column)-1)), 1)
column[randcolumn[0]]=column[randcolumn[0]].strip()
subprocess.call(["espeak"," Choose your option 1 Encode 2 Decode 3 Guess "])
with lock:
	os.system("./choose.sh")
r=open('./test.hyp','r')					
arr=r.read().split(" ")
letter=arr[0]
r.close()
print(letter)
if letter==str(1):
	s=rand()
	hint=shift("Anirban", s)
	with lock:
		subprocess.call(["espeak"," If Anirban is encoded as "+hint])
	print("Anirban -> "+hint)
	encode=shift(column[randcolumn[0]], s)
	with lock:
		subprocess.call(["espeak"," Then encode "+column[randcolumn[0]]])
	print(column[randcolumn[0]]+ " ->" +" ?")
	with lock:
		os.system("./endec.sh "+str(len(column[randcolumn[0]])))
	files(encode)
elif letter==str(2):
	s=rand()
	hint=shift("Anirban", s)
	with lock:
		subprocess.call(["espeak"," If "+hint+ "is decoded as Anirban"])
	print(hint+" -> Anirban")
	encode=shift(column[randcolumn[0]], s)
	with lock:
		subprocess.call(["espeak"," Then decode "+encode])
	print(encode+ " ->" +" ?")
	with lock:
		os.system("./endec.sh "+str(len(column[randcolumn[0]])))
	files(column[randcolumn[0]])
	
	
	
elif letter==str(3):
	s=rand()
	encode=shift(column[randcolumn[0]], s)
	for k in range(10):
		subprocess.call(["espeak"," Enter shifting key"])
		with lock:
			os.system("./key.sh")
		r=open('./test.hyp','r')					
		arr=r.read().split(" ")
		num=arr[0]
		r.close()
		e=shift(encode, num)
		print(e)
		if e==column[randcolumn[0]]:
			subprocess.call(["espeak","-s","120"," Good!"])
		elif k==9:
			subprocess.call(["espeak","-s","120"," No you are wrong...the answer will be "])
			for j in range(0, len(column[randcolumn[0]])):
				subprocess.call(["espeak","-s","100", column[randcolumn[0]][i]])

else:
	subprocess.call(["espeak"," Wrong choice"])
def shift(word, n):
	f = ["" for x in range(len(word))]
	for i in range(0,len(word)):
		if ord(word[i])+n > 122:
			f[i]=chr(97+ord(word[i])+n-122)
		else:
			f[i]=chr(ord(word[i])+n)
	return f

def rand():
	ran=random.randint(1,26)
	return ran
			
			
def files(w):
	f=open("./file.txt", "r+")
	word=f.read().split(" ")
	string = ""
	for i in range(0, len(word)):
		string=string + word[i]
	if string==w:
		subprocess.call(["espeak","-s","150"," Good!"])

	else:
		subprocess.call(["espeak","-s","150"," No you are wrong...the answer will be "])
		for i in range(0, len(w)):
			subprocess.call(["espeak","-s","100", w[i]])
	f.close()
