#!/usr/bin/env bash

set -e

rm -rf _site/benchmarking/visualization
mkdir -p _site/benchmarking/visualization
cd _site/benchmarking/visualization
curl --silent -O https://oqs-tests.s3.us-east-2.amazonaws.com/site/site.tgz
tar zxf site.tgz
for f in *.list; do
    mv $f orig-$f
    tail orig-$f > $f
done
