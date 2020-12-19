#!/usr/bin/env python3

import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

color_map = {
    'Guts': bcolors.HEADER,
    'Charm': bcolors.FAIL,
    'Knowledge': bcolors.OKBLUE,
    'Proficiency': bcolors.WARNING,
    'Kindness': bcolors.OKCYAN,
    'Courage': bcolors.OKGREEN
}


## Mapper from first name or last name to full name
mapper = {'MAKOTO': 'Makoto Nijima', 'HARU': 'Haru Okumura', 'OKUMURA':
          'Haru Okumura', 'YUSUKE': 'Yusuke Kitagawa', 'KITAGAWA': 'Yusuke\
          Kitagawa', 'SOJIRO': 'Sojiro Sakura', 'ANN': 'Ann Takamaki',
          'TAKAMAKI': 'Ann Takamaki', 'RYUJI': 'Ryuji Sakamoto', 'SAKAMOTO':
          'Ryuji Sakamoto', 'GORO': 'Goro Akechi', 'AKECHI': 'Goro Akechi',
          'FUTABA': 'Futaba Sakura', 'CHIHAYA': 'Chihaya Mifune', 'MIFUNE':
          'Chihaya Mifune', 'IWAI': 'Iwai Munehisa', 'MUNEHISA': 'Iwai\
          Munehisa', 'TAE': 'Tae Takemi', 'TAKEMI': 'Tae Takemi', 'SADAYO':
          'Sadayo Kawakami', 'KAWAKAMI': 'Sadayo Kawakami', 'ICHIKO':
          'Ichiko Ohya', 'OHYA': 'Ichiko Ohya', 'SHINYA': 'Shinya Oda',
          'ODA': 'Shinya Oda', 'MAKOTO NIJIMA': 'Makoto Nijima', 'SAE\
          NIJIMA': 'Sae Nijima', 'HARU OKUMARU': 'Haru Okumaru', 'YUSUKE\
          KITAKAWA': 'Yusuku Kitagawa', 'SOJIRO SAKURA': 'Sojiro Sakura',\
          'ANN TAKAMAKI': 'Ann Takamaki', 'RYUJI SAKAMOTO': 'Ryuji\
          Sakamoto', 'GORO AKECHI': 'Goro Akechi', 'FUTABA SAKURA': 'Futaba\
          Sakura', 'CHIHAYA MIFUNE': 'Chihaya Mifune', 'IWAI MUNEHISA':
          'Iwai Munehisa', 'TAE TAKEMI': 'Tae Takemi', 'SADAYO KAWAKAMI':
          'Sadayo Kawakami', 'ICHIKO OHYA': 'Ichiko Ohya', 'SHINYA ODA':
          'Shinya Oda', 'KASUMI': 'Kasumi Yoshizawa', 'YOSHIZAWA': 'Kasumi\
          Yoshizawa', 'KASUMI YOSHIZAWA': 'Kasumi Yoshizawa', 'HIFUMI':
          'Hifumi Togo', 'TOGO': 'Hifumi Togo', 'HIFUMI TOGO': 'Hifumi Togo',
          'YOSHIDA': 'Toranosuke Yoshida', 'TORANOSUKE': 'Toranosuke Yoshida',
          'TORANOSUKE YOSHIDA': 'Toranosuke Yoshida'}


## List of available names for input
clist = ['KAWAKAMI', 'MORGANA', 'MAKOTO', 'HARU', 'YUSUKE', 'SOJIRO', 'ANN', 'RYUJI', 'GORO', 'FUTABA', 'CHIHAYA', 'TWINS', 'IWAI', 'TAE', 'SADAYO', 'ICHOKO', 'HIFUMI', 'YUUKI', 'TORANOSUKE', 'SAE', 'KASUMI', 'TAKUTO', 'MARUKI', 'TAKUTO MARUKI', 'YOSHIZAWA', 'KASUMI YOSHIZAWA', 'SAE NIJIMA', 'YOSHIDA', 'TORANOSUKE YOSHIDA', 'MISHIMA', 'YUUKI MISHIMA', 'TOGO', 'HIFUMI TOGO', 'SHINYA ODA', 'ODA', 'SHINYA', 'OHYA', 'ICHIKO OHYA', 'TAKEMI', 'TAE TAKEMI', 'MUNEHISA', 'IWAI MUNEHISA', 'MIFUNE', 'CHIHAYA MIFUNE', 'FUTABA SAKURA', 'AKECHI', 'GORO AKECHI', 'SAKAMOTO', 'RYUJI SAKAMOTO', 'TAKAMAKI', 'ANN TAKAMAKI', 'SOJIRO SAKURA', 'KITAGAWA', 'YUSUKE KITAGAWA', 'OKUMURA', 'HARU OKUMURA', 'MAKOTO NIJIMA']

def isConfidant(name):
    """Checks whether [name] is a valid confidant"""
    return name.strip().upper() in clist

def normalizeName(name):
    """Gets the name of the confidant used in the program from the name/keyword inputted by the user"""
    return mapper[name.strip().upper()] if name.strip().upper() in mapper else None

def get_path_to_file(confidant, isVerbose):
    """Returns the path to the dialogue file for [confidant]"""
    if isVerbose:
        print('Getting path to file for confidant', confidant)
    pathToScript = os.path.realpath(__file__)
    if isVerbose:
        print('Path to script =', pathToScript)
    filepath = pathToScript[0:pathToScript.rfind('/')]
    if isVerbose:
        print('Path after strip =', filepath)

    return filepath

def getPathToDialogue(filepath, confidant, isVerbose):
    filepath += '/dialogues'
    if confidant == 'Sadayo Kawakami':
        filepath += '/KawakamiRomance.txt'
    elif confidant == 'Makoto Nijima':
        filepath += '/MakotoRomance.txt'
    elif confidant == 'Kasumi Yoshizawa':
        filepath += '/KasumiRomance.txt'
    elif confidant == 'Hifumi Togo':
        filepath += '/HifumiRomance.txt'
    elif confidant == 'Tae Takemi':
        filepath += '/TakemiRomance.txt'
    elif confidant == 'Chihaya Mifune':
        filepath += '/ChihayaRomance.txt'
    elif confidant == 'Ichiko Ohya':
        filepath += '/OhyaRomance.txt'
    elif confidant == 'Haru Okumura':
        filepath += '/HaruRomance.txt'
    elif confidant == 'Futaba Sakura':
        filepath += '/FutabaRomance.txt'
    elif confidant == 'Ann Takamaki':
        filepath += '/AnnRomance.txt'
    elif confidant == 'Toranosuke Yoshida':
        filepath += '/YoshidaGuide.txt'
    elif confidant == 'Yusuke Kitagawa':
        filepath += '/YusukeGuide.txt'
    elif confidant == 'Goro Akechi':
        filepath += '/AkechiGuide.txt'
    if isVerbose:
        print('Full path', filepath)
    return filepath

def listConfidants():
    """Prints the list of available names/keywords that can be used when selecting a confidant"""
    clist.sort()
    print('------------------------------------------------------------------------------------------')
    print('\nList of available confidant keywords:\n')
    i = 0
    for name in clist:
        if i != 0 and i % 7 == 0:
            print(name+'\n')
        else:
            print(name, end=' | ')
        i += 1
    print('\n------------------------------------------------------------------------------------------')

def chooseConfidant(isVerbose):
    """Get input from user and return full name of confidant selected"""
    confidant = input('Which confidant do you need information about? ')
    if isVerbose:
        print('Input received... verifying input')
    temp = confidant.strip().upper()
    if temp not in clist:
        print(confidant, 'is not valid confidant name...')
        print('The list of available names is as follows:')
        print(clist)
        exit(1)
    if isVerbose:
        print(confidant, 'found in mapper... returning', mapper[temp])
    return mapper[temp]

def cleanupLine(bestAnswer, isVerbose):
    """Cleans up the line by removing and leading 'Response' or 'Followup' strings and remove unwanted spaces"""
    ## One last check to get rid of the lingering 'Response' or 'Followup' text at beginning of some lines
    if len(bestAnswer) != 0 and bestAnswer[0] == 'Response':
        if isVerbose:
            print('"Response" found in string')
            print('Popping off first two values of list...') 
        bestAnswer.pop(0)
        bestAnswer.pop(0)
    elif bestAnswer[0] == 'Followup':
        if isVerbose:
            print('"Followup" found in string')
            print('Popping off first value of list...') 
        bestAnswer.pop(0)
    ## Account for instance where + and the value are separate values at end of list
    if bestAnswer[len(bestAnswer) - 2] == '+':
        if isVerbose:
            print('Extra space detected')
            print('Appending to second to last element and pop off last element of the list')
        bestAnswer[len(bestAnswer) - 2] += bestAnswer[len(bestAnswer) - 1]
        bestAnswer.pop()

def findRomanceAnswer(parts, isVerbose):
    end_idx = parts.index('END') if 'END' in parts else None
    rom_idx = parts.index('(ROMANCE)') 
    if end_idx != None and end_idx < rom_idx:
        return ' '.join(parts[end_idx + 1:rom_idx + 1])
    elif end_idx != None and rom_idx < end_idx:
        return ' '.join(parts[2:rom_idx + 1])
    elif end_idx == None:
        idx = -1
        counter = 0
        if parts[-2] == '(ROMANCE)':
            for part in parts:
                if part[0] == '+':
                    idx = counter
                    break
                counter += 1
            return ' '.join(parts[idx + 1:len(parts) - 1])
        else:
            for part in parts:
                if part[0] == '+':
                    # start at one becuase there is Response x before the actual
                    # response
                    # counter + 2 because counter is still 1 behind here
                    return ' '.join(parts[1:counter + 2])
                counter += 1


def findBestAnswer(parts, isVerbose):
    """Parses the parts vector for the best answer for each dialogue option"""
    scores = []
    indicies = []
    count = 0
    if isVerbose:
        print('parsing line', ' '.join(parts[0:]))
    for part in parts:
        ## If a + is there a single digit follows guaranteed
        if part[0] == '+':
            scores.append(part[1])
            indicies.append(count)
        count += 1

    # Akechi level 9
    if len(scores) == 0 and parts[0] == 'Story':
        return (f'{bcolors.BOLD}' + ' '.join(parts[0:])) + f'{bcolors.ENDC}'
    
    maxVal = -99999 ## initialize to low val
    index = 0 ## idx of highest value answer
    count = 0
    allSame = True
    if isVerbose:
        print('line parsed... finding index of best option')
    ## indicies will only be size 1 when all same value
    for score in scores:
        if int(score) > int(maxVal):
            maxVal = int(score)
            index = count
        if count > 0 and scores[count] != scores[count - 1]:
            if isVerbose:
                print('All scores NOT the same')
            allSame = False
        count += 1

    ## If all the options have the same score
    if allSame:
        if isVerbose:
            print('All scores same')
        return 'Pick Any'

    bestAnswer = ''
    if index == 0: 
        ## if best option is the left most option
        bestAnswer = parts[:indicies[index]+1]
    else:
        idx = indicies[index-1]
        if index != len(parts) - 1:
            idx += 1
        beginIndex = idx
        endIndex = indicies[index]
        bestAnswer = parts[beginIndex:endIndex]
        bestAnswer += parts[endIndex]
        ## shouldn't need this anymore

    cleanupLine(bestAnswer, isVerbose)
    ## best answer = an array containing each word in the answer
    bestAnswer = ' '.join(bestAnswer)
    after_plus = bestAnswer[bestAnswer.find('+') + 1]
    return bestAnswer

def printDialogueAnswers(confidant, isVerbose):
    """Prints the best (or first if there is a tie) answers for dialogue with the chosen confidant"""
    print(f'{bcolors.UNDERLINE}{bcolors.BOLD}{bcolors.HEADER}Dialog Answers for', confidant + f':{bcolors.ENDC}')
    if isVerbose:
        print('Getting path to dialogue file for', confidant)
    filepath = get_path_to_file(confidant, isVerbose)
    filepath = getPathToDialogue(filepath, confidant, isVerbose)
    if isVerbose:
        print('Path =', filepath)
    ranknine = False
    with open(filepath) as f:
        if isVerbose:
            print(filepath, 'opened')
        lines = f.readlines()
        first = 0
        for line in lines:
            ## get rid of unwanted blank lines
            if len(line) == 0 or line == '\n':
                continue
            parts = line.split(' ')
            if parts[0] == 'Rank':
                ## make the Rank # bold
                temp = f'\n{bcolors.BOLD}'
                temp += parts[0]
                parts[0] = temp
                temp = f'{bcolors.BOLD}'
                temp += parts[1]
                parts[1] = temp
                temp += f'{bcolors.ENDC}'
                print(parts[0], parts[1])
                continue
            elif parts[0] == 'Level' or parts[0] == 'MAX':
                ## make entire Level # X required bold
                temp = f'{bcolors.BOLD}'
                attribute = ''
                if parts[0] == 'Level':
                    ## Level # [attribute] Required
                    attribute = parts[2]
                elif parts[0] == 'MAX':
                    ## MAX X Required
                    attribute = parts[1]
                temp += color_map[attribute]
                for i in range(len(parts)):
                    temp += ' ' + parts[i]
                temp += f'{bcolors.ENDC}'
                print(temp)
                continue
            elif parts[0] == '(ROMANCE)' and len(parts) > 1:
                temp = f'{bcolors.WARNING}'
                temp += parts[0]
                temp += f'{bcolors.ENDC}'
                print(temp)
                continue
            if '(ROMANCE)' in parts: 
                best = findRomanceAnswer(parts, isVerbose)
                temp = best.split(' ')
                last = bcolors.FAIL + temp[-1] + bcolors.ENDC
                temp[-1] = last
                best = ' '.join(temp[:])
                print(f'{bcolors.ENDC}Answer:', best)
            else:
                if isVerbose:
                    print(f'{bcolors.ENDC}finding best answer...')
                best = findBestAnswer(parts, isVerbose)
                if isVerbose:
                    print(f'{bcolors.ENDC}best answer found...')
                print(f'{bcolors.ENDC}Answer:', best)

## ----------------------------------------------------------------------------
## Gift guide

def getPathToGift(filepath, confidant, isVerbose):
    """Returns the filepath to the best gifts for the given confidant"""
    filepath += '/Gifts'
    if confidant == 'Ann Takamaki':
        filepath += '/AnnGifts.txt'
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
        exit(1)