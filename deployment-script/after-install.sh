
cd /home/ec2-user/pgscript/deployment-script
python database_creation.py
sleep 10s
python object_creation.py
sleep 10s
python table_creation.py


