# Crossword

This is a game in which the user has to guess the words as in hangman...but with a twist...one word would lead to another.
To run the entire game type:
```
python3 Crossword.py
```
## Documentation

### `Maker_files`
They are used to make the dictionary of the words along with their meanings.
To run the entire file-making script just type:
```
$./make.sh
```
This script will automatically determine if the __words.csv__ file is present or not and would act accordingly.

### `Crossword.py`
This script is used to find out the words from the .csv to make a 4*4 crossword with two rows and two columns to be filled by the user.
* `find(word, c, r)`: This function helps to find if there is an intersection between the c'th letter of a word and the r'th letter of another word given in the file.
* `find_inv(x, y, p)`: This function helps to find out a word, whose two letters at two specified positions are x and y.

### `maker.py`
This is the main script...takes the four generated words and the row and column values as arguments from __maker.py__ and runs the game.
* `meaning(w)`: Extracts the meaning out of the line containing the word.
* `check(str1,l)`: Checks if the input letter matches with any letter of the word or not.
* `formation(w,q)`: Here the q argument is mainly aimed at specifying the word number such that the meaning of it can be displayed as a hint. The main task of this function is to run a sequence like the Hangman game to complete each of the four words. If the number of trials exceed 20 for each word...it shifts to the next word...and again back to it if time permits...in order to strive towards the solution. However, if the time of game-running exceeds 2 minutes...the game stops.
* `display()`: This function displays the crossword matrix at each stage of the game.

### `input.sh`
This shell script starts the record_once.py script.

### `decode.sh`
This shell script runs the pocketsphinx_batch to decode the recorded file.

### `record_once.py`
A recording script.

## Development

This game is currently under development...the improvements will be updated soon.
