from parsers.ProcessorData import getProcessorData
from parsers.RamData import getRamData
from parsers.BatteryData import getBatteryData
from parsers.DisksData import getDisksData
from parsers.ProductData import getProductData
from parsers.VideoAdaptersData import getVideoAdaptersData

from GUI import MainWindow

import utils.FormatDrives

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

print(utils.FormatDrives.listDisks())


#set graphical elements
gui = MainWindow()
gui.setInfoSection(strout)
gui.setKeytestButton()
gui.setFormatDisks()
gui.run()





