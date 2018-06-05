pocketsphinx_batch -adcin yes -cepdir $1 -cepext .wav -ctl test.fileids -lm ../../Language_Models/characters.lm -dict ../../Language_Models/characters.dic -samprate 22050 -nfft 1024 -hyp test.hyp
output="$(perl word_align.pl test.transcription test.hyp)"
python3 stat.py "$output"
