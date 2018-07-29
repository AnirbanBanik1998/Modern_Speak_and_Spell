#!/usr/bin/env bash
if [ -e ../words.csv ]
then
	echo "File already present"
else
	touch ../words.csv
	python3 list.py
	python3 meaning.py
	rm ../*.txt
fi
