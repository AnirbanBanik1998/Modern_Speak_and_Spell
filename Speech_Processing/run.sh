echo "Enter Sampling Rate:"
read samples
echo "Enter Chunk Size:"
read chunk
echo "Enter Minimum Volume:"
read vol
python3 record_new.py $samples $chunk $vol
output= "$(ls wav | wc -l)"
python3 edit.py $output

echo "Enter Language Model:"
read lang
echo "Enter Dictionary:"
read dic

pocketsphinx_batch -adcin yes -cepdir wav -cepext .wav -ctl test.fileids -lm $lang -dict $dic -samprate $samples -nfft $chunk -hyp test.hyp 
output="$(perl word_align.pl test.transcription test.hyp)"
python3 stat.py "$output"
