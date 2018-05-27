import os
dictionary=open("phonetic.dic", "w+")
d=os.listdir()
d.sort()
for di in d:
	p=0
	if os.path.isfile(di):
		filename, ext=os.path.splitext(di)
		
		if len(filename)==1 and ord(filename) in range(65,91):
			p=1
		if ext==".dic" and p:
			f=open(di, "r")
			words=f.read().split("\n")
			f.close()
			k=1
			for i in range(len(words)):
				if len(words[i])>0:
					dictionary.write(filename+"("+str(k)+")	"+ words[i]+"\n")
					k=k+1
dictionary.close()
