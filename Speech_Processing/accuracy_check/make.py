import os

dictionary = open("phonetic.csv", "w+")
d = os.listdir()
d.sort()
for di in d:
    p = 0
    if os.path.isfile(di):
        filename, ext = os.path.splitext(di)

        if len(filename) == 1 and ord(filename) in range(65, 91):
            p = 1
        if ext == ".dic" and p:
            f = open(di, "r")
            lines = f.read().split("\n")
            f.close()
            # k=1
            dictionary.write(filename + ",")
            for i in range(len(lines)):
                words = lines[i].split(" ")
                if len(words[0]) > 0 and int(words[len(words) - 1]) > 2:
                    # dictionary.write(filename+"("+str(k)+")	"+ words[i]+"\n")
                    # k=k+1
                    for j in range(len(words) - 1):
                        dictionary.write(words[j] + " ")
                    dictionary.write(",")
                elif filename in words[:]:
                    for j in range(len(words) - 1):
                        dictionary.write(words[j] + " ")
                    dictionary.write(",")
            dictionary.write("\n")
dictionary.close()
