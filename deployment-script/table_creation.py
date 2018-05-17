import os
import subprocess
import time
import datetime
import ConfigParser






configParser = ConfigParser.RawConfigParser()  
configFilePath = 'config_properties.properties'
configParser.read(configFilePath)  

ERROR_LOG = configParser.get('PARAMETERS', 'TB_ERROR_LOG')
BASE_FOLDER = configParser.get('PARAMETERS', 'BASE_FOLDER')

pg_folder = os.path.join(BASE_FOLDER, 'test-db')

PGHOST = configParser.get('PARAMETERS', 'PGHOST')
PGPORT = configParser.get('PARAMETERS', 'PGPORT')
PGDATABASE = configParser.get('PARAMETERS', 'PGDATABASE')
PGUSER = configParser.get('PARAMETERS', 'PGUSER')
PGPASSWORD = configParser.get('PARAMETERS', 'PGPASSWORD')
PSQL = configParser.get('PARAMETERS', 'PSQL')


def create_schema(schemaFlag, password):
    configParser = ConfigParser.RawConfigParser()  
    configFilePath = 'config_properties.properties'
    configParser.read(configFilePath)  

    ERROR_LOG = configParser.get('PARAMETERS', 'TB_ERROR_LOG')
    BASE_FOLDER = configParser.get('PARAMETERS', 'BASE_FOLDER')

    pg_folder = os.path.join(BASE_FOLDER, 'test-db')

    
    PGHOST = configParser.get('PARAMETERS', 'PGHOST')
    PGPORT = configParser.get('PARAMETERS', 'PGPORT')
    PGDATABASE = configParser.get('PARAMETERS', 'PGDATABASE')
    PGUSER = configParser.get('PARAMETERS', 'PGUSER')
    PGPASSWORD = configParser.get('PARAMETERS', 'PGPASSWORD')
    PSQL = configParser.get('PARAMETERS', 'PSQL')
    schemas_list = configParser.get('PARAMETERS', 'schemas_list').split(',')
    schema_objects = ['Tables']
  

    queries_list = []
    num_queries = 0
    list_of_errored_sqls = list()
    
    os.environ['PGPASSWORD'] = password

    if schemaFlag == 'A':
        pass
    else:
        schemas_list = []
        print 'Invalid schema input'
        return

    if schemaFlag == 'A' :
        print schemas_list, schema_objects
        for schema in schemas_list:
            schema_path = os.path.join(pg_folder, schema)

            for objects in schema_objects:
                objects_path = os.path.join(schema_path , objects)
                #print os.walk(objects_path)
                for root, dirs, files in os.walk(objects_path, topdown=True):
                    for name in files:
                        sql_file = os.path.join(root, name)
                        if os.path.exists(sql_file):
                            filename, fileextension = os.path.splitext(sql_file)
                            print sql_file
                            if fileextension == '.sql':
                                spaces_adjusted_file = "{}".format(r'"%s"' % sql_file)
                                command = "{} -d {} -U {} -h {} -p {} -f {} >> {} 2>&1 ".format(PSQL, PGDATABASE,
                                                                                                PGUSER, PGHOST,
                                                                                                PGPORT,
                                                                                                spaces_adjusted_file,
                                                                                                ERROR_LOG)
                                print command
                                proc = subprocess.Popen(command,shell=True)
                                proc.communicate()
                                print proc.returncode

        sqlres = "select schema_name from information_schema.schemata where schema_name not in ('pg_catalog','information_schema','public','vestek')  order by schema_name "
        
        command = "{} -d {} -U {} -h {} -p {} -c {} ".format(PSQL, PGDATABASE, PGUSER, PGHOST, PGPORT,
                                                             r'"%s"' % sqlres.strip())
        

        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        records = proc.communicate()[0]
        
        schemas = records.split("\n")[2:-3]

        for record in schemas:
            schema_path = os.path.join(pg_folder, record.strip())

            
            for objects in schema_objects:
                objects_path = os.path.join(schema_path , objects)
                
                for root, dirs, files in os.walk(objects_path, topdown=True):
                  
                    for name in files:
                        sql_file = os.path.join(root, name)
                        
                        if os.path.exists(sql_file):
                           
                            filename, fileextension = os.path.splitext(sql_file)
                            if fileextension == '.sql':
                                
                                spaces_adjusted_file = "{}".format(r'"%s"' % sql_file)
                                
                                command = "{} -d {} -U {} -h {} -p {} -f {} >> {} 2>&1 ".format(PSQL, PGDATABASE,
                                                                                                PGUSER, PGHOST, PGPORT,
                                                                                                spaces_adjusted_file,
                                                                                                ERROR_LOG)
                                print "File execution command = " + command
                                proc = subprocess.Popen(command, shell=True)
                                output = proc.communicate()
                                print proc.returncode


if __name__ == "__main__":

    PGHOST = configParser.get('PARAMETERS', 'PGHOST')
    PGPORT = configParser.get('PARAMETERS', 'PGPORT')
    PGDATABASE = configParser.get('PARAMETERS', 'PGDATABASE')
    PGUSER = configParser.get('PARAMETERS', 'PGUSER')
    PGPASSWORD = configParser.get('PARAMETERS', 'PGPASSWORD')
   
    
    
    print "Enter A - For ALL"
    
    print "Enter Q -  To Quit"
    flag = raw_input("Enter Your Choice:")
    if flag == 'Q':
        exit(0)
    if flag == 'R':
        errored_sqlfiles = list()
        os.environ['PGPASSWORD'] = PGPASSWORD
        with open(ERROR_LOG, "r") as logfile:
            all_lines = logfile.readlines()
        for line in all_lines:
            if "ERROR" in line and 'already exists' not in line:
                sql_file = line.split(':')[1]
                if '.sql' in sql_file:
                    errored_sqlfiles.append(sql_file)

        list_of_sqlfiles = sorted(set(errored_sqlfiles),key=errored_sqlfiles.index)

        for sql_file in list_of_sqlfiles:
            if os.path.exists(sql_file):
                spaces_adjusted_file = "{}".format(r'"%s"' % sql_file)
                command = "{} -d {} -U {} -h {} -p {} -f {} ".format(PSQL, PGDATABASE, PGUSER, PGHOST,
                                                                 PGPORT, spaces_adjusted_file)
                print command
                proc = subprocess.Popen(command, shell=True)
                proc.communicate()
                print proc.returncode


        for part_sql in re_rerun_list:
            sql_file = os.path.join(pg_folder, part_sql)
            if sql_file in list_of_sqlfiles:
                if os.path.exists(sql_file):
                    spaces_adjusted_file = "{}".format(r'"%s"' % sql_file)
                    command = "{} -d {} -U {} -h {} -p {} -f {} ".format(PSQL, PGDATABASE, PGUSER, PGHOST,
                                                                     PGPORT, spaces_adjusted_file)
                    print command
                    proc = subprocess.Popen(command, shell=True)
                    proc.communicate()
                    print proc.returncode


    string_f = "started at {}".format(datetime.datetime.now())
    with open(ERROR_LOG,'a') as logfile:
        logfile.write(string_f)
    create_schema(flag.upper(),PGPASSWORD)
    string_f = "ended at {}".format(datetime.datetime.now())
    with open(ERROR_LOG,'a') as logfile:
        logfile.write(string_f)