import re
from P5RGuide.ConfidantGuides.DialogueGuide import get_path_to_file
from P5RGuide.colors.colors import bcolors

AVAILABLE_CONFIDANTS = ['Ann Takamaki', 'Sadayo Kawakami', 'Makoto Nijima']

def printAvailableConfidants():
    """Prints the list of available confidants for the gifts"""
    for c in AVAILABLE_CONFIDANTS:
        print(c, end='    ')
    print()

def getPathToGift(filepath, confidant, isVerbose):
    """Returns the filepath to the best gifts for the given confidant"""
    filepath += '/Gifts'
    if confidant == 'Ann Takamaki':
        filepath += '/AnnGifts.txt'
    elif confidant == 'Sadayo Kawakami':
        filepath += '/KawakamiGifts.txt'
    elif confidant == 'Makoto Nijima':
        filepath += '/MakotoGifts.txt'
    return filepath

def getScoreIdx(parts, isVerbose):
    """Returns the index of the first +x where x is the score"""
    count = 0
    for part in parts:
        if part[0] == '+':
            return count
        count += 1
    return None 

def putColor(parts, idx, colors):
    """colors the output at index idx"""
    part = parts[idx]
    temp = colors + part + bcolors.ENDC
    parts[idx] = temp

def putColors(parts, begin, end, colors):
    """Puts the colors between begin and end"""
    while begin < end:
        part = parts[begin]
        temp = colors + part + bcolors.ENDC
        parts[begin] = temp
        begin += 1

def checkP5R(parts):
    """Checks for the P5R string in the message"""
    idx = 0
    begin = end = 999
    if '(P5R' in parts or 'P5R)' in parts:
        for part in parts:
            if part[0] == '(':
                begin = idx
            if part[-1] == ')':
                end = idx
            idx += 1
        if begin == 999 or end == 999:
            return -1
        return (begin, end)
    return -1

def checkSpecialChars(line, s_char, color, isVerbose):
    """Returns the colored special characters (^*) in the string"""
    if s_char in line:
        parts = line.split(s_char)
        temp = color + s_char + bcolors.ENDC
        return temp.join(parts[:]) 
    return -1
                
def getBestGift(confidant, isVerbose):
    """Returns the list of best gifts for the given confidant"""
    filepath = get_path_to_file(confidant, isVerbose) 
    filepath = getPathToGift(filepath, confidant, isVerbose)
    try:
        with open(filepath) as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                parts = line.split(' ')
                score_idx = getScoreIdx(parts, isVerbose)
                putColor(parts, score_idx, bcolors.OKGREEN)
                tup = checkP5R(parts)
                if tup != -1:
                    putColors(parts, tup[0], tup[1] + 1, bcolors.FAIL)
                lines[count] = ' '.join(parts[:])
                temp = checkSpecialChars(line, '*', bcolors.WARNING, isVerbose)
                if temp != -1:
                    lines[count] = temp
                temp = checkSpecialChars(lines[count], '^', bcolors.HEADER, isVerbose)
                if temp != -1:
                    lines[count] = temp
                count += 1
            return lines
    except IsADirectoryError:
        print(f'Support for {confidant} has not been added yet')
        print('The list of available confidants can be seen below')
        printAvailableConfidants()
        exit(1)
