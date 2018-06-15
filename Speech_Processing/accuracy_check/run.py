import sys
sys.path.insert(0, "../../")
from API import recorder, edit

record=recorder.Recorder("../../Language_Models/", DECODE=True, TRANSCRIBE=True, OUTPUT_SHELL="./lock.sh")
record.start()

