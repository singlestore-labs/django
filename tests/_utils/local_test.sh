export DJANGO_HOME=`pwd`

export PYTHONPATH=$DJANGO_HOME:$DJANGO_HOME/tests:$DJANGO_HOME/tests/singlestore_settings:$PYTHONPATH

# uncomment this to run tests without unique constraints on the data base level 
# export NOT_ENFORCED_UNIQUE=1

# these are default django apps, we use ROWSTORE REFERENCE tabkes for them
export  DJANGO_SINGLESTORE_TABLE_STORAGE_TYPE_ADMIN="ROWSTORE REFERENCE"
export  DJANGO_SINGLESTORE_TABLE_STORAGE_TYPE_AUTH="ROWSTORE REFERENCE"
export  DJANGO_SINGLESTORE_TABLE_STORAGE_TYPE_CONTENTTYPES="ROWSTORE REFERENCE"
export  DJANGO_SINGLESTORE_TABLE_STORAGE_TYPE_SITES="ROWSTORE REFERENCE"

# 12 many-to-many fields, just use reference tables to save time
export TABLE_STORAGE_TYPE_PREFETCH_RELATED="ROWSTORE REFERENCE"

# abstract models - specifying through is tricky 
export TABLE_STORAGE_TYPE_MANY_TO_MANY="ROWSTORE REFERENCE"

# specify the path to the test to run
MODULE_TO_TEST=serializers
./tests/runtests.py --settings=singlestore_settings --noinput -v 3 $MODULE_TO_TEST --keepdb
