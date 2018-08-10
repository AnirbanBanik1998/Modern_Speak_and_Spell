import sys

sys.path.insert(0, "../../")
from API import recorder, edit
import threading

lock = threading.Lock()
with lock:
    record = recorder.Recorder("../../Language_Models/", "../../Acoustic_Models/", DECODE=True, TRANSCRIBE=True,
                               OUTPUT_SHELL="./lock.sh")
    record.start()
