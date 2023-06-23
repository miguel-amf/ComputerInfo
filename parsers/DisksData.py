from pySMART import *
from math import floor

def get_internal_disks():
    return DeviceList()
    internal_disks = []
    disks = DeviceList()
    for disk in disks:
        if not disk.is_external:
            internal_disks.append(disk)
    return internal_disks


def getDisksData() :
	returnString = ""
	internal_disks = get_internal_disks()
	i = 1
	badsectors = -1
	for disk in internal_disks:
		for attr in disk.attributes:
			if attr != None and attr.name == 'Reallocated_Sector_Ct' :
				badsectors = attr.raw 
				break
		disk_type = "Unknown Type"
		if(disk.is_ssd) :
			disk_type = 'SSD'   
		else :
			disk_type = 'HDD'    
		returnString += "DISK" + str(i) + ":\t\t" + \
						str(disk_type) + " " + str(floor(disk.size/1000**3)) + \
						" GB | BAD SECTORS: " + str(badsectors) +'\n'
		i += 1
	return returnString