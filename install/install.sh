#!/bin/bash

# Install the required packages

echo "Installing packages..."
apt install -y -q python3-pip

apt install -y -q smartmontools

pip3 install pysmart --quiet

pip3 install tk --quiet

echo "installing program files..."

# Clone the Git repository
git clone https://github.com/miguel-amf/ComputerInfo.git

echo "Moving files to system folders..."

# Move the cloned repository to /usr/sbin
cp -r ComputerInfo /usr/sbin

#move the keyboard test website shortcut to the desktop
cp KEYTEST.desktop /home/mint/Desktop/

# Change ownership of the moved repository to root
chown -R root:root /usr/sbin/ComputerInfo

# move startup file to startup folder
cp -r pchelper.desktop /home/mint/.config/autostart/




# Optional: Clean up by removing the cloned repository directory
rm -rf ComputerInfo

echo "Installation completed."