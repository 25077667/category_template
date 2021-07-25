#!/bin/bash

# Apply hooks
cp script/*.hook .git/hooks/
touch .git/hooks/applied

py_pkg=(pre-commit)
# Check pre-commit has installed
if [ ! -x "$(command -v pre-commit --version)" ]; then
    sudo script/library_setup.sh
    exit 1
fi

# Librarian dependency
py_pkg=(pre-commit) # overwrite the pkg list
pip3 install ${py_pkg[@]} -y
