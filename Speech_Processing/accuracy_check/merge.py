import wave, os
f=open("b.txt", "r")
words=f.read().split("\n")
directory=os.listdir()
for word in words:
	details=open("details.txt", "w+")
	os.system("touch "+word+".hyp")
	with open("test.fileids","w") as r:
		r.write(word)
	for d in directory:
		if os.path.isdir(d):
			os.chdir(d)
			files=os.listdir()
			for fi in files:
				filename, ext = os.path.splitext(fi)
				if ext==".wav" and filename==word:
					details.write("./"+d+"/"+fi+" ")
			os.chdir("..")
	details.close()
	details=open("details.txt", "r")
	waves=details.read().split(" ")
	os.system("sox -n -r 22050 -c 1 silence.wav trim 0.0 2")
	string=""
	for wave in waves:
		string=string+" "+wave+" "+"silence.wav"
	string = string+" "+"./wav/"+word+".wav"
	os.system("sox"+string)
f.close()
	
#piku=merge("./Aditi/CROSSWORD.wav", "./Amy/CROSSWORD.wav", 1, "CROSS")
