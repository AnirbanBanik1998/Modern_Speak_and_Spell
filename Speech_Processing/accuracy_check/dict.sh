unzip samples.zip
prev="./samples"
new="."
mv $prev/* $new
rm -r "./samples"

python3 dictionary.py
python3 translate.py

python3 final.py
python3 make.py

rm *.dic
rm *.hyp
