#!/bin/bash
# get the path of the main module and the tests
my_path=`dirname "$0"`
main_path=${my_path}/ala_operator
tests_path=${my_path}/tests

# add the name of the main module to the path (otherwise import in tests will not work)
export PYTHONPATH="$PYTHONPATH:${main_path}"


echo -e "\n########## Running unit tests ############"
for testf in ${tests_path}/test*.py
do
    echo "#### Running tests from $testf ####"
    python $testf
done
echo -e "########### Done with unit tests ############\n\n"


echo -e "########### Running system tests #############"
python ${tests_path}/system_test.py ${main_path}
echo -e "########### Done with system tests ############\n"
