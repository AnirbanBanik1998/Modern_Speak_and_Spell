import random
import os
f=open("./words.csv", "r")
lines=f.read().split("\n")

row=random.randint(0,1)
column=random.randint(0,1)
word1=""
word2=""
word3=""
word4=""
k=1
def find(w, c, r):
	for i in range(0, len(lines)):
		g=lines[i].split(",")
		if w[r]==g[0][c]:
			return g[0]
	return ""

def find_inv(x, y, p):
	for i in range(0, len(lines)):
		g=lines[i].split(",")
		if g[0][p]==x and g[0][p+2]==y:
			return g[0]
	return ""

while k:
	wordlist = []
	my_randoms=random.randint(0,len(lines)-1)
	g=lines[my_randoms].split(",")
	word1=g[0]
	wordlist.append(word1)
	try:
		word2=find(word1, row, column)
		wordlist.append(word2)
		word3=find(word1, row, (column+2))
		wordlist.append(word3)
	except:
		word2=""
		word3=""
	if word2 == "" or word3 == "":
		k=1
	else:
		try:
			word4=find_inv(word2[row+2], word3[row+2], column)
			wordlist.append(word4)
			if len(wordlist) != len(set(wordlist)):
				k=1
			else:
				k=0
		except:
			word4=""
			k=1
'''
print("Row "+str(row+1)+" " + word1)
print("Row "+str(row+3)+" " + word4)
print("Column "+str(column+1)+" " + word2)
print("Column "+str(column+3)+" " + word3)
'''
os.system("python3 Crossword.py"+ word1+ " "+ word2+ " "+ word3+ " "+ word4+ " "+ str(row)+ " "+ str(column))

