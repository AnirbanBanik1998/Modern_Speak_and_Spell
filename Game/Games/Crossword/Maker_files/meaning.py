from PyDictionary import PyDictionary
import shutil
temp = open("../temp.csv", "w+")
dictionary=PyDictionary()
with open("../words.txt", "r") as r:
	for line in r:
		temp.write(line[:len(line)-1]+",")
		try:
			d=dictionary.meaning(line)
			for key, value in d.items():
				temp.write(key+":")
				for i in range(len(value)):
					words=value[i].split(" ")
					if line not in words:
						temp.write(value[i]+",")
						break
				break
		except Exception as e:
			print(e)
		temp.write("\n")
temp.close()
shutil.move("../temp.csv", "../words.csv")
