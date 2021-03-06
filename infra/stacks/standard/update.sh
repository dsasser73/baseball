#!/bin/bash

# Get options
tname="cloud.json"
tfile="$(cd "$(dirname "${tname}")"; pwd)/$(basename "${tname}")"
kname="builder"

# Determine if running on Windows (affects template file argument to aws cli)
platform=`uname`
if [[ ${platform} == *"MINGW"* ]]; then
  echo "Using Windows file path"
  tfile=`cygpath -w ${tfile} | sed -e 's/[\/]/\/\//g'`
else
  echo "Using Linux file path"
fi

# Create stack
aws cloudformation update-stack --stack-name BTR-standard --template-body "file://${tfile}" --parameters ParameterKey=KeyName,ParameterValue=${kname} --capabilities CAPABILITY_IAM
