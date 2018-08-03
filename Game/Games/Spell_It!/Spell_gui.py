import pygame
import Spell_It
import subprocess


def message(msg, color, width, height, font_size, center=False, bg=None):
    '''
	Function to display a specific message in a specific position with a specific color.
	
	:param msg: The text to be displayed.
	:param color: The font color.
	:param width: The horizontal position of the text on the screen.
	:param height: The vertical position of the text on the screen.
	:param font_size: The font size of the text.
	:param center: Boolean value to determine if text will be aligned to the center or not.
	:param bg: Sets the background colour of the text on the window. Default value is None.
	'''
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(msg, True, color)
    if center == True:
        text_rect = screen_text.get_rect(center=(width, height))
        gameDisplay.blit(screen_text, text_rect)
    else:
        gameDisplay.blit(screen_text, [width, height])


def main():
    '''
	The main block of the program which runs the entire display.
	'''
    global m
    m = ""
    spell = Spell_It.Spell()
    pygame.init()  # Initialize pygame
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    global gameDisplay
    gameDisplay = pygame.display.set_mode((800, 600))  # Pass a tuple as a parameter
    display_width = 800
    display_height = 600
    pygame.display.set_caption("Spell_It!")
    pygame.display.update()  # Update the specific modification
    clock = pygame.time.Clock()
    gameExit = False
    while True:
        try:
            random_word = spell.rand()
            break
        except Exception as e:
            print(e)
    while not gameExit:
        message("Spell It...", red, display_width / 7, display_height / 7, 50)
        pygame.display.update()
        w = ""
        i = 0
        while i < len(random_word) and spell.counter < 20:

            subprocess.call(["espeak", str(20-spell.counter)+" trials left"])
            w1 = spell.test(w, random_word[i])
            message(m, black, display_width / 2, display_height / 2, 40, True, black)
            pygame.display.update()

            if w1 is not "-":
                w = w1
                message(w.upper(), white, display_width / 2, display_height / 2, 45, True)
                pygame.display.update()
                m = w.upper()
                i += 1
            else:
                message((w + w1).upper(), white, display_width / 2, display_height / 2, 45, True)
                pygame.display.update()
                m = (w + w1).upper()
            if w == random_word:
                subprocess.call(["espeak", "-s", "125", " Good!"])
                gameExit = True
                break
            if spell.counter > 20:
                subprocess.call(["espeak", "-s", "125", " No you are wrong...the answer will be "])
                message("You Lose...Answer is: " + random_word, red, display_width / 2, (3 * display_height) / 4, 45,
                        True)
                pygame.display.update()
                for j in random_word:
                    subprocess.call(["espeak", "-s", "100", j])
                gameExit = True
        message("Score out of 10: " + str(spell.score(w, random_word)), green, display_width / 2,
                (5 * display_height) / 6, 40, True)
        pygame.display.update()
        clock.tick(20)
    subprocess.call(["espeak", "-s", "125", " Options are 1: Resume and 2: Start another game"])
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
