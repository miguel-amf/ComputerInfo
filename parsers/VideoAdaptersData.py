import subprocess

def _getGpu():
    try:
        output = subprocess.check_output(['lshw', '-C', 'display'])
        output = output.decode('utf-8')
        lines = output.split('\n')
        gpuNames = []
        for line in lines: 
            if 'product' in line.lower():
                name = line.split(':')[1].strip()
                gpuNames.append(name)
        return gpuNames if gpuNames else None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def getVideoAdaptersData():

    outputString = "GPU:\t\t"
    gpuNames = _getGpu()
    if gpuNames is not None:
        for gpu in gpuNames:
            outputString += gpu + ' | '
    else:
        outputString += 'no GPU Found'

    outputString = outputString[:-3]
    return outputString + '\n'