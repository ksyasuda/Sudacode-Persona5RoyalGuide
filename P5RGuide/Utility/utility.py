import sys
import getopt
from P5RGuide.ConfidantGuides.p5rConfidantGuide import chooseConfidant
from P5RGuide.ConfidantGuides.p5rConfidantGuide import isConfidant
from P5RGuide.ConfidantGuides.p5rConfidantGuide import normalizeName
from P5RGuide.ConfidantGuides.p5rConfidantGuide import listConfidants 
from P5RGuide.ConfidantGuides.p5rConfidantGuide import printDialogueAnswers
from P5RGuide.ConfidantGuides.p5rConfidantGuide import getBestGift
from P5RGuide.ClassroomAnswers.p5rClassroomQuestions import readQuestions
from P5RGuide.ClassroomAnswers.p5rClassroomQuestions import getInput   
from P5RGuide.ClassroomAnswers.p5rClassroomQuestions import printData   
from P5RGuide.Activities.p5rActivities import getActivities
from P5RGuide.Help.help import printHelp
from P5RGuide.Help.help import printHelp


def getConfidant(isVerbose):
    """
    Gets the formatted name of the confidant that the
    user needs information about
    """
    if isVerbose:
        print('Getting user input for confidant name...')
    confidant = chooseConfidant(isVerbose)
    if isVerbose:
        print('User input received...', confidant, 'chosen')
    return confidant

def get_opts():
    """
    Parse the command-line arguments and returns a tuple of the (options, remainder) if
    found and exits if an exception occurs
    """
    argv = sys.argv
    argc = len(argv)
    provided_confidant = ''
    args = ['help=', 'answers=', 'verbose=', 'confidants=', 'daily=']
    try:
        options, remainder = getopt.gnu_getopt(argv[1:], 'vhac:d', args)
        return (options, remainder, argc, argv)
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


def handle_options(options, remainder, argc, argv):
    """
    Handles the command-line options, calling the relevant methods for each
    option
    """
    days = {}
    isVerbose = False
    helpFlag = False
    ansFlag = False
    confidantFlag = False
    activitiesFlag = False
    conf_given = False
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
                    confidantHelp()
                    exit(1)
                confidantArg = arg
                if isConfidant(argv[argc-1]):
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
        readQuestions(days, isVerbose)
        chosenDate = getInput(isVerbose)
        printData(days, chosenDate, isVerbose)
    if confidantFlag:
        if len(confidantArg) <= 0:
            print('No argument provided but 1 argument required...')
            exit(1)
        arg = confidantArg
        getName = normalizeName
        printDialogue = printDialogueAnswers
        getGifts = getBestGift
        if arg == 'all' or arg == 'a':
            confidant = utility.getConfidant(isVerbose)
            # printAllConfidantInfo()
            pass
        elif arg == 'dialogue' or arg == 'd':
            if not conf_given:
                confidant = getConfidant(isVerbose)
                # p5rConfidantGuide.printDialogueAnswers(confidant, isVerbose)
                printDialogue(confidant, isVerbose)
            else:
                provided_confidant = getName(provided_confidant)
                printDialogue(provided_confidant, isVerbose)
        elif arg == 'gifts' or arg == 'g':
            if not conf_given:
                confidant = utility.getConfidant(isVerbose)
                gifts = getGifts(confidant, isVerbose)
            else:
                provided_confidant = getName(provided_confidant)
                gifts = getGifts(provided_confidant, isVerbose)
            for gift in gifts:
                print(gift)
        elif arg == 'list' or arg == 'l':
            listConfidants()
        else:
            options = '"dialogue", "gifts", "list", and "all"'
            print('options are: {}'.format(options))
            # printAllConfidantInfo()
    elif activitiesFlag:
        getActivities()
        # p5rActivities.getDay()

