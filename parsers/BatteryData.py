#get battery data
from os import path
from math import floor

def _get_battery_max_percentage():
    chargeDesign = 100
    chargeCurrent = 0
    cycles = 0
    if path.exists('/sys/class/power_supply/BAT0/charge_full_design') :
        with open('/sys/class/power_supply/BAT0/charge_full_design') as f:
            chargeDesign = int(f.read().strip())
    if path.exists('/sys/class/power_supply/BAT0/charge_full_design') :
        with open('/sys/class/power_supply/BAT0/charge_full') as f:
            chargeCurrent = int(f.read().strip())
    if path.exists('/sys/class/power_supply/BAT0/cycle_count') :
        with open('/sys/class/power_supply/BAT0/cycle_count') as f:
            cycles = int(f.read().strip())
    
    return {'life' : (chargeCurrent/chargeDesign)*100,  'cycles': cycles}



def getBatteryData():
	if (path.exists("/sys/class/power_supply/BAT0/")) :
		bat_result = _get_battery_max_percentage()
		return "Battery:\t\t" + str(floor(bat_result['life'])) + "%|Cycles: " + str(bat_result['cycles']) + '\n'
	else:
		return "Battery:\t\tNo Battery Detected"