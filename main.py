import platform
import psutil
import subprocess
import math
from pySMART import *
import subprocess
import os
import io

from parsers.ProcessorData import getProcessorData
from parsers.RamData import getRamData
from parsers.BatteryData import getBatteryData

import tkinter as tk
from tkinter import *


##########################
#    HELPER FUNCTIONS    #
##########################

def get_internal_disks():
    return DeviceList()
    internal_disks = []
    disks = DeviceList()
    for disk in disks:
        if not disk.is_external:
            internal_disks.append(disk)
    return internal_disks

def keyboardTestClick(): 
    subprocess.run(['sudo','-u', 'mint', 'xdg-open', 'https://www.key-test.ru'])


def getGpu():
    try:
        output = subprocess.check_output(['lshw', '-C', 'display'])
        output = output.decode('utf-8')
        lines = output.split('\n')
        gpuNames = []
        for line in lines: 
            if 'product' in line.lower():
                name = line.split(':')[1].strip()
                gpuNames.append(name)
        return gpuNames if gpuNames else None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

##########################
#    PRINT SECTION       #
##########################

#set variables for output
file_path = '/home/mint/Desktop/output.txt'
output_file = open(file_path, 'w')
window = tk.Tk()
strout = ""

#PRINT THE PROCESSOR SPECS
strout += getProcessorData()

#PRINT RAM
strout += getRamData()

#PRINT BATTERY
strout += getBatteryData()


#PRINT DISKS
internal_disks = get_internal_disks()
i = 1
for disk in internal_disks:
    disk_type = "Unknown Type"
    if(disk.is_ssd) :
        disk_type = 'SSD'   
    else :
        disk_type = 'HDD'    
    #print("DISK", i,":\t",disk_type,math.ceil(disk.size/1024**3), "GB|BAD SECTORS:", disk.attributes[5].raw, file = output_file)
    strout += "DISK" + str(i) + ":\t\t" + str(disk_type) + " " + str(math.floor(disk.size/1000**3)) + " GB | BAD SECTORS: " +smart_health_assement(disk.name) +'\n'
    i += 1

#SERIAL NUMBER
serialNumber = 'NO SERIAL'
with open('/sys/class/dmi/id/product_serial') as f:
    serialNumber = f.read().strip()

print("SN:\t\t\t", serialNumber, file = output_file)
strout += "SN:\t\t" + str(serialNumber) + '\n'

#PRODUCT NAME
productName = 'NO PRODUCT NAME'
with open('/sys/class/dmi/id/product_name') as f:
    productName = f.read().strip()

print("Product:\t", productName, file = output_file)

strout += "Product:\t\t" + str(productName) + '\n' 

#Graphical adapters
gpuNames = getGpu()
strout += "GPU:\t\t"
if gpuNames is not None:
    for gpu in gpuNames:
        strout += gpu + ' | '
    strout += '\n'
else:
    strout += 'no GPU Found' + '\n'



label = tk.Label(window, text=strout, anchor="w", justify=LEFT)
label.pack(anchor='w', side= TOP)




############################
#WRAP UP AND OUTPUT SECTION#
############################
output_file.close()

#subprocess.run(['sudo','-u', 'mint', 'xdg-open', file_path])

button = tk.Button(window, text="GO TO KEYBOARD TEST", command=keyboardTestClick)
button.pack()

window.mainloop()

