# Modern_Speak_and_Spell

A repository for the Google Summer of Code 2018 for Beagleboard.org

### Introduction

This is besically a project to rebrain the original Speak and Spell by Texas Instruments, first introduced in 1978. The main improvement over its predecessor is the addition of Speech to Text functionalities in addition to Text to Speech. This project will be deployed on a PocketBeagle as a part of GSoC-2018.

### Brief Description:

* Accuracy Checker - Generates accuracy stats after decoding. Right now working on three types of data for generating statistics.

1. Continuous Input from microphone - Works better if you have a microphone with automatic gain control. After each rounds of recording, processing takes place while the recording is paused and then accuracy statistics are generated.
2. Sample audio files - Two types of processes take place here, firstly just the audio files themselves...just convert from .mp3 to .wav and process them...and secondly, combining the audio files speaking out the same transcription into bigger files with intervals of silence in between them.

For more information go to "./Speech_Processing/accuracy_check"
[Documentation](./Speech_Processing/accuracy_check/description.md)

* Game Launcher - Code for voice-launching the games. For more information go to "./Game/Game_launcher"
[Documentation](./Game/Game_launcher/launcher.md)

* Games - Code for the games themselves. There are four games made for this project.

1. Spell It!	[Documentation](./Game/Games/Spell_It!/instructions.md)
2. Hangman	[Documentation](./Game/Games/Hangman/instructions.md)
3. Encrypter	[Documentation](./Game/Games/Encrypter/instructions.md)
4. Crossword	[Documentation](./Game/Games/Crossword/instructions.md)

For more information go to "./Game/Games"

### Further Improvements to be done

* Building a centralized recording script which can be utilised in every games...and the game_launcher...thereby improving reusability.
* Generating scoreboard after completion of every game.
* Generating UI using pygame.
