# Game Launcher

This a voice launcher for the games to be made. According to the input provided by the user, the games are launched.

## Run
```
python3 run_launcher.py
```

## Documentation

### `run_launcher.py`

Script to initiate the game_launcher.

### `main.py`

Script to launch the games based on the audio input. Launches the previous game if **RESUME** is entered. We don't need to run this script..this is automatically called by run_launcher.py through the shell script.
 
## Commands

1. **START** or **GENERATE** Game_Name to start a new game.
2. **RESUME** to resume the previously run game.

**EXAMPLES**:

* To start Spell It!:
```
GENERATE SPELL
```
* To start Hangman:
```
GENERATE HANGMAN
```
* To start Encrypter:
```
GENERATE ENCRYPTER
```
* To start Crossword:
```
GENERATE CROSSWORD
```
* To resume the previous game:
```
RESUME
```
