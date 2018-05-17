import os
import subprocess
import time
import datetime
import ConfigParser


configParser = ConfigParser.RawConfigParser()
configFilePath = 'config_properties.properties'
configParser.read(configFilePath)
ERROR_LOG = configParser.get('PARAMETERS','PKG_ERROR_LOG')
BASE_FOLDER = configParser.get('PARAMETERS','BASE_FOLDER2')

sql_folder = os.path.join(BASE_FOLDER, 'sql')



def run_sql(sql_name, user, password):
    configParser = ConfigParser.RawConfigParser()
    configFilePath = 'config_properties.properties'
    configParser.read(configFilePath)
    PSQL = configParser.get('PARAMETERS','PSQL')

    sql_file = os.path.join(sql_folder, sql_name)
    
    os.environ['PGPASSWORD'] = password
   
    if os.path.exists(sql_file):
        
        spaces_adjusted_file = "{}".format(r'"%s"' % sql_file)
        command = "{} -d {} -U {} -h {} -p {} -f {} >> {} 2>&1 ".format(PSQL, PGDATABASE, user, PGHOST,
                                                                        PGPORT, spaces_adjusted_file,
                                                                        ERROR_LOG)

        print command
        proc = subprocess.Popen(command, shell=True)
        proc.communicate()
        print proc.returncode



if __name__ == "__main__":

    PGHOST = configParser.get('PARAMETERS','PGHOST')
    PGPORT = configParser.get('PARAMETERS','PGPORT')
    PGDATABASE = configParser.get('PARAMETERS','PGDATABASE_EXT') # SPECIFY THE NAME OF ANY EXISITING DATABASE WITH "vestek" ROLE LOGIN
    #PGSUPERUSER= configParser.get('PARAMETERS','PGSUPERUSER')
    PGUSER = configParser.get('PARAMETERS','PGUSER')
    PGPASSWORD = configParser.get('PARAMETERS','PGPASSWORD')
    #PGSUPASSWORD= configParser.get('PARAMETERS','PGSUPASSWORD')
    PSQL = configParser.get('PARAMETERS','PSQL')

    
    
    create_database_sql_file = 'create_database.sql'


    create_extension_sql_file ='create_schema.sql'
    
    string_f = "started at {}".format(datetime.datetime.now())
    with open(ERROR_LOG,'a') as logfile:
    	logfile.write(string_f)
    
    run_sql(create_database_sql_file, PGUSER, PGPASSWORD)
  
    PGDATABASE = configParser.get('PARAMETERS','PGDATABASE')# SPECIFY THE NEW DATABASE NAME TO BE CREATED IN .SQL FILE AS WELL
    

    run_sql(create_extension_sql_file, PGUSER, PGPASSWORD)
    
    string_f = "ended at {}".format(datetime.datetime.now())
    with open(ERROR_LOG,'a') as logfile:
    	logfile.write(string_f)

