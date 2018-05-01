#!/bin/bash

################################################################################
# Usage:
#  bash runner.sh python runner/data/sample.py
################################################################################

path_to_this_dir=$(cd $(dirname ${0});pwd)
path_to_repository=$(cd ${path_to_this_dir}/..;pwd)
export PYTHONPATH="${path_to_repository}:${PYTHONPATH}"

exec "$@"
