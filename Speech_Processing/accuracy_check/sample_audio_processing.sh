z="$1.zip"
unzip $z
prev="./$1"
new="."
mv $prev/* $new
rm -rf $prev

python3 convert.py
python3 dictionary.py
python3 translate.py
python3 final.py

if ! [ -e phonetic.csv ]
then
	python3 make.py
else
	echo "phonetic csv file present"
fi
python3 add.py
python3 modify.py
rm generate.py
rm voices.json
rm a.txt
rm *.dic
rm *.hyp
rm -r */
