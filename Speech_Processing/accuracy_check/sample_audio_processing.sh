unzip samples.zip
prev="./samples"
new="."
mv $prev/* $new
rm -rf "./samples"

python3 convert.py
python3 dictionary.py
python3 translate.py
python3 final.py

if [ -e	phonetic.csv ]
then
	python3 add.py
else 
	python3 make.py
	python3 add.py
fi

rm generate.py
rm voices.json
rm a.txt
rm *.dic
rm *.hyp
rm -r */
