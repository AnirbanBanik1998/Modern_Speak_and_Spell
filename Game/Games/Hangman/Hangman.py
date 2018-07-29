'''
Updated Version of Hangman Game
'''
import sys

sys.path.insert(0, "../../../")
import random
import subprocess
import time
import os
import threading
from API import recorder, edit


class Hangman:
    def __init__(self):
        self.lock = threading.Lock()
        self.f = open("../Wordlist.csv", 'r')
        self.rows = self.f.read().split("\n")
        self.f.close()
        self.k = 0
        self.string = ""
        self.str1 = ""
        self.counter = 0

    def rand(self):
        '''
		Generates a random word from Wordlist.csv
		'''
        self.my_randoms = random.sample(range(0, len(self.rows)), 1)
        self.column = self.rows[self.my_randoms[0]].split(",")
        self.randcolumn = random.sample(range(0, (len(self.column) - 1)), 1)
        self.column[self.randcolumn[0]] = self.column[self.randcolumn[0]].strip()
        return self.column[self.randcolumn[0]]

    def initialize(self, r):
        '''
		Displays the word in form of dashes.
		
		:param r: Random word generated.
		'''
        str1 = ""
        for i in range(0, len(r)):
            self.string = self.string + "-"
        for i in range(0, len(self.string)):
            str1 = str1 + self.string[i] + " "
        return (str1)

    def check(self, str1, l, r):
        '''
		Function to check if input letter is present anywhere in the word
		
		:param str1: To compute the updated string.
		:param l: The input letter.
		:param r: The word generated using rand().
		
		:return: The updated word after insertion of the input letter, if present in the actual word.
		'''
        print(" Input is " + l)
        for j in range(0, len(self.string)):
            if l == r[j] and self.string[j] == "-":
                str1 = str1 + l
            else:
                str1 = str1 + self.string[j]
        return str1

    def score(self, output, word):
        '''
		Finds out the user's score after comparing with the original word.
		
		:param output: The part of the word formed due to user input.
		:param word: The original word.
		
		:return: The user's score out of 10
		'''
        i = 0
        k = 0
        for j in word:
            if j == output[i]:
                k += 1
            i += 1
        score = (k / len(word)) * 10
        return score

    def terminal(self, word):
        '''
		Calls the other functions to run the entire terminal version of the game.
		
		:param word: The word which is generated randomly using function rand()
		'''
        self.str1 = self.initialize(word)
        print(self.str1)
        self.str1 = ""
        while self.counter < 20:
            self.counter = self.counter + 1
            self.str1 = ""
            letter = ""
            print("Enter letter: ")
            with self.lock:
                record = recorder.Recorder("../../../Language_Models/", LIB_FILE="characters", SILENCE=1, TRIALS=1,
                                           DECODE=True)
                record.start()
            r = open('./test.hyp', 'r')
            arr = r.read().split(" ")
            letter = arr[0]
            print(letter)
            lt = letter.lower()
            r.close()
            try:
                self.string = str(self.check(self.str1, lt, word))

            except Exception as e:
                print(e)

            self.str1 = ""
            for j in range(0, len(self.string)):
                self.str1 = self.str1 + self.string[j] + " "
            print(self.str1)
            if self.string == word:
                subprocess.call(["espeak", "You win"])
                break
            elif self.counter == 20:
                subprocess.call(["espeak", "You lose"])
                with self.lock:
                    subprocess.call(["espeak", "The answer is " + word])
                print(" Answer is: " + word)
