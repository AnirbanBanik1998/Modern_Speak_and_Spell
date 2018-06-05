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
python3 edit.py 1

echo "Enter Language Model:"
read lang
echo "Enter Dictionary:"
read dic

pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm $lang -dict $dic -samprate $1 -nfft $2 -hyp test.hyp
output="$(perl word_align.pl test.transcription test.hyp)"
python3 stat.py "$output"
python3 rename.py
if ! [ -e test.hyp ]
then
	if [ -e phonetic.csv ]
	then 
		python3 add.py
	else
		python3 make.py
	fi
else
	echo "Test hypothesis file is present"
fi
rm -rf ./wav/*
rm *.dic
