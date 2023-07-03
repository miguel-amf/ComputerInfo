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

	#check for bad sectors by searching for an
	#attribute with the Reallocated Keyword.
	#manufacturers sometimes use the id 5 or 196 for
	#reallocation count but since naming and id varies
	#it is best to just go for this linear search.

	#set error value to -1 so if it doesnt change it means
	#that smart was not present
	badsectors = -1
	for disk in internal_disks:
		print(disk.diagnostics)
		for attr in disk.attributes:
			
			#check if attribute has realocated in it
			if attr != None and 'Reallocated' in attr.name:
				#get the raw value of bad sectors
				badsectors = attr.raw 
				break
		#set default value
		disk_type = "Unknown Type"

		#check if disk is ssd
		if(disk.is_ssd) :
			disk_type = 'SSD'   
		else :
			disk_type = 'HDD'

		#forming the output string    
		returnString += "DISK" + str(i) + ":\t\t" + \
						str(disk_type) + " " + str(floor(disk.size/1000**3)) + " GB | "
		if (badsectors == -1) :
			returnString += "BAD SECTORS: ?? (\"" + disk.assessment + "\" REPORTED)\n"
		else:
			returnString +=	"BAD SECTORS: " + str(badsectors) +'\n'
		i += 1
	return returnString