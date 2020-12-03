#!/usr/bin/env python3

import getopt
from p5rClassroomQuestions import *

def printHelp():
    print('Sudacode Persona 5 Royal Guide Help Menu\n')
    print('Words of Advice:')
    print('When In Doubt, Factor Out - Mr. Kim\n')
    print('USAGE')
    print('./persona5-royal-guide.py [args]')
    print('OR')
    print('python persona5-royal-guide.py [args]\n')
    print('ARGUMENTS')
    print('-h, --help', '\t\t', 'Bring up the help menu')
    print('-v, --verbose', '\t\t', 'Enable verbose output')
    print('-c, --class','\t\t', 'Get answers for in-game questions asked during class and exams')

def main():
    days = {}
    argv = sys.argv
    argc = len(argv)
    isVerbose = False
    options, remainder = getopt.gnu_getopt(argv[1:], 'hcv', ['help=',
                                                             'class=',
                                                             'verbose='])
    helpFlag = False
    classFlag  = False
    if len(options) > 0:
        ## need to run through first time to check if verbose flag is set
        for opt, arg in options:
            if opt in ('-v', '--verbose'):
                isVerbose = True
            elif opt in ('-h', '--help'):
                helpFlag = True 
            elif opt in ('-c', '--class'):
                classFlag = True
    else:
        printHelp()

    if helpFlag:
        printHelp()
        sys.exit(0)
    if classFlag:
        readQuestions(days, isVerbose)
        chosenDate = getInput(isVerbose)
        printData(days, chosenDate, isVerbose)

if __name__ == '__main__':
    main()
