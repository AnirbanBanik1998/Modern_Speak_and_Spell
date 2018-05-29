python3 dictionary.py
python3 translate.py

python3 final.py
if [ -e	phonetic.csv ]
then
	python3 add.py
else 
	python3 make.py
fi

rm *.dic
rm *.hyp
