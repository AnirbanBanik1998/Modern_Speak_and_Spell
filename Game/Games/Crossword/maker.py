import sys

sys.path.insert(0, "../../../")
import sys
import os
import time
import subprocess
import threading
from API import recorder, edit

lock = threading.Lock()
start = round(time.time())


def meaning(w):
    with open("words.csv", "r") as r:
        for line in r:
            word = line[:len(line) - 1].split(",")
            if word[0] == w:
                return word[1:]
        return


mean = []
for i in range(1, 5):
    mean.append(meaning(sys.argv[i]))


def check(str1, l, w):
    print(" Input is " + l)
    for j in range(4):
        if l == w[j] and string[j] == "-":
            str1 = str1 + l
        else:
            str1 = str1 + string[j]
    return str1


def formation(w, q):
    print("Meaning of the word is " + mean[q])
    k = 0
    str1 = ""
    global string
    string = ""
    if "-" not in w[:]:
        for i in range(0, len(w)):
            string = string + "-"
        for i in range(0, len(string)):
            str1 = str1 + string[i] + " "
    else:
        string = w
        str1 = w
    print(str1)
    str1 = ""
    while k < 15:
        k = k + 1
        str1 = ""
        letter = ""
        print("Enter letter: ")
        with lock:
            record = recorder.Recorder("../../../Language_Models/", "../../../Acoustic_Models/", L_LIB="characters",
                                       A_LIB="en-us", DECODE=True, TRIALS=1,
                                       SILENCE=1)
            record.start()
        r = open('./test.hyp', 'r')
        arr = r.read().split(" ")
        letter = arr[0]
        print(letter)
        lt = letter.lower()
        r.close()
        try:
            string = str(check(str1, lt, w))

        except Exception as e:
            print(e)

        str1 = ""
        for j in range(0, len(string)):
            str1 = str1 + string[j] + " "
        print(str1)
        if string == q or k == 15:
            return string
        elif int(round(time.time()) - start) >= 180:
            subprocess.call(["espeak", "You lose"])
            break
    return "End"


output = ["" for j in range(4)]
matrix = [["" for x in range(4)] for y in range(4)]


def display():
    text = ""
    if output[0] != "":
        for t in range(4):
            matrix[int(sys.argv[5])][t] = output[0][t]
    if output[1] != "":
        for t in range(4):
            matrix[t][int(sys.argv[6])] = output[1][t]
    if output[2] != "":
        for t in range(4):
            matrix[t][int(sys.argv[6]) + 2] = output[2][t]
    if output[3] != "":
        for t in range(4):
            matrix[int(sys.argv[5]) + 2][t] = output[3][t]
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == "":
                text = text + "-" + " "
            else:
                text = text + matrix[i][j] + " "
        print(text)
        text = ""


n = 0
s = 0
m = 0
z = 1
while z:
    if len(output[n % 4]) == 0 and output[n % 4] != "End":
        output[n % 4] = formation(sys.argv[(n % 4) + 1], n % 4)
        m = m + 1
        print(m)
    elif output[n % 4] != sys.argv[(n % 4) + 1] and output[n % 4] != "End":
        output[n % 4] = formation(output[n % 4], n % 4)

    elif output[n % 4] == sys.argv[(n % 4) + 1] and output[n % 4] != "End":
        s = s + 1
        if s >= 4:
            subprocess.call(["espeak", "You win"])
        z = 0
    if output[n % 4] == "End":
        z = 0
    else:
        display()
    n = n + 1

subprocess.call(["espeak", "-s", "125", " Options are 1: Resume and 2: Start another game"])
