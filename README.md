# Modern_Speak_and_Spell

A repository for the Google Summer of Code 2018 for Beagleboard.org

[Link for documentation](https://anirbanbanik1998.github.io/Modern_Speak_and_Spell/)

### Introduction

This is besically a project to rebrain the original Speak and Spell by Texas Instruments, first introduced in 1978. The main improvement over its predecessor is the addition of Speech to Text functionalities in addition to Text to Speech. This project will be deployed on a PocketBeagle as a part of GSoC-2018.

### Brief Description:

* Accuracy Checker - Generates accuracy stats after decoding. Right now working on three types of data for generating statistics.

1. Continuous Input from microphone - Works better if you have a microphone with automatic gain control. After each rounds of recording, processing takes place while the recording is paused and then accuracy statistics are generated.
2. Sample audio files - Two types of processes take place here, firstly just the audio files themselves...just convert from .mp3 to .wav and process them...and secondly, combining the audio files speaking out the same transcription into bigger files with intervals of silence in between them.

For more information go to "./Speech_Processing/accuracy_check"
[Documentation](./Speech_Processing/accuracy_check/README.md)

* Game Launcher - Code for voice-launching the games. For more information go to "./Game/Game_launcher"
[Documentation](./Game/Game_launcher/README.md)

* Games - Code for the games themselves. There are four games made for this project.

1. Spell It!	
2. Hangman	
3. Encrypter	
4. Crossword	
For more information go to "./Game/Games"

* An Updated Speech Processing API to help in easier recording and decoding...so that the games can be made more easily.


### Installation Procedure

Edit /root/.bashrc file to include the following lines:
```
export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
export PYTHONPATH=/usr/local/lib/python2.7/site-packages/
```
Clone various repositories needed to /root/ folder:
```
 git clone https://github.com/cmusphinx/sphinxbase.git
 git clone https://github.com/cmusphinx/pocketsphinx.git
 git clone https://github.com/AnirbanBanik1998/Modern_Speak_and_Spell.git
```
Install bison:
```
sudo apt-get install bison
```
In /root/sphinxbase Directory:
```
./autogen.sh
make
make install
```
In /root/pocketsphinx Directory:
```
./autogen.sh
make
make install
```

#### Dependencies

To install all the dependencies for the project, go to the main project directory and run:
```
bash setup.sh
```

### Further Improvements to be done

* Making the enire project run on the pocketbeagle with proper GUI functioning.

