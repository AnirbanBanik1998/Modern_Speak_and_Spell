if [ -e test.fileids ]
then
	echo "test.fileids already present..."
else
	touch test.fileids
fi

python3 ../../edit.py 1
pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm "../../../Language_Models/characters.lm" -dict "../../../Language_Models/characters.dic" -samprate $1 -nfft $2 -hyp test.hyp
