if [ -d wav ]
then
	echo "Directory wav already present"
else
	mkdir wav
fi
echo "Enter Sampling Rate:"
read samples
echo "Enter Chunk Size:"
read chunk
echo "Enter Minimum Volume:"
read vol

echo "Press CTRL+C to interrupt the recording"
python3 record_new.py $samples $chunk $vol
output= "$(ls wav | wc -l)"
python3 edit.py $output

echo "Enter Language Model:"
read lang
echo "Enter Dictionary:"
read dic

pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm $lang -dict $dic -samprate $samples -nfft $chunk -hyp test.hyp
 
python3 word_align.py test.transcription test.hyp
