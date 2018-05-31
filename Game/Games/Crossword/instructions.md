# Crossword

This is a game in which the user has to guess the words as in hangman...but with a twist...one word would lead to another.

## Documentation

### `Maker_files`
They are used to make the dictionary of the words along with their meanings.
To run the entire file-making script just type:
```
$./make.sh
```
This script will automatically determine if the __words.csv__ file is present or not and would act accordingly.
### `maker.py`
This script is used to find out the words from the .csv to make a 4*4 crossword with two rows and two columns to be filled by the user.
* `find(word, c, r)`: This function helps to find if there is an intersection between the c'th letter of a word and the r'th letter of another word given in the file.
* `find_inv(x, y, p)`: This function helps to find out a word, whose two letters at two specified positions are x and y.

## Development

This game is currently under development...the improvements will be updated soon.
