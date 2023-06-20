# ComputerInfo

This python script creates a pop up with computer information. The main purpose is to debbug and catalog a great volume of computers and fit a specific Businness Inteligence format. 
It was intended to be used with a live usb linux installation, specially Linux Mint. It will not work on Windows and most likely wont work with macOS either.
It requires root permissions due to pySMART. As far as i can tell by the time i'm writing this (first readme, gimme a break), it requires "pip3 install pySMART". Since pySMART requires smartctl, you will also need
to install smartmontools, so you will have to run "apt install smartmontools".

After processing, the script presents a window containing information for user decision making. There are also extra buttons on the window to run additional scripts for some common next steps.
