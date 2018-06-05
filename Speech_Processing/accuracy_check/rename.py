import os
f=open("test.transcription", "r")
letter=f.read().split(" ")
for l in letter:
	if ord(l) in range(65,91):
		os.system("mv test.hyp "+l+".dic")
		break
f.close()
