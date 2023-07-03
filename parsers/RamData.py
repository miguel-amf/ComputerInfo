#GET RAM DATA
import subprocess
from math import ceil
from psutil import virtual_memory
import re

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

def get_memory_by_bank():
    output = subprocess.check_output(['dmidecode', '-t', 'memory'], universal_newlines=True)
    lines = output.split("\n\t")
    sizeBanks = []
    for line in lines:
        if line.startswith("Size: "):
            value = line.split()[-2]
            if value.isdigit():
                sizeBanks.append(value)
            else:
                sizeBanks.append("0")
    return sizeBanks


    return memory_banks

def getRamData():
	#determine the DDR version
    output = ""
    ramTech = _get_ram_ddr_technology()
    output += "RAM: \t\t" + ramTech + " " + str(ceil(virtual_memory().total/(1024 ** 3))) + " GB ("

    memory_banks = get_memory_by_bank()
    i = 1
    for mem in memory_banks:
        output += str(mem) + "GB/"
        i += 1
    #remove " | " padding from the end
    output = output[:-1]

    return output + ")\n"