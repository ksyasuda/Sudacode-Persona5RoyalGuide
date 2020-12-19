#!/usr/bin/env python

import sys
import os

def getInput(isVerbose):
    """Gets input from the user about the current month and day"""
    monthMap = {'JANUARY': 1, 'FEBRUARY': 2, 'MARCH': 3, 'APRIL': 4, 'MAY': 5, 'JUNE': 6, 'JULY': 7, 'AUGUST': 8, 'SEPTEMBER': 9, 'OCTOBER': 10, 'NOVEMBER': 11, 'DECEMBER': 12, 'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    if isVerbose:
        print('Getting User Data...')
    month = input('Which Month (String or Integer)? ')
    # if input is a string then convert it into its numerical equivalent
    if not month.isnumeric():
        tempMonth = month.upper()
        if tempMonth in monthMap:
            month = monthMap[tempMonth]
        else:
            print(month, 'is not a valid month')
            sys.exit(1)
    day = input('What Day (Integer)? ')
    datestr = str(month) + "/" + str(day)
    if isVerbose:
        print('User input received... generating and returning date string', datestr)
    return datestr

def printData(days, day, isVerbose):
    """Print answers to questions on day [day]"""
    if isVerbose:
        print('Searching dictionary for date string', day)
    if day in days:
        if isVerbose:
            print(day, 'found in dictionary... printing information about the day')
        for key in days[day]:
            ## [Q/A]: [Question/Answer] 
            print(key, days[day][key])
    else:
        print(day, 'is not a day where questions are asked in class')

def readQuestions(days, isVerbose):
    """Read the questions from the file at $CWD/P5RClassroomAnswers.txt, then parses it into the days dict"""
    ## get path of current file, following sym-links
    pathToScript = os.path.realpath(__file__)
    # take off the filename and last '/'
    filepath = pathToScript[0:pathToScript.rfind('/')]
    filepath += '/P5RClassroomAnswers.txt'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August',  'September', 'November', 'December']
    with open(filepath) as f:
        lines = f.readlines()
        # first line will be date 4/12
        day = {}
        date = lines[0]
        first = True
        for i in range(len(lines)):
            # first date already set skip
            # don't need empty lines either
            if i == 0 or lines[i][:lines[i].find(' ')] in months:
                continue
            parts = lines[i].split(' ')
            if len(parts) == 1:
                # date string
                days[date.rstrip()] = day
                if isVerbose:
                    print('DATE: ', parts[0], 'Q/A', day)
                day = {}
                date = parts[0] 
            elif len(parts) >= 2 and parts[0] == 'EXAMS':
                # exams date string
                days[date.rstrip()] = day
                date = parts[1]
                if isVerbose:
                    print('DATE: ', parts[1], 'Q/A', day)
                day = {}
            else:
                # append to the day dictionary the entire question/answer
                day[parts[0]] = ' '.join(parts[1:]).rstrip()
        ## One last day of questions
        days[date.rstrip()] = day
        if isVerbose:
            print('Finished loading dictionary... ready for user input')
