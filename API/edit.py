import os
def fileids(n):
	os.system("truncate -s 0 test.fileids")
	f=open("./test.fileids", "w")
	for i in range(1, (int(n)+1)):
		f.write("test"+str(i)+"\n")
	f.close()

