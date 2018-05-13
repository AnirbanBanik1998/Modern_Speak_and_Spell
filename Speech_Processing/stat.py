import sys
f=open("./stat.txt", "a+")
f.write(sys.argv[1]+"\n\n")
f.close()

