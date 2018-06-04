import shutil
temp =open('temp.csv', 'w+')
with open('phonetic.csv', 'r') as r:
	for line in r:
		words=line[:len(line)-1].split(",")
		if len(words[0])>0:
			f=open((words[0]+".dic"), "r")
			lines=f.read().split("\n")
			f.close()
			for i in range(len(lines)):
				arr=lines[i].split(" ")
				string=""
				if len(arr[0])>0 and int(arr[len(arr)-1])>2:
					#dictionary.write(filename+"("+str(k)+")	"+ words[i]+"\n")
					#k=k+1
					for j in range(len(arr)-1):
						string=string+arr[j]
					if string not in words:
						words.append(string)
				
				elif words[0] in arr[:]:
					for j in range(len(arr)-1):
						string=string+arr[j]
					if string not in words:
						words.append(string)
			for j in range(len(words)):
				temp.write(words[j]+",")
			temp.write("\n")
temp.close()
shutil.move("temp.csv", "phonetic.csv")		
				
