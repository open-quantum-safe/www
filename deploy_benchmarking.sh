#!/usr/bin/env bash

set -e

rm -rf _site/benchmarking/visualization_tmp
mkdir -p _site/benchmarking/visualization_tmp
cd _site/benchmarking/visualization_tmp
# curl --silent -O https://oqs-tests.s3.us-east-2.amazonaws.com/site/site.tgz
/usr/local/bin/aws s3 cp s3://oqs-tests/site/site-x86_64.tgz .
tar zxf site-x86_64.tgz
for f in *.list; do
    mv $f orig-$f
    tail orig-$f > $f
done
cd ..
rm -rf visualization && mv visualization_tmp visualization
