#!/bin/bash

# Install the required packages
apt install -y python3-pip

apt install -y smartmontools

pip3 install pysmart

pip3 install tk

# Clone the Git repository
git clone https://github.com/miguel-amf/ComputerInfo.git

# Move the cloned repository to /usr/sbin
cp -rv ComputerInfo /usr/sbin

# Change ownership of the moved repository to root
chown -R root:root /usr/sbin/ComputerInfo

# move startup file to startup folder

cp -rv pchelper.desktop /etc/xdg/autostart

# enable the startup file

#sudo systemctl enable /etc/systemd/system/pchelper.service

# run the service

#sudo systemctl start pchelper

# Optional: Clean up by removing the cloned repository directory
rm -rf ComputerInfo

echo "Installation completed."