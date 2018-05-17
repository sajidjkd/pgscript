#!/bin/bash

PGHOST="testdb1.c2tskthlfglu.us-east-1.rds.amazonaws.com"
PGPORT="5432"
PGDATABASE="testdb"
PGUSER="root"
PGPASSWORD="root1234"
NO_OF_CORES=2
PSQL="/usr/local/bin/psql"

export PGPASSWORD=root1234

BASE_FOLDER='/home/ec2-user/pgscript/test-db/testschema/Constraints'
echo 'Postgres code basefolder=' $BASE_FOLDER
