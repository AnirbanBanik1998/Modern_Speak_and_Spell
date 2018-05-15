if [ -e test.fileids ]
then
	echo "test.fileids already present..."
else
	touch test.fileids
fi

if [ -e test.transcription ]
then
	echo "test.transcription already present..."
else
	touch test.transcription
fi
python3 ../accuracy_check/edit.py 1

echo "Enter Language Model:"
read lang
echo "Enter Dictionary:"
read dic

pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm $lang -dict $dic -samprate $1 -nfft $2 -hyp test.hyp

python3 launcher.py
