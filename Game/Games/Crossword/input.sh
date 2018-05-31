if [ -d wav ]
then
	echo "Directory wav already present"
	output="$(ls wav | wc -l)"
	if [ "${output}" -gt 0 ]
	then
		rm -rf "./wav/"
		mkdir wav
	else
		echo "wav directory already empty"
	fi
	
else
	mkdir wav
fi
python3 record_once.py 16000 1024 1600

