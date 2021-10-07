
SOURCEPATH=/home/sujingyang/baks/backUpForReboot

for dir_item in $( ls    ${SOURCEPATH})
do
	RESULT=$(echo $dir_item | grep ".tar.gz")

	if [  -n "$RESULT"   ]
	then 
		
		tar -zxvf  ${SOURCEPATH}/${dir_item} 

	fi

done
