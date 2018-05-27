pocketsphinx_batch -adcin yes -cepdir $3 -cepext .wav -ctl test.fileids -lm 5887.lm -dict new.dic -samprate 22050 -nfft 1024 -hyp $1

python3 append.py $2 $1
