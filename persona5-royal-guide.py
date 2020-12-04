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
    print('Sudacode Persona 5 Royal Guide Help Menu\n')
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

def main():
    """The literal main"""
    days = {}
    argv = sys.argv
    argc = len(argv)
    options, remainder = getopt.gnu_getopt(argv[1:], 'vhac:', ['help=',
                                                               'answers=',
                                                               'verbose=',
                                                               'confidants='])
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
                confidantArg = arg
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
            confidant = getConfidant(isVerbose)
            p5rConfidantGuide.printDialogueAnswers(confidant)
            pass
        elif arg == 'hangout' or arg == 'h':
            confidant = getConfidant(isVerbose)
            # printHangoutLocation(confidant)
            pass
        else:
            print('options are: "dialogue", "hangout", and "all"')
            # printAllConfidantInfo()
            pass

if __name__ == '__main__':
    main()
