from parsers.ProcessorData import getProcessorData
from parsers.RamData import getRamData
from parsers.BatteryData import getBatteryData
from parsers.DisksData import getDisksData
from parsers.ProductData import getProductData
from parsers.VideoAdaptersData import getVideoAdaptersData

import tkinter as tk
from tkinter import *


##########################
#    HELPER FUNCTIONS    #
##########################

def keyboardTestClick(): 
    subprocess.run(['sudo','-u', 'mint', 'xdg-open', 'https://www.key-test.ru'])
##########################
#    PRINT SECTION       #
##########################

#set variables for output

strout = ""

#PRINT THE PROCESSOR SPECS
strout += getProcessorData()

#PRINT RAM
strout += getRamData()

#PRINT BATTERY
strout += getBatteryData()

#PRINT DISKS
strout += getDisksData()

#PRINT PRODUCTS INFO

strout += getProductData()

#Graphical adapters
strout += getVideoAdaptersData()


#graphical stuff
window = tk.Tk()
label = tk.Label(window, text=strout, anchor="w", justify=LEFT)
label.pack(anchor='w', side= TOP)




############################
#WRAP UP AND OUTPUT SECTION#
############################

button = tk.Button(window, text="GO TO KEYBOARD TEST", command=keyboardTestClick)
button.pack()

window.mainloop()

