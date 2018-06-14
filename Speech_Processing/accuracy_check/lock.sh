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
