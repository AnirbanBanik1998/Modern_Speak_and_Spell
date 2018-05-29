if [ -e test.fileids ]
then
	echo "test.fileids already present..."
else
	touch test.fileids
fi

python3 ../../edit.py 1
pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm ../9731.lm -dict ../9731.dic -samprate $1 -nfft $2 -hyp test.hyp
python3 file.py
