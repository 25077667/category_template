#!/bin/bash

# Apply hooks
cp scripts/pre-commit.hook .git/hooks/pre-commit
cp scripts/commit-msg.hook .git/hooks/commit-msg

py_pkg=(pre-commit)
# Check pre-commit has installed
if [ ! -x "$(command -v pre-commit --version)" ]; then
    sudo scripts/library_setup.sh
    exit 1
fi

# Librarian dependency
py_pkg=(pre-commit) # overwrite the pkg list
pip3 install ${py_pkg[@]} -y
