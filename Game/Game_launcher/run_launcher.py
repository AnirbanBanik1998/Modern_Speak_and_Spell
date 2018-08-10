import sys

sys.path.insert(0, "../../")
from API import recorder, edit

record = recorder.Recorder("../../Language_Models/", "../../Acoustic_Models/", L_LIB="commands", A_LIB="en-us", DECODE=True, OUTPUT_SHELL="./launch.sh")
record.start()
