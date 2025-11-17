#!/bin/bash

set -e

www_dir=$(pwd)
liboqs_dir="$(pwd)/_includes/liboqs"
echo "Using liboqs_dir=${liboqs_dir}"
cd $liboqs_dir

if [[ -d $liboqs_dir/build ]]; then
    rm -rf $liboqs_dir/build
    mkdir $liboqs_dir/build
fi

CWD=$liboqs_dir \
$liboqs_dir/scripts/run_doxygen.sh $(which doxygen) $liboqs_dir/docs/.Doxyfile $liboqs_dir/build

if [[ -d $www_dir/liboqs/api/doxygen ]]; then
    rm -rf $www_dir/liboqs/api/doxygen
fi
cp -r $liboqs_dir/build/docs/html $www_dir/liboqs/api/doxygen
