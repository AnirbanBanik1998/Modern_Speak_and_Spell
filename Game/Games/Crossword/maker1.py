import sys

sys.path.insert(0, "../../../")
import sys
import os
import time
import subprocess
import threading
from API import recorder, edit
import pygame


class Crossword:
    def __init__(self):
        self.lock = threading.Lock()
        self.start = round(time.time())
        self.m = ""
        self.n = ""
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.gameDisplay = pygame.display.set_mode((800, 600))  # Pass a tuple as a parameter
        self.display_width = 800
        self.display_height = 600
        self.output = ["" for j in range(4)]
        self.mat = ["" for j in range(4)]
        self.matrix = [["" for x in range(4)] for y in range(4)]
        self.mean = []
        self.dummy = ""
        self.assign_meaning()

    def message(self, msg, color, width, height, font_size, center=False):
        '''
		Function to display a specific message in a specific position with a specific color.
	
		:param msg: The text to be displayed.
		:param color: The font color.
		:param width: The horizontal position of the text on the screen.
		:param height: The vertical position of the text on the screen.
		:param font_size: The font size of the text.
		:param center: Boolean value to determine if text will be aligned to the center or not.
		'''
        font = pygame.font.SysFont(None, font_size)
        screen_text = font.render(msg, True, color)
        if center == True:
            text_rect = screen_text.get_rect(center=(width, height))
            self.gameDisplay.blit(screen_text, text_rect)
        else:
            self.gameDisplay.blit(screen_text, [width, height])

    def multi_line_text(self, surface, text, pos, font_size, color):
        '''
		Used to display multi_line text.
		
		:param surface: The game display surface or window.
		:param text: The single(or multi-line)text to be displayed.
		:param pos: The width and height positions of the text, to be entered in tuple format.
		:param font_size: The display font_size of the text.
		:param color: The color of the text to be displayed on screen.
		'''
        words = [word.split(' ') for word in text.splitlines()]
        font = pygame.font.SysFont(None, font_size)
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def meaning(self, w):
        '''
		Extracts the meaning out of the line containing the word.
		
		:param w: The word for which meaning has to be found out.
		
		:return: The meaning of the word concerned.
		'''
        with open("words.csv", "r") as r:
            for line in r:
                word = line[:len(line) - 1].split(",")
                if word[0] == w:
                    return word[1:]
            return

    def assign_meaning(self):
        '''
		Appends the meanings to a list.	
		'''
        for i in range(1, 5):
            self.mean.append(self.meaning(sys.argv[i]))

    def check(self, str1, l, w):
        '''
		Checks if letter is present in word or not.
		
		:param str1: Variable to return the updated string.
		:param l: The letter itself...as user-input.
		:param w: The string to be checked.
		
		:return: The updated string.
		'''
        print(" Input is " + l)
        for j in range(4):
            if l == w[j] and string[j] == "-":
                str1 = str1 + l
            else:
                str1 = str1 + string[j]
        return str1

    def formation(self, w, q):
        '''
		Main function, which just like in hangman, forms the string taking the user-input at every time.
		
		Here the q argument is mainly aimed at specifying the word number such that the meaning of it can be displayed as a hint. The main task of this function is to run a sequence like the Hangman game to complete each of the four words. If the number of trials exceed 15 for each word...it shifts to the next word...and again back to it if time permits...in order to strive towards the solution. However, if the time of game-running exceeds 3 minutes...the game stops.
		
		:param w: The qth word generated from Crossword script.
		:param q: The index of the word.
		
		:return: The updated string if within game-running time, or else returns "END".
		'''
        string1 = ""
        mean_string = "Meaning of the word is :"
        f = pygame.font.SysFont(None, 25)
        word_surf = f.render(mean_string, True, self.green)
        word_wid, word_hei = word_surf.get_size()
        self.multi_line_text(self.gameDisplay, mean_string, (0, self.display_height / 10), 25, self.green)
        pygame.display.update()
        self.multi_line_text(self.gameDisplay, self.n, (word_wid, self.display_height / 8), 25, self.black)
        pygame.display.update()
        for meaning in self.mean[q]:
            print(meaning)
            string1 = string1 + meaning + "\n"
        self.multi_line_text(self.gameDisplay, string1, (word_wid, self.display_height / 8), 25, self.white)
        pygame.display.update()
        self.n = string1

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
        self.message(self.m, self.black, self.display_width / 2, self.display_height / 3, 30, True)
        pygame.display.update()
        self.message("Output: " + str1, self.white, self.display_width / 2, self.display_height / 3, 30, True)
        pygame.display.update()
        self.m = "Output: " + str1
        str1 = ""
        subprocess.call(["espeak", "Guess the word"])
        while k < 15:
            k = k + 1
            str1 = ""
            letter = ""
            print("Enter letter: ")
            subprocess.call(["espeak", "Trials left " + str(16 - k)])
            with self.lock:
                record = recorder.Recorder("../../../Language_Models/", LIB_FILE="characters", DECODE=True, TRIALS=1,
                                           SILENCE=1)
                record.start()
            r = open('./test.hyp', 'r')
            arr = r.read().split(" ")
            letter = arr[0]
            print(letter)
            lt = letter.lower()
            r.close()
            try:
                string = str(self.check(str1, lt, w))

            except Exception as e:
                print(e)

            str1 = ""
            for j in range(0, len(string)):
                str1 = str1 + string[j] + " "
            self.message(self.m, self.black, self.display_width / 2, self.display_height / 3, 30, True)
            pygame.display.update()
            self.message("Output: " + str1, self.white, self.display_width / 2, self.display_height / 3, 30, True)
            pygame.display.update()
            self.m = "Output: " + str1
            if string == q or k == 15:
                return string
            elif int(round(time.time()) - self.start) >= 180:
                subprocess.call(["espeak", "Time is up You lose"])
                break
        return "End"

    def display(self, color):
        '''
		This function displays the crossword matrix at each stage of the game, on the pygame window.
		
		:param color: The color to be displayed.
		'''
        self.message(self.dummy, self.black, self.display_width / 2, 5 * self.display_height / 6, 40, True)
        pygame.display.update()
        text = "|"
        addition = 0
        x = self.display_width / 2
        y = self.display_height / 2

        if self.output[0] != "":
            for t in range(4):
                self.matrix[int(sys.argv[5])][t] = self.output[0][t]
        if self.output[1] != "":
            for t in range(4):
                self.matrix[t][int(sys.argv[6])] = self.output[1][t]
        if self.output[2] != "":
            for t in range(4):
                self.matrix[t][int(sys.argv[6]) + 2] = self.output[2][t]
        if self.output[3] != "":
            for t in range(4):
                self.matrix[int(sys.argv[5]) + 2][t] = self.output[3][t]
        for i in range(4):
            self.message(self.mat[i], self.black, x, y, 30, True)
            pygame.display.update()
            for j in range(4):
                if self.matrix[i][j] == "":
                    text = text + "#" + "| "
                else:
                    text = text + self.matrix[i][j] + "| "
                    addition += 1
            self.mat[i] = text
            self.message(text, color, x, y, 30, True)
            pygame.display.update()
            y = y + 40
            text = ""
        self.message("Score: " + str(addition * 10 / 16), self.green, self.display_width / 2,
                     5 * self.display_height / 6, 40, True)
        pygame.display.update()
        self.dummy = "Score: " + str(addition * 10 / 16)


def main():
    '''
	Main function to launch the pygame GUI, and use the other functions to build the game sequence.
	'''
    pygame.init()
    c = Crossword()
    pygame.display.set_caption("Crossword")
    pygame.display.update()  # Update the specific modification
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:
        c.message("Crossword", c.blue, c.display_width / 20, c.display_height / 20, 50)
        pygame.display.update()
        n = 0
        s = 0
        m = 0
        z = 1
        while z:
            if len(c.output[n % 4]) == 0 and c.output[n % 4] != "End":
                c.output[n % 4] = c.formation(sys.argv[(n % 4) + 1], n % 4)
                m = m + 1
                print(m)
            elif c.output[n % 4] != sys.argv[(n % 4) + 1] and c.output[n % 4] != "End":
                c.output[n % 4] = c.formation(c.output[n % 4], n % 4)

            elif c.output[n % 4] == sys.argv[(n % 4) + 1] and c.output[n % 4] != "End":
                s = s + 1
                if s >= 4:
                    subprocess.call(["espeak", "You win"])
                    gameExit = True
                z = 0
            if c.output[n % 4] == "End":
                gameExit = True
                z = 0
                # After game ends...display all the the original words in the crossword.
                for p in range(4):
                    c.output[p] = sys.argv[p + 1]
                c.display(c.red)
            else:
                c.display(c.white)
            n = n + 1
        clock.tick(20)
    subprocess.call(["espeak", "-s", "125", " Options are 1: Resume and 2: Start another game"])
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
