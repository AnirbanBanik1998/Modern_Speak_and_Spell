#!/bin/sh
# This script is mainly to install and update all the dependencies for this project.

# Install espeak
sudo apt-get install espeak

# Install Sphinxtrain
sudo apt-get update
sudo apt-get install sphinxtrain

# Upgrading to pip3
pip3 install --upgrade pip

# Installing pyaudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip3 install pyaudio

# Installing Wave
sudo pip3 install Wave

# Installing pocketsphinx
sudo apt-get install swig
pip3 install --upgrade setuptools wheel
sudo apt-get install libpulse-dev
pip3 install --upgrade pocketsphinx

