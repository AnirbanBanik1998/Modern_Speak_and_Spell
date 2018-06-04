import shutil
f=open("new.dic","r")
lines=f.read().split("\n")
lines.sort()
w=open("temp.dic","w+")
for l in lines:
	w.write(l+"\n")
w.close()
f.close()
shutil.move("temp.dic", "new.dic")

