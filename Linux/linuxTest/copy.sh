COPYPATH=/homes/backUpForReboot
SOURCEPATH=/homes
#backUpForReboot

for dir_item in $(ls ${SOURCEPATH})
do
	if [ -d ${SOURCEPATH}/${dir_item} ] && [ ${SOURCEPATH}/${dir_item} != ${COPYPATH}  ]
	then 
	   
	   tar -zcvf ${COPYPATH}/${dir_item}.tar.gz ${SOURCEPATH}/${dir_item}   
	   #echo ${SOURCEPATH}/${dir_item}    
	fi

done
