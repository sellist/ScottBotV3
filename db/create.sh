#!/bin/bash
export PGPASSWORD=''
export DB_NAME='scottbot'
export DB_USER=''
export DB_PASS=''
export TOKEN=''

BASEDIR=$(dirname "$0")
DATABASE=$DB_NAME
psql -U "$DB_USER" -f "$BASEDIR/dropdb.sql" &&
createdb -U "$DB_USER" $DATABASE &&
psql -U "$DB_USER" -d $DATABASE -f "$BASEDIR/schema.sql" &&
psql -U "$DB_USER" -d $DATABASE -f "$BASEDIR/data.sql"