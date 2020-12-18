#!/usr/bin/env python3

import sys
import getopt
from ClassroomAnswers import p5rClassroomQuestions
from ConfidantGuides import p5rConfidantGuide
from Activities import p5rActivities
from colors import colors
from Help import help

CLEAR = colors.bcolors.ENDC
RED = colors.bcolors.FAIL
PINK = colors.bcolors.HEADER
BOLD = colors.bcolors.BOLD
UNDER = colors.bcolors.UNDERLINE
GREEN = colors.bcolors.OKGREEN
BLUE = colors.bcolors.OKBLUE
YELLOW = colors.bcolors.WARNING


def getConfidant(isVerbose):
    """
    Gets the formatted name of the confidant that the
    user needs information about
    """
    if isVerbose:
        print('Getting user input for confidant name...')
    confidant = p5rConfidantGuide.chooseConfidant(isVerbose)
    if isVerbose:
        print('User input received...', confidant, 'chosen')
    return confidant


def main():
    """The literal main"""
    days = {}
    argv = sys.argv
    argc = len(argv)
    provided_confidant = ''
    conf_given = False
    args = ['help=', 'answers=', 'verbose=', 'confidants=', 'daily=']
    try:
        options, remainder = getopt.gnu_getopt(argv[1:], 'vhac:d', args)
    except getopt.GetoptError:
        for i in range(len(argv)):
            # go through each argument and check for a 'c' or 'confidant' since
            # no other argument has 'c' in the name
            if 'c' in argv[i] or 'confidant' in argv[i]:
                command = ' '.join(argv[0:])
                print('Invalid number of arguments in command', command)
                print('Confidant mode requires additional input...')
                help.confidantHelp()
                exit(1)
        print('Invalid number of arguments in command', ' '.join(argv[0:]))
        exit(1)

    isVerbose = False
    helpFlag = False
    ansFlag = False
    confidantFlag = False
    activitiesFlag = False
    confidantArg = ''
    if len(options) > 0:
        # need to run through first time to check if verbose flag is set
        for opt, arg in options:
            if opt in ('-v', '--verbose'):
                isVerbose = True
            elif opt in ('-h', '--help'):
                helpFlag = True
            elif opt in ('-a', '--answers'):
                ansFlag = True
            elif opt in ('-c', '--confidants'):
                confidantFlag = True
                if arg is None or arg == '':
                    # confidantHelp()
                    help.confidantHelp()
                    exit(1)
                confidantArg = arg
                if p5rConfidantGuide.isConfidant(argv[argc-1]):
                    conf_given = True
                    provided_confidant = argv[argc-1]
            elif opt in ('-d', '--daily'):
                activitiesFlag = True

    else:
        help.printHelp()

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
        getName = p5rConfidantGuide.normalizeName
        printDialogue = p5rConfidantGuide.printDialogueAnswers
        getGifts = p5rConfidantGuide.getBestGift
        if arg == 'all' or arg == 'a':
            confidant = getConfidant(isVerbose)
            # printAllConfidantInfo()
            pass
        elif arg == 'dialogue' or arg == 'd':
            if not conf_given:
                confidant = getConfidant(isVerbose)
                # p5rConfidantGuide.printDialogueAnswers(confidant, isVerbose)
                printDialogue(provided_confidant, isVerbose)
            else:
                provided_confidant = getName(provided_confidant)
                printDialogue(provided_confidant, isVerbose)
        elif arg == 'gifts' or arg == 'g':
            if not conf_given:
                confidant = getConfidant(isVerbose)
                gifts = getGifts(confidant, isVerbose)
            else:
                provided_confidant = getName(provided_confidant)
                gifts = getGifts(provided_confidant, isVerbose)
            for gift in gifts:
                print(gift)
        elif arg == 'hangout' or arg == 'h':
            confidant = getConfidant(isVerbose)
            # printHangoutLocation(confidant)
            pass
        elif arg == 'list' or arg == 'l':
            p5rConfidantGuide.listConfidants()
        else:
            options = '"dialogue", "gifts", "hangout", "list", and "all"'
            print('options are: {}'.format(options))
            # printAllConfidantInfo()
    elif activitiesFlag:
        p5rActivities.getActivities()
        # p5rActivities.getDay()


if __name__ == '__main__':
    main()
