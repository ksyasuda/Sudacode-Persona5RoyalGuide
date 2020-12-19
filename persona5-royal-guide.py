#!/usr/bin/env python3

import P5RGuide.Utility.utility as utility
from P5RGuide.ClassroomAnswers import p5rClassroomQuestions
from P5RGuide.ConfidantGuides import p5rConfidantGuide
from P5RGuide.Activities import p5rActivities
from P5RGuide.colors import colors
from P5RGuide.Help import help

CLEAR = colors.bcolors.ENDC
RED = colors.bcolors.FAIL
PINK = colors.bcolors.HEADER
BOLD = colors.bcolors.BOLD
UNDER = colors.bcolors.UNDERLINE
GREEN = colors.bcolors.OKGREEN
BLUE = colors.bcolors.OKBLUE
YELLOW = colors.bcolors.WARNING


def main():
    """The literal main"""
    options, remainder, argc, argv = utility.get_opts()
    utility.handle_options(options, remainder, argc, argv)

if __name__ == '__main__':
    main()
