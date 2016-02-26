#!/bin/bash -e

THIS_SCRIPT=$0
THIS_DIR=$(dirname ${THIS_SCRIPT})

DIR_TO_CHECK=$1/utcdatetime

function check_that_directory_exists {
  test -d "${DIR_TO_CHECK}"
}

function run_most_pep8_checks_on_everything {
    # F401: imported but unused
    # F403: from foo import *

    flake8 --verbose \
        --ignore=F401,F403 \
    ${DIR_TO_CHECK}
}

function run_particular_pep8_checks_excluding_init_files {

    # F401: don't allow `imported but unused` except in __init__.py
    flake8 --verbose \
        --select=F401 \
        --exclude='*/__init__.py' \
    ${DIR_TO_CHECK}

    # F403: from xxx import *   - this is OK in __init__.py
    flake8 --verbose \
        --select=F403 \
        --exclude='*/__init__.py' \
    ${DIR_TO_CHECK}
}

check_that_directory_exists
run_most_pep8_checks_on_everything
run_particular_pep8_checks_excluding_init_files
