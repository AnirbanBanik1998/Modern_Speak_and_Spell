import os
f=open("c.txt", "r")
lines=f.read().split("\n")
data=os.listdir()
for line in lines:
	fi=open((line+".hyp"), "w")
	print(line)
	r=open((line+".dic"), "r")
	ar=r.read().split("\n")
	for j in range(len(ar)):
		arr=ar[j].split(" ")
		for i in range(len(arr)):
			fi.write(arr[i])
		fi.write(" ")
	fi.write("("+line+")")
	fi.close()	
	with open("./test.fileids", "w") as w:
		w.write(line)
	fid=open("./test.transcription", "w")
	for i in range(47):
		fid.write(line+" ")
	fid.write("("+line+")")
	fid.close()
	os.system("./stat.sh "+line+".hyp")
	
f.close()
	
