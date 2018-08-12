# Spell It!

## Introduction

This is a very simple game...a game in which the user has to spell a word given out and based on whether the word is spelt correct or wrong the results are generated accordingly.

## How to Play

* Open a terminal and move to this directory.
* Run the entire game in GUI mode:
```
python3 Spell_gui.py
```
To run the game in terminal mode:
```
python3 Spell_It.py
```
* Now the entire process is automated...spell out the word given to you and the results will be generated.

## Documentation

### `Spell_It.py`

Main program...takes out words at random from the wordlist and asks to spell them out. It can be used to play the terminal version of the game.

* `Spell`: Main class containing all the core functionality of the game.
* `random()`: Generates a random word from Wordlist.csv.
* `test(string, w)`: Function to take the recording and check if it matches with the letters.
1. **string** -> The string to be formed as the result of the operations performed.
2. **w** -> The specific letter to be checked.
* `terminal(word)`: Main function to take care of the whole process, and generate the terminal version of the game, often calling the test() function to aid in the process.
1. **word** -> The randomly generated word from rand().

### `Spell_gui.py`

Generates GUI using pygame, for Spell It!, using core functionality from Spell_It.py script.

* `message(msg, color, width, height, font_size)`: Function to display a specific message in a specific position with a specific color. Is also used for overwriting the previously displayed messages.
1. **msg** -> The text to be displayed.
2. **color** -> The font color.
3. **width** -> The horizontal position of the text on the screen.
4. **height** -> The vertical position of the text on the screen.
5. **font_size** -> The font size of the text.
* `main`: The main block of code to generate the GUI using pygame.

### `decoder.sh`

Automating the running of file.py

### `file.py`

Operates on the hypothesis file.
