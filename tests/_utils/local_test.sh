export DJANGO_HOME=`pwd`

export PYTHONPATH=$DJANGO_HOME:$DJANGO_HOME/tests:$DJANGO_HOME/tests/singlestore_settings:$PYTHONPATH

# export NOT_ENFORCED_UNIQUE=1

export TABLE_STORAGE_TYPE_ADMIN="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_AUTH="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_CONTENTTYPES="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_SITES="ROWSTORE REFERENCE"


export TABLE_STORAGE_TYPE_SERIALIZERS="ROWSTORE"
export TABLE_STORAGE_TYPE_ADMIN_INLINES="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_AUTH_TESTS="REFERENCE"
export TABLE_STORAGE_TYPE_INTROSPECTION="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_VALIDATION="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_CONSTRAINTS="ROWSTORE REFERENCE"
export TABLE_STORAGE_TYPE_BULK_CREATE="ROWSTORE REFERENCE"

# 12 many-to-many fields
export TABLE_STORAGE_TYPE_PREFETCH_RELATED="ROWSTORE REFERENCE"

# abstract models - specifying through is tricky 
export TABLE_STORAGE_TYPE_MANY_TO_MANY="ROWSTORE REFERENCE"



prepare_settings() {
    for dir in $(find tests -maxdepth 1 -type d | awk -F '/' '{print $2}'); do
        # echo $dir
        sed -e "s|TEST_MODULE|$dir|g" tests/singlestore_settings_TMPL > tests/singlestore_settings/singlestore_settings_$dir.py
    done
}

# prepare_settings


run_all_tests() {
    for dir in $(find tests -maxdepth 1 -type d | awk -F '/' '{print $2}'); do
        echo $dir
        ./tests/runtests.py --settings=singlestore_settings_$dir --noinput -v 3 $dir >> django_test_result_$dir.txt 2>&1
    done
}
# python run_tests_parallel.py
# run_all_tests

./tests/runtests.py --settings=singlestore_settings --noinput -v 3 queries --keepdb
