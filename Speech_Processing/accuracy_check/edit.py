import os
import sys
os.system("truncate -s 0 test.fileids")
os.system("truncate -s 0 test.transcription")
f=open("./test.fileids", "w")
t=open("./test.transcription", "w")
for i in range(1, (int(sys.argv[1])+1)):
	f.write("test"+str(i)+"\n")
	val=input("Enter the transcription:\n")
	type(val)
	t.write(str(val)+"\n")
f.close()
t.close()
