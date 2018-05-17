#!/bin/bash

PGHOST="localhost"
PGPORT="5432"
PGDATABASE="testdb"
PGUSER="testdb"
PGPASSWORD="testdb"
NO_OF_CORES=2
PSQL="/usr/local/bin/psql"

export PGPASSWORD=testdb

BASE_FOLDER='/Users/durgach/github/DP/test-db/testschema/Constraints/'
echo 'Postgres code basefolder=' $BASE_FOLDER