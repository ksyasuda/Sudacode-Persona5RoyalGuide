#!/usr/bin/env python3

import getopt
from p5rClassroomQuestions import *

def printHelp():
    print('Help')
    print('When In Doubt, Factor Out - Mr. Kim')

def main():
    days = {}
    argv = sys.argv
    argc = len(argv)
    isVerbose = False
    # if argc > 1 and argv[1] == '-v':
    #    isVerbose = True 
    options, remainder = getopt.gnu_getopt(argv[1:], 'hcv', ['help=',
                                                             'class=',
                                                             'verbose='])
    # need to run through first time to check if verbose flag is set
    helpFlag = False
    classFlag  = False
    for opt, arg in options:
        if opt in ('-v', '--verbose'):
            isVerbose = True
        elif opt in ('-h', '--help'):
            helpFlag = True 
        elif opt in ('-c', '--class'):
            classFlag = True
    if helpFlag:
        printHelp()
        sys.exit(0)
    if classFlag:
        readQuestions(days, isVerbose)
        chosenDate = getInput(isVerbose)
        printData(days, chosenDate, isVerbose)

if __name__ == '__main__':
    main()
