if [ -d wav ]
then
	echo "Directory wav already present"
	output="$(ls wav | wc -l)"
	if [ "${output}" -gt 0 ]
	then
		rm -rf ./wav/*
	else
		echo "wav directory already empty"
	fi
	
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
python3 record_lock.py $samples $chunk $vol

