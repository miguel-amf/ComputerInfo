import psutil
from subprocess import check_output

def listDisks():
	disksNames = []
	output = check_output(['parted', '-l'])
	output = output.decode('utf-8')
	lines = output.split('\n')
	for line in lines:
		if 'Disk /' in line:
			device = line.split(':')
			disk = {'name': device[0].split(' ')[1], 'capacity': device[1].split('G')[0]}
			disksNames.append(disk)
	return disksNames