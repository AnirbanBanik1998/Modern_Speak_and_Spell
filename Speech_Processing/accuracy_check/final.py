import os
d=os.listdir()
for di in d:
	if os.path.isfile(di):
		filename, ext=os.path.splitext(di)
		if ext==".dic":
			f=open(di, "r")
			words=f.read().split("\n")
			f.close()
			words.sort()
			word = []
			word = [words[i] for i in range(len(words)-1) if words[i]!=words[i+1]]
			f=open(di, "w")
			for i in range(len(word)):
				f.write(word[i]+"\n")
			f.close()

