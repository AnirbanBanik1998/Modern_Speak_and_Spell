
if [ -e test.fileids ]
then
	echo "test.fileids already present..."
else
	touch test.fileids
fi

python3 ../edit.py 1

echo "Enter Language Model:"
read lang
echo "Enter Dictionary:"
read dic

pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm $lang -dict $dic -samprate $1 -nfft $2 -hyp test.hyp

python3 launcher.py
chmod 777 ./wav/*
rm -rf ./wav/*

