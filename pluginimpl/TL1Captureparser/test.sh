for i in `cat ciena-6500-otm.txt | grep -e RTRV-PM-OTM -e ".*\"" | sed -e 's/^[ ]*\"//g' | sed 's/"//g'`
do
	a=$(echo $i | grep -c "^OTM.*")
	if [ $a = 1 ]
	then
		echo $i >>"results/"$filename".txt"
	else
		filename=$(echo $i | awk -F ':' '{print$1,"-",$3}' |sed 's/ //g' )
		echo $filename
	fi
	
done
	
		
	
