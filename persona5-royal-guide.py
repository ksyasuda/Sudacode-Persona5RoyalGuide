#!/usr/bin/env python3

import sys
import getopt
from ClassroomAnswers import p5rClassroomQuestions
from ConfidantGuides import p5rConfidantGuide

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
    print('\nSudacode Persona 5 Royal Guide Help Menu\n')
    print('Words of Advice:')
    print('When In Doubt, Factor Out - Mr. Kim\n')
    print('USAGE')
    print('./persona5-royal-guide.py [args]')
    print('OR')
    print('python persona5-royal-guide.py [args]\n')
    print('ARGUMENTS')
    print('-h, --help', '\t\tno extra args\t\t', 'Bring up the help menu')
    print('-v, --verbose', '\t\tno extra args\t\t', 'Enable verbose output')
    print('-a, --answers','\t\tno extra args\t\t', 'Get answers for in-game questions asked during class and exams')
    print('-c, --confidants', '\tone required arg\t', 'Get info about the confidants')

def confidantHelp():
    """Prints the help menu for the confidant mode"""
    print('\nConfidant Help Menu\n')
    print('Currently the only working options are dialog and list\n')
    print('Usage:')
    print('./persona5-royal-guide.py -c [dialog | hangout | list | all] [confidant name/keyword] (optional)')
    print('Unless you provided the confident as an argument, upon entering confidant mode, you\'ll be prompted to input the name of the chosen confidant')
    print('Options\n')
    print('dialogue\t\t', 'Confidant dialog option to get the best answers for each rank of the chosen confidant')
    print('hangout\t\t\t', 'Prints the typical hangout spot for the chosen confidant')
    print('list\t\t\t', 'Prints all the names/keywords of confidants that can be used during confidant selection or passed as an argument to the script')
    print('all\t\t\t', 'Prints all information (dialogue options and hangout locations) about the chosen confidant')

def main():
    """The literal main"""
    days = {}
    argv = sys.argv
    argc = len(argv)
    provided_confidant = ''
    conf_given = False
    try:
        options, remainder = getopt.gnu_getopt(argv[1:], 'vhac:', ['help=',
                                                               'answers=',
                                                               'verbose=',
                                                               'confidants='])
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
                if arg == None:
                    confidantHelp()
                    exit(1)
                confidantArg = arg
                if p5rConfidantGuide.isConfidant(argv[argc-1]):
                    conf_given = True
                    provided_confidant = argv[argc-1]

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
                p5rConfidantGuide.printDialogueAnswers(confidant)
            else:
                provided_confidant = p5rConfidantGuide.normalizeName(provided_confidant)
                p5rConfidantGuide.printDialogueAnswers(provided_confidant)
            pass
        elif arg == 'hangout' or arg == 'h':
            confidant = getConfidant(isVerbose)
            # printHangoutLocation(confidant)
            pass
        elif arg == 'list' or arg == 'l':
            p5rConfidantGuide.listConfidants()
        else:
            print('options are: "dialogue", "hangout", "list", and "all"')
            # printAllConfidantInfo()
            pass

if __name__ == '__main__':
    main()
