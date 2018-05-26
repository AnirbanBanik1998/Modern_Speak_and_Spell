output="$(perl word_align.pl test.transcription "$1")"
python3 stat.py "$output"
