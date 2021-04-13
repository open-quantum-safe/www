#!/usr/bin/env bash

set -e

rm -rf _site/benchmarking/visualization_tmp
mkdir -p _site/benchmarking/visualization_tmp
cd _site/benchmarking/visualization_tmp
/usr/local/bin/aws s3 cp s3://oqs-tests/site/site-combined.tgz .
if [ $? -eq 0 ]; then
   # The tarball only contains the last 10 days of data: No further processing required
   tar zxf site-combined.tgz
   cd ..
   rm -rf visualization && mv visualization_tmp visualization
   cd ../..
   echo "New data successfully deployed"
else
   cd ../../..
fi

