import shutil

temp = open('temp.csv', 'w+')
with open('phonetic.csv', 'r') as r:
    for line in r:
        words = line[:len(line) - 1].split(",")
        words_trim = [words[i].strip() for i in range(len(words))]
        if len(words_trim[0]) > 0:
            try:
                f = open((words_trim[0] + ".dic"), "r")
                lines = f.read().split("\n")
                f.close()
                for i in range(len(lines)):
                    arr = lines[i].split(" ")
                    string = ""
                    if len(arr[0]) > 0 and int(arr[len(arr) - 1]) > 2:
                        # dictionary.write(filename+"("+str(k)+")	"+ words[i]+"\n")
                        # k=k+1
                        for j in range(len(arr) - 1):
                            string = string + arr[j] + " "
                        if string.strip() not in words_trim:
                            words_trim.append(string.strip())

                    elif words[0] in arr[:]:
                        for j in range(len(arr) - 1):
                            string = string + arr[j] + " "
                        if string.strip() not in words_trim:
                            words_trim.append(string.strip())
                for j in range(len(words_trim)):
                    temp.write(words_trim[j] + ",")
                temp.write("\n")
            except Exception as e:
                print(e)
temp.close()
shutil.move("temp.csv", "phonetic.csv")
