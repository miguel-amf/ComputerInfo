#MODULE FOR PROCESSOR DATA RETRIEVAL
import psutil

def _get_max_cpu_clock():
    max_clock = 0.0
    for cpu in psutil.cpu_freq(percpu=True):
        if cpu.max > max_clock:
            max_clock = cpu.max
    return max_clock

def _get_processor_name():
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if line.startswith('model name'):
                return line.split(':')[1].strip()
    return "Unknown"


def getProcessorData ():
	processor_name = _get_processor_name()
	max_clock_speed = str(_get_max_cpu_clock()/1000)
	return "Processor: \t" + processor_name + ", Max: " + max_clock_speed + "GHz\n"