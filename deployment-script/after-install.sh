
cd /home/ec2-user/pgscript/deployment-script
python database_creation.py
sleep 1m
python object_creation.py
sleep 1m
python table_creation.py



echo "after deploy" > after-install-script.txt
