'''
This is the improvised Spell_It game
'''
import sys

sys.path.insert(0, "../../../")
import random
import threading
import subprocess
import time
import os
from API import recorder, edit


class Spell:
    def __init__(self):
        self.lock = threading.Lock()
        self.f = open("../Wordlist.csv", 'r')
        self.rows = self.f.read().split("\n")
        self.f.close()
        self.k = 0
        self.j = 0
        print("Spell It!")

        self.counter = 0
        self.flag = 0
        self.string = ""
        self.str1 = ""
        self.answer = ""

    def rand(self):
        '''
		Generates a random word from Wordlist.csv
		'''
        self.my_randoms = random.sample(range(0, len(self.rows)), 1)
        self.column = self.rows[self.my_randoms[0]].split(",")
        self.randcolumn = random.sample(range(0, (len(self.column) - 1)), 1)
        self.column[self.randcolumn[0]] = self.column[self.randcolumn[0]].strip()
        subprocess.call(["espeak", "-s", "100", " Spell " + self.column[self.randcolumn[0]]])
        return self.column[self.randcolumn[0]]

    def test(self, string, w):
        '''
		Function to take the recording and check if it matches with the letters.
		
		:param string: The string to be formed as the result.
		:param w: The specific letter to be checked.
		
		:return: Returns string, improvised by the function itself.
		'''
        self.counter += 1
        with self.lock:
            record = recorder.Recorder("../../../Language_Models/", "../../../Acoustic_Models/", SILENCE=1, TRIALS=1,
                                       DECODE=True,
                                       L_LIB="characters", A_LIB="en-us", OUTPUT_SHELL="./decoder.sh")
            record.start()
        f = open("./file.txt", "r")
        letter = f.read().strip()
        if letter.lower() == w:
            string = string + w
            return string
        else:
            return "-"

    def score(self, output, word):
        '''
		Finds out the user's score after comparing with the original word.
		
		:param output: The part of the word formed due to user input.
		:param word: The original word.
		
		:return: The user's score out of 10
		'''
        score = (len(output) / len(word)) * 10
        return score

    def terminal(self, word):
        '''
		Main function to take care of the whole process
		
		:param word: Takes the randomly generated word from rand() as input parameter.
		'''
        w = ""
        i = 0
        while i < len(word) and self.counter <= 20:
            w1 = self.test(w, word[i])
            if w1 is not "-":
                w = w1
                print(w.upper())
                i += 1
            else:
                print((w + w1).upper())
            if w == word:
                subprocess.call(["espeak", "-s", "125", " Good!"])
                break
            if self.counter > 20:
                subprocess.call(["espeak", "-s", "125", " No you are wrong...the answer will be "])
                for j in word:
                    subprocess.call(["espeak", "-s", "100", j])
        print("Score: " + str(self.score(w, word)))
        subprocess.call(["espeak", "-s", "125", " Options are 1: Resume and 2: Start another game"])


# To run the terminal version of the game
def main():
    ob = Spell()
    random_word = ob.rand()
    ob.terminal(random_word)


if __name__ == "__main__":
    main()
