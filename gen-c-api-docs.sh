#!/bin/bash

set -e

www_dir=$(pwd)
liboqs_dir="$(pwd)/_includes/liboqs"
echo "Using www_dir=${www_dir}"
echo "Using liboqs_dir=${liboqs_dir}"
cd $liboqs_dir

if [[ -d $liboqs_dir/build/docs ]]; then
    echo "Found existing $liboqs_dir/build/docs"
    read -p "Press enter to delete or ctrl+c to exit: "
    rm -rf $liboqs_dir/build/docs
    mkdir -p $liboqs_dir/build/docs
fi

$liboqs_dir/scripts/run_doxygen.sh $(which doxygen) $liboqs_dir/docs/.Doxyfile $liboqs_dir/build

if [[ -d $www_dir/liboqs/api/doxygen ]]; then
    echo "Found existing $www_dir/liboqs/api/doxygen"
    read -p "Press enter to delete or ctrl+c to exit: "
    rm -rf $www_dir/liboqs/api/doxygen
fi
cp -r $liboqs_dir/build/docs/html $www_dir/liboqs/api/doxygen
