import sys

f = open(sys.argv[1] + ".dic", "a+")
g = open(sys.argv[2], "r")
hyp = g.read().split(" ")
for i in range(len(hyp) - 2):
    f.write(hyp[i].upper() + " ")
f.write("\n")
g.close()
f.close()
