python3 final.py
if ! [ -e test.hyp ]
then
	if ! [ -e phonetic.csv ]
	then 
		python3 make.py
	else
		echo "phonetic csv file present"
	fi
	python3 add.py
	python3 modify.py
else
	echo "Test hypothesis file is present"
fi
rm -rf ./wav/*
rm *.dic
