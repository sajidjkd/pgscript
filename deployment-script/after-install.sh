python /home/ec2-user/pgscript/deployment-script/database_creation.py
sleep 1m
python /home/ec2-user/pgscript/deployment-script/object_creation.py
sleep 2m
python /home/ec2-user/pgscript/deployment-script/table_creation.py



echo "after deploy" > after-install-script.txt
