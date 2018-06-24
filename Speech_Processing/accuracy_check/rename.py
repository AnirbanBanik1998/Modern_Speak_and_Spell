import os
f=open("test.transcription", "r")
letter=f.read().split(" ")
r=open("test.hyp","r")
hyp=r.read().split(" ")
r.close()
result=""
for r in hyp[:len(hyp)-2]:
	result=result+r+" "
result=result.strip()
for l in letter:
	if l is not '' and ord(l) in range(65,91):
		with open((l+".dic"), "a+") as w:
			w.write(result+"\n")
		os.remove("test.hyp")
		break
f.close()
