# Encrypter

### Introduction

This is a game in which the user will be given three choices.
* Encode
* Decode
* Guess

In the first two games the user will be given to encode or decode some words based on a hint provided. In the third game, the user has to guess the actual word from the encrypted one using some shift operations.

### How to play

To run the GUI mode of the game:
```
python3 Encrypter_gui.py
```
To run the terminal mode of the game:
```
python3 Encrypter.py
```

### A note on the Ceasar Cipher

This is a very simple cipher used in encryptions in which the letters are shifted each by a specific value.

Let us for example shift **ANIRBAN** by 4:

So,
A -> E
N -> R
I -> M
R -> V
B -> F
A -> E
N -> R

So the final encrypted result is -> ERMVFER.
