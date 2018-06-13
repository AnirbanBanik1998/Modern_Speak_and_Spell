import os
def fileids(n):
	os.system("truncate -s 0 test.fileids")
	f=open("./test.fileids", "w+")
	for i in range(1, (int(n)+1)):
		f.write("test"+str(i)+"\n")
	f.close()
def transcription(n):
	os.system("truncate -s 0 test.transcription")
	t=open("./test.transcription", "w+")
	for i in range(1, (int(n)+1)):
		val=input("Enter the transcription:\n")
		type(val)
		t.write(str(val)+" (test"+str(i)+")"+"\n")
	t.close()
	
