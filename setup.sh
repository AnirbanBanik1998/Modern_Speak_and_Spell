#!/bin/sh
# This script is mainly to install and update all the dependencies for this project.

# Install espeak
sudo apt-get install espeak

# Install Sphinxtrain
sudo apt-get update
sudo apt-get install sphinxtrain

# Installing pyaudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip install pyaudio

# Installing Wave
sudo pip install Wave

# Installing pocketsphinx
sudo apt-get install swig
sudo pip install --upgrade pip setuptools wheel
sudo apt-get install libpulse-dev
sudo pip install --upgrade pocketsphinx || sudo pip --no-cache-dir install --upgrade pocketsphinx

# Installing pygame
sudo pip install pygame

# Installing PyDictionary
sudo pip install PyDictionary
