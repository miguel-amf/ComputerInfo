#GET RAM DATA
import subprocess
from math import ceil
from psutil import virtual_memory

#get the technology of the RAM
def _get_ram_ddr_technology():
    try:
        output = subprocess.check_output("dmidecode -t memory", shell=True).decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            if "DDR" in line:
                return line.strip().split()[-1]
    except subprocess.CalledProcessError:
        pass

    return "Unknown"

def getRamData():
	#determine the DDR version
	ramTech = _get_ram_ddr_technology()
	return "RAM: \t\t" + ramTech + " " + str(ceil(virtual_memory().total/(1024 ** 3))) + " GB\n"