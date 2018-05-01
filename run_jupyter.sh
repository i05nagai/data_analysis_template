#!/bin/sh

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)
export PYTHONPATH=${PATH_TO_THIS_DIR}:${PYTHONPATH}
jupyter-notebook notebook
