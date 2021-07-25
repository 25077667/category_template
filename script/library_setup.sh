#!/bin/bash

echo "This is an automatic tool to install dependent tool chains"
echo "Enjoy it :)"

# Check root permission
if [ "$EUID" -ne 0 ]; then
    echo "Please use this tool in \'root\' user!"
    exit
fi

packages=(pdfgrep git python3 python3-pip)
install_operator="install"

# Specify package manager
if [ -x "$(command -v apk)" ]; then
    package_manager="apk"
elif [ -x "$(command -v apt-get)" ]; then
    package_manager="apt-get"
elif [ -x "$(command -v dnf)" ]; then
    package_manager="dnf"
elif [ -x "$(command -v zypper)" ]; then
    package_manager="zypper"
else echo "FAILED TO INSTALL PACKAGE: Package manager not found. You must manually install."; fi

# apk add operator
if [ -x "$(command -v apk)" ]; then install_operator="add"; fi

# Update package list
bash -c "${package_manager[@]} update -y"

echo "installing... "
echo "$package_manager $install_operator ${packages[@]} -y"
bash -c "$package_manager $install_operator ${packages[@]} -y"
