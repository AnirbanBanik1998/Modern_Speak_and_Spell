import random
import os

f = open("./words.csv", "r")
lines = f.read().split("\n")

row = random.randint(0, 1)
column = random.randint(0, 1)
word1 = ""
word2 = ""
word3 = ""
word4 = ""


def find(w, c, r):
    '''
	This function helps to find if there is an intersection between the c'th letter of a word and the r'th letter of another word given in the file.
	
	:param w: The word provided.
	:param c: The index of the letter of the required word.
	:param r: The index of the letter of the given word.
	
	:return: The word whose letter matches with the letter of the given word.
	'''
    for i in range(0, len(lines)):
        g = lines[i].split(",")
        if w[r] == g[0][c]:
            return g[0]
    return ""


def find_inv(x, y, p):
    '''
	This function helps to find out a word, whose two letters at two specified positions are x and y.
	
	:param x: The letter at the beginning position.
	:param y: The letter at the beginning position.
	
	:return: The word found out from the list.
	'''
    for i in range(0, len(lines)):
        g = lines[i].split(",")
        if g[0][p] == x and g[0][p + 2] == y:
            return g[0]
    return ""


def main():
    '''
	Uses the functions to generate 4 4-letter words for a 4 X 4 crossword.
	'''
    k = 1
    while k:
        wordlist = []
        my_randoms = random.randint(0, len(lines) - 1)
        g = lines[my_randoms].split(",")
        word1 = g[0]
        wordlist.append(word1)
        try:
            word2 = find(word1, row, column)
            wordlist.append(word2)
            word3 = find(word1, row, (column + 2))
            wordlist.append(word3)
        except:
            word2 = ""
            word3 = ""
        if word2 == "" or word3 == "":
            k = 1
        else:
            try:
                word4 = find_inv(word2[row + 2], word3[row + 2], column)
                wordlist.append(word4)
                if len(wordlist) != len(set(wordlist)):
                    k = 1
                else:
                    k = 0
            except:
                word4 = ""
                k = 1
    '''
	print("Row "+str(row+1)+" " + word1)
	print("Row "+str(row+3)+" " + word4)
	print("Column "+str(column+1)+" " + word2)
	print("Column "+str(column+3)+" " + word3)
	'''
    os.system(
        "python3 maker1.py " + word1 + " " + word2 + " " + word3 + " " + word4 + " " + str(row) + " " + str(column))


if __name__ == "__main__":
    main()
