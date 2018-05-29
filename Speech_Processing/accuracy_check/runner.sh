pocketsphinx_batch -adcin yes -cepdir $3 -cepext .wav -ctl test.fileids -lm ../../Language_Models/characters.lm -dict ../../Language_Models/characters.dic -samprate 22050 -nfft 1024 -hyp $1

python3 append.py $2 $1
