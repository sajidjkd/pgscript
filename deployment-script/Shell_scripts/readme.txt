This document is to used to execute the shell scripts for the execution of Primary_keys, Indexes, Foreign_keys and Check_constraints

Steps:

1- Modify the "pg_db_details.sh" as per the required connection details:

PGHOST="portfolio-qa-cluster.cluster-c6mxreiwpdjf.us-east-1.rds.amazonaws.com"
PGDATABASE="portfolio"
PGUSER="vestek"
PGPASSWORD="vestekqa"
PSQL="/Library/PostgreSQL/9.6/bin"
BASE_FOLDER='/Users/pranay/THOMSON_REUTERS/PAL-LE/Vestek/Constraints/'

Set the PATH and PGPASSWORD environment variables:

export PATH=$PATH:/Library/PostgreSQL/9.6/bin/
export PGPASSWORD=vestekqa


2- The order of execution is strictly in the following order:

(i)	    Create Primary_keys by executing create_individual_Primary_key.sh script file
	    sh create_individual_Primary_key.sh

(ii)	Create Indexes by executing create_individual_indexes.sh script file
	    sh create_individual_indexes.sh

(iii)	Create Check Constraints by executing create_individual_check_constraint.sh script file
	    sh create_individual_check_constraint.sh

(iv)	Create Foreign_keys by executing create_individual_foreign_keys.sh script file
	    sh create_individual_foreign_keys.sh

Each script file will capture execution log and is stored in the same folder location.


