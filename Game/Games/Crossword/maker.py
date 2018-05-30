import random
f=open("./words.txt", "r")
lines=f.read().split("\n")

row=random.randint(0,1)
column=random.randint(0,1)
word1=""
word2=""
word3=""
word4=""
k=1
#print(str(row)+ " " +str(column))
def find(w, c, r):
	for i in range(0, len(lines)):
		if w[r]==lines[i][c]:
			return lines[i]
	return ""

def find_inv(x, y, p):
	#print(p)
	for i in range(0, len(lines)):
		if lines[i][p]==x and lines[i][p+2]==y:
			return lines[i]
	return ""

while k:
	wordlist = []
	my_randoms=random.randint(0,len(lines)-1)
	word1=lines[my_randoms]
	wordlist.append(word1)
	#print(word1)
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

print("Row "+str(row+1)+" " + word1)
print("Row "+str(row+3)+" " + word4)
print("Column "+str(column+1)+" " + word2)
print("Column "+str(column+3)+" " + word3)

	

