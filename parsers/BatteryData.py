#get battery data
from os import path
from math import floor

def _get_battery_max_percentage():
    chargeDesign = 1000
    chargeCurrent = -1
    cycles = 0

    batteries = []

    #path normally follows the format of /sys/class/power_supply/BAT*/, se we got to check for every BAT* possible
    initialPathStr = '/sys/class/power_supply/BAT'

    batIterator = 0

    while(True) :
        if path.exists('/sys/class/power_supply/BAT' + str(batIterator) + '/'):
            #check for design and different naming types
            if path.exists('/sys/class/power_supply/BAT' + str(batIterator) + '/charge_full_design') :
                with open('/sys/class/power_supply/BAT' + str(batIterator) + '/charge_full_design') as f:
                    chargeDesign = int(f.read().strip())
            elif path.exists('/sys/class/power_supply/BAT0/energy_full_design'):
                with open('/sys/class/power_supply/BAT0/energy_full_design') as f:
                    chargeDesign = int(f.read().strip())

            if path.exists('/sys/class/power_supply/BAT' + str(batIterator) + '/charge_full') :
                with open('/sys/class/power_supply/BAT' + str(batIterator) + '/charge_full') as f:
                    chargeCurrent = int(f.read().strip())

            elif path.exists('/sys/class/power_supply/BAT' + str(batIterator) + '/energy_full'):
                with open('/sys/class/power_supply/BAT' + str(batIterator) + '/energy_full') as f:
                    chargeCurrent = int(f.read().strip())
            batteries.append([batIterator,(chargeCurrent/chargeDesign)*100])
            batIterator += 1
        else:
            break
    return batteries



def getBatteryData():
    returnStr = ''
    batCount = 1
    for bat in _get_battery_max_percentage():
        returnStr += "Battery " + str(batCount) + ":\t" + str(floor(bat[1])) + "%\n"
        batCount += 1
    return returnStr