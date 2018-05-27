if [ -d audio ]
then
	echo "Directory already present..."
else
	mkdir wav
fi
python3 merge.py
python3 decode.py
