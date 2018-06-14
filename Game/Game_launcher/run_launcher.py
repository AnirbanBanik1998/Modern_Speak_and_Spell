from API import recorder, edit
import os

record=recorder.Recorder("../../Language_Models/", DECODE=True, OUTPUT_SHELL="./launch.sh")
record.start()
