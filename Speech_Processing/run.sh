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
val= "$(sox --i './wav/test1.wav')"
python3 stat.py "$val"
echo "Press CTRL+C to interrupt the recording"
python3 record_lock.py $samples $chunk $vol

