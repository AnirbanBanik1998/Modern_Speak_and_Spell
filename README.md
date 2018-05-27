# Modern_Speak_and_Spell

A repository for the Google Summer of Code 2018 for Beagleboard.org

## Introduction

This is besically a project to rebrain the original Speak and Spell by Texas Instruments, first introduced in 1978. The main improvement over its predecessor is the addition of Speech to Text functionalities in addition to Text to Speech. This project will be deployed on a PocketBeagle as a part of GSoC-2018.

### Games

* Spell It!
* Hangman
* Encrypter
* Crossword

### Requirements

* Python3
* PyAudio
```
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip3 install pyaudio
```
* PocketSphinx
```
pip3 install --upgrade pip setuptools wheel
pip3 install --upgrade pocketsphinx
```
* Wave

### Description

The project consists of:

* Accuracy Checker - Generates accuracy stats after decoding. For more information go to "./Speech_Processing/accuracy_check"
* Game Launcher - Code for voice-launching the games. For more information go to "./Game/Game_launcher"
* Games - Code for the games themselves. For more information go to "./Game/Games"

### Further Improvements to be done

* Generate accuracy staistics after each operation...be it running the games..or voice-launching...or just testing.
* Updating the dictionary automatically from time to time based on the stats generated.
