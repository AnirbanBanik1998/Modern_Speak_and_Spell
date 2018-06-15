from API import recorder, edit

record=recorder.Recorder("../../Language_Models/", LIB_FILE="commands", DECODE=True, OUTPUT_SHELL="./launch.sh")
record.start()
