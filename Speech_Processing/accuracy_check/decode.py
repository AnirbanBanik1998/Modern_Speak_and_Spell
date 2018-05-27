import os
os.chdir("./audio")
arr=os.listdir()
for wave in arr:
	filename, ext = os.path.splitext(wave)
	if filename!=".wav":
		with open("../test.fileids", "w") as w:
			w.write(filename)
		f=open("../test.transcription", "w")
		for i in range(47):
			f.write(filename+" ")
		f.write("("+filename+")")
		f.close()
		os.chdir("..")
		os.system("./decoder.sh "+ "./audio")
		os.chdir("./audio")
os.chdir("..")
