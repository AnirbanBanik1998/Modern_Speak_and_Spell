f=open("../../Wordlist.csv", "r")
g=open("../statistics.txt", "w+")
w=open("../words.txt", "w+")
rows=f.read().split("\n")
words = []
for i in range(0, len(rows)):
	columns=rows[i].split(",")
	for j in range(0, len(columns)):
		if len(columns[j])==4:
			w.write(columns[j]+"\n")
			words.append(columns[j])
for i in range(0, len(words)):
	g.write(words[i]+"\n")
	for m in range(4):
		for n in range(4):
			g.write(str(m)+" "+str(n)+" "+"-> ")
			for j in range(0, len(words)):
				if words[i][m]==words[j][n] and i!=j:
					g.write(words[j]+",")
			g.write("\n")
	g.write("\n")
f.close()
g.close()
w.close()
