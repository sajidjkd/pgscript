#!/bin/bash

# PostgreSQL Database details and credentials
. ./pg_db_details.sh

rm -rf Index_error_log.log

ERROR_LOG=Index_error_log.log

myfolders[0]="Index"



now=$(date +"%T")
echo "Index creation STARTED : $now"
echo "Index creation STARTED : $now" >> $ERROR_LOG 2>&1


filecnt=1
allfiles[0]="test.sql"
nfilecnt=1
firsttime=0

for foldername in "${myfolders[@]}"; do
	echo $foldername
	myFileNames=$(ls $BASE_FOLDER/$foldername/)
	
	for filename in $myFileNames; do
		allfiles[$nfilecnt]=$BASE_FOLDER/$foldername/$filename
		#echo 'filename ====> ' $BASE_FOLDER/$foldername/Indexes/$filename
		echo $nfilecnt ${allfiles[$nfilecnt]}
		nfilecnt=`expr $nfilecnt + 1`		
	done		

	firsttime=`expr $firsttime + 1`		

	while [ 1 = 1 ];
	do
		no_of_psql_procs=`ps -ef|grep -v grep|grep psql|wc -l`
	
		echo $filecnt
	
		if [ $filecnt -gt ${#allfiles[@]} ];
		then
			break
		fi
	
		if [ $no_of_psql_procs -lt $NO_OF_CORES ];
		then
		
			echo '---------------->' $filecnt
			fullfilename=${allfiles[$filecnt]}
			echo 'Start Time : '`date`' , Executing individual SQL file : ' $fullfilename
			echo 'Start Time : '`date`' , Executing individual SQL file : ' $fullfilename >> $ERROR_LOG 2>&1
		
			psql -d $PGDATABASE -U $PGUSER  -h $PGHOST  -p $PGPORT -f $fullfilename >> $ERROR_LOG 2>&1 &
			echo 'Postgres Execution Status [ success(0)/failure(>0) ] : ' $?
			echo 'Postgres Execution Status [ success(0)/failure(>0) ] : ' $? >> $ERROR_LOG 2>&1
		
		
			filecnt=`expr $filecnt + 1`	
	
		else	
			sleep 30
		
		fi
	

	done
	
	echo 'now nfilecnt =========================>' $nfilecnt
	echo 'now firsttime ========================>' $firsttime

	if [ $firsttime -eq 0 ];
	then
		filecnt=1
	else
		filecnt=$nfilecnt
		echo '2     changed to nfilecnt =========================>' $nfilecnt
	fi
	
	echo 'now filecnt =========================>' $filecnt	
	
	sleep 10

done


now=$(date +"%T")
echo "Indexes creation END : $now"
echo "Indexes creation END : $now" >> $ERROR_LOG 2>&1



