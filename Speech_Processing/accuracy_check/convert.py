import os
arr=os.listdir()
for a in arr:
	if os.path.isdir(a):
		os.chdir(a)
		arr1=os.listdir()
		for files in arr1:
			filename, extension=os.path.splitext(files)
			if extension == ".mp3":
				os.system("ffmpeg -i "+files+" "+filename+".wav")
				os.remove(files)
		os.chdir("..")
		
