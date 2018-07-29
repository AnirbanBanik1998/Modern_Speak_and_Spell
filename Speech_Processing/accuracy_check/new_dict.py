f = open("../../Language_Models/characters.dic", "r")
g = open("./phonetic.csv", "r")
w = open("./new.dic", "w+")
ar = f.read().split("\n")
arr = g.read().split("\n")
for line in arr:
    hyp = line.split(",")
    i = 0
    try:
        while ar[i].startswith(hyp[0]):
            w.write(ar[i] + "\n")
            i = i + 1
    except Exception as e:
        print(e)
    for h in hyp[:len(hyp) - 1]:
        if len(h) > 1:
            w.write(hyp[0] + "(" + str(i + 2) + ")" + "	" + h + "\n")
            i = i + 1
f.close()
g.close()
w.close()
