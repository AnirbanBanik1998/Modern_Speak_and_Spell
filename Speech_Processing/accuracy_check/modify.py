import shutil

temp = open("./temp.csv", "w+")
dic = {}
alpha = [chr(i) for i in range(65, 91)]
dictionary = {k: [] for k in alpha}
a = {'B', 'P', 'D', 'T', 'G', 'K', 'F', 'V', 'S', 'Z', 'L', 'R', 'Y', 'W', 'M', 'N'}
f = open("../../Language_Models/characters.dic", "r")
lines = f.read().split("\n")
for line in lines:
    b = line.split("	")
    if len(b[0]) > 0 and b[0][0] in alpha:
        try:
            dictionary[b[0][0]].append(b[1])
        except:
            print(b[0][0])
with open("./phonetic.csv", "r") as r:
    for line in r:
        string = ""
        words = line[:len(line) - 1].split(",")
        dic[words[0]] = [words[i] for i in range(1, len(words)) if len(words[i]) > 1]
        temp.write(words[0] + ",")
        for j in dic[words[0]]:
            p = j.split(" ")
            iterations = 1
            for l in p:
                if l not in a:
                    iterations = iterations * len(dictionary[l])
            array = ["" for i in range(iterations)]
            for l in p:
                if l in a:
                    for k in range(iterations):
                        array[k] = array[k] + " " + l
                else:
                    n = 0
                    for k in range(int(iterations / len(dictionary[l]))):
                        for q in dictionary.get(l):
                            array[n] = array[n] + " " + q
                            n += 1
            for l in array:
                temp.write(l.strip() + ",")
        temp.write("\n")

temp.close()
f.close()
shutil.move("temp.csv", "phonetic.csv")
