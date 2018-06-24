python3 final.py
if ! [ -e test.hyp ]
then
	if [ -e phonetic.csv ]
	then 
		python3 add.py
	else
		python3 make.py
		python3 add.py
	fi
else
	echo "Test hypothesis file is present"
fi
rm -rf ./wav/*
rm *.dic
