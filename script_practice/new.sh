#!/bin/bash
#



echo "Statuus of the system"


set -x

set -e #exit the script when there is an error but does not exit if there is an error in pipeline (only checks last command is correct)

set -o pipefail #pipefail for error

free

df -h

nproc


ps -ef | grep amazon | awk -F" " '{print $2}'
