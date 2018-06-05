unzip samples.zip
prev="./samples"
new="."
mv $prev/* $new
rm -rf "./samples"

python3 convert.py
mkdir audio
python3 merge.py
python3 decode.py
rm silence.wav
rm generate.py
rm voices.json
rm a.txt
rm *.dic
rm *.hyp
rm -r */
rm details.txt
