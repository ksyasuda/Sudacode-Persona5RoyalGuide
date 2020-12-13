#!/usr/bin/env python3

import sys
import getopt
from ClassroomAnswers import p5rClassroomQuestions
from ConfidantGuides import p5rConfidantGuide
from Activities import p5rActivities
from colors import colors

CLEAR = colors.bcolors.ENDC
RED = colors.bcolors.FAIL
PINK = colors.bcolors.HEADER
BOLD = colors.bcolors.BOLD
UNDER = colors.bcolors.UNDERLINE
GREEN = colors.bcolors.OKGREEN
BLUE = colors.bcolors.OKBLUE
YELLOW = colors.bcolors.WARNING

def getConfidant(isVerbose):
    """Gets the formatted name of the confidant that the user needs information about"""
    if isVerbose:
        print('Getting user input for confidant name...')
    confidant = p5rConfidantGuide.chooseConfidant(isVerbose)
    if isVerbose:
        print('User input received...', confidant, 'chosen')
    return confidant

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
    print(f'{GREEN}./persona5-royal-guide.py{CLEAR} -c {RED}[dialogue | hangout | list | all]{CLEAR} {YELLOW}[confidant name/keyword] (optional){CLEAR}')
    print(f'\n{BOLD + UNDER}Unless you provided the confident as an argument, upon entering confidant mode, you\'ll be prompted to input the name of the chosen confidant{CLEAR}\n')
    print(f'{PINK}Options{CLEAR}\n')
    print(f'{BOLD}dialogue{CLEAR}\t\t', 'Confidant dialogue option to get the best answers for each rank of the chosen confidant')
    print(f'{BOLD}hangout{CLEAR}\t\t\t', 'Prints the typical hangout spot for the chosen confidant')
    print(f'{BOLD}list{CLEAR}\t\t\t', 'Prints all the names/keywords of confidants that can be used during confidant selection or passed as an argument to the script')
    print(f'{BOLD}all{CLEAR}\t\t\t', 'Prints all information (dialogue options and hangout locations) about the chosen confidant')
    p5rConfidantGuide.listConfidants()

def main():
    """The literal main"""
    days = {}
    argv = sys.argv
    argc = len(argv)
    provided_confidant = ''
    conf_given = False
    try:
        options, remainder = getopt.gnu_getopt(argv[1:], 'vhac:d', ['help=',
                                                               'answers=',
                                                               'verbose=',
                                                               'confidants=',
                                                               'daily='])
    except getopt.GetoptError:
        for i in range(len(argv)):
            ## go through each argument and check for a 'c' or 'confidant' since
            ## no other argument has 'c' in the name 
            if 'c' in argv[i] or 'confidant' in argv[i]:
                print('Invalid number of arguments in command', ' '.join(argv[0:]))
                print('Confidant mode requires additional input...')
                confidantHelp()
                exit(1)
        print('Invalid number of arguments in command', ' '.join(argv[0:]))
        exit(1)
    isVerbose = False
    helpFlag = False
    ansFlag  = False
    confidantFlag = False
    activitiesFlag = False
    confidantArg = ''
    if len(options) > 0:
        ## need to run through first time to check if verbose flag is set
        for opt, arg in options:
            if opt in ('-v', '--verbose'):
                isVerbose = True
            elif opt in ('-h', '--help'):
                helpFlag = True 
            elif opt in ('-a', '--answers'):
                ansFlag = True
            elif opt in ('-c', '--confidants'):
                confidantFlag = True
                if arg == None or arg == '':
                    confidantHelp()
                    exit(1)
                confidantArg = arg
                if p5rConfidantGuide.isConfidant(argv[argc-1]):
                    conf_given = True
                    provided_confidant = argv[argc-1]
            elif opt in ('-d', '--daily'):
                activitiesFlag = True

    else:
        printHelp()

    if helpFlag:
        printHelp()
        sys.exit(0)
    if ansFlag:
        p5rClassroomQuestions.readQuestions(days, isVerbose)
        chosenDate = p5rClassroomQuestions.getInput(isVerbose)
        p5rClassroomQuestions.printData(days, chosenDate, isVerbose)
    if confidantFlag:
        if len(confidantArg) <= 0:
            print('No argument provided but 1 argument required...')
            exit(1)
        arg = confidantArg
        if arg == 'all' or arg == 'a':
            confidant = getConfidant(isVerbose)
            # printAllConfidantInfo()
            pass
        elif arg == 'dialogue' or arg == 'd':
            if not conf_given:
                confidant = getConfidant(isVerbose)
                p5rConfidantGuide.printDialogueAnswers(confidant, isVerbose)
            else:
                provided_confidant = p5rConfidantGuide.normalizeName(provided_confidant)
                p5rConfidantGuide.printDialogueAnswers(provided_confidant, isVerbose)
            pass
        elif arg == 'gift' or arg == 'g':
            if not conf_given:
                confidant = getConfidant(isVerbose)
            gift = p5rConfidantGuide.getBestGift(confidant, isVerbose)
        elif arg == 'hangout' or arg == 'h':
            confidant = getConfidant(isVerbose)
            # printHangoutLocation(confidant)
            pass
        elif arg == 'list' or arg == 'l':
            p5rConfidantGuide.listConfidants()
        else:
            print('options are: "dialogue", "hangout", "list", and "all"')
            # printAllConfidantInfo()
    elif activitiesFlag:
        p5rActivities.getActivities()
        # p5rActivities.getDay()
        

if __name__ == '__main__':
    main()
