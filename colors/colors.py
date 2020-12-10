class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

color_map = {
    'Guts': bcolors.HEADER,
    'Charm': bcolors.FAIL,
    'Knowledge': bcolors.OKBLUE,
    'Proficiency': bcolors.WARNING,
    'Kindness': bcolors.OKCYAN,
    'Courage': bcolors.OKGREEN
}

color_mapper = {
    'red': bcolors.FAIL,
    'pink': bcolors.HEADER,
    'yellow': bcolors.WARNING,
    'blue': bcolors.OKBLUE,
    'bold': bcolors.BOLD,
    'underline': bcolors.UNDERLINE,
    'green': bcolors.OKGREEN,
    'end': bcolors.ENDC
}

def putColor(line, before):
    """Returns the passed in line with color"""
    return str(before) + str(line) + bcolors.ENDC 
