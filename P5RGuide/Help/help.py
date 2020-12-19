from P5RGuide.colors import colors
from P5RGuide.ConfidantGuides.DialogueGuide import listConfidants

CLEAR = colors.bcolors.ENDC
RED = colors.bcolors.FAIL
PINK = colors.bcolors.HEADER
BOLD = colors.bcolors.BOLD
UNDER = colors.bcolors.UNDERLINE
GREEN = colors.bcolors.OKGREEN
BLUE = colors.bcolors.OKBLUE
YELLOW = colors.bcolors.WARNING

def printHelp():
    """Prints the help menu for the script"""
    print(f'\n{BOLD + RED}Sudacode Persona 5 Royal Guide{CLEAR}\n')
    print(f'{UNDER}Words of Advice{CLEAR}:')
    print(f'{BOLD}When In Doubt, Factor Out - Mr. Kim{CLEAR}\n')
    print(f'{UNDER + BOLD + PINK}USAGE{CLEAR}')
    print(f'{GREEN}./persona5-royal-guide.py{CLEAR} {RED}[args]{CLEAR}')
    print(f'{RED}OR{CLEAR}')
    print(f'{GREEN}python persona5-royal-guide.py{CLEAR} {RED}[args]{CLEAR}\n')
    print(f'{BOLD + UNDER + PINK}ARGUMENTS{CLEAR}')
    print(f'{BOLD}-h, --help{CLEAR}', '\t\tno extra args\t\t', 'Bring up the help menu')
    print(f'{BOLD}-v, --verbose{CLEAR}', '\t\tno extra args\t\t', 'Enable verbose output')
    print(f'{BOLD}-a, --answers{CLEAR}','\t\tno extra args\t\t', 'Get answers for in-game questions asked during class and exams')
    print(f'{BOLD}-c, --confidants{CLEAR}', f'\t{RED}one required arg{CLEAR}\t', 'Get info about the confidants')
    print(f'{BOLD}-d, --daily{CLEAR}', '\t\tno extra args\t\t', 'Get a list of daily activities/events')

def confidantHelp():
    """Prints the help menu for the confidant mode"""
    print(f'\n{BOLD + UNDER + BLUE}Confidant Help Menu{CLEAR}\n')
    print(f'{BOLD + UNDER}Currently the only working options are dialog and list\n')
    print(f'{UNDER + PINK + BOLD}Usage{CLEAR}:')
    print(f'{GREEN}./persona5-royal-guide.py{CLEAR} -c {RED}[dialogue | gifts | hangout | list | all]{CLEAR} {YELLOW}[confidant name/keyword] (optional){CLEAR}')
    print(f'\n{BOLD + UNDER}Unless you provided the confident as an argument, upon entering confidant mode, you\'ll be prompted to input the name of the chosen confidant{CLEAR}\n')
    print(f'{PINK}Options{CLEAR}\n')
    print(f'{BOLD}dialogue{CLEAR}\t\t', 'Confidant dialogue option to get the best answers for each rank of the chosen confidant')
    print(f'{BOLD}gifts{CLEAR}\t\t\t', 'Prints the list of best gifts for the given confidant')
    print(f'{BOLD}hangout{CLEAR}\t\t\t', 'Prints the typical hangout spot for the chosen confidant')
    print(f'{BOLD}list{CLEAR}\t\t\t', 'Prints all the names/keywords of confidants that can be used during confidant selection or passed as an argument to the script')
    print(f'{BOLD}all{CLEAR}\t\t\t', 'Prints all information (dialogue options and hangout locations) about the chosen confidant')
    listConfidants()
