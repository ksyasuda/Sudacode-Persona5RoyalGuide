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


def chooseConfidant(isVerbose):
    """Get input from user and return full name of confidant selected"""
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
              'Shinya Oda'}
    ## List of available names for input
    clist = ['KAWAKAMI', 'MORGANA', 'MAKOTO', 'HARU', 'YUSUKE', 'SOJIRO', 'ANN', 'RYUJI', 'GORO', 'FUTABA', 'CHIHAYA', 'TWINS', 'IWAI', 'TAE', 'SADAYO', 'ICHOKO', 'HIFUMI', 'YUUKI', 'TORANOSUKE', 'SAE', 'KASUMI', 'TAKUTO', 'MARUKI', 'TAKUTO MARUKI', 'YOSHIZAWA', 'KASUMI YOSHIZAWA', 'SAE NIJIMA', 'YOSHIDA', 'TORANOSUKE YOSHIDA', 'MISHIMA', 'YUUKI MISHIMA', 'TOGO', 'HIFUMI TOGO', 'SHINYA ODA', 'ODA', 'SHINYA', 'OHYA', 'ICHIKO OHYA', 'TAKEMI', 'TAE TAKEMI', 'MUNEHISA', 'IWAI MUNEHISA', 'MIFUNE', 'CHIHAYA MIFUNE', 'FUTABA SAKURA', 'AKECHI', 'GORO AKECHI', 'SAKAMOTO', 'RYUJI SAKAMOTO', 'TAKAMAKI', 'ANN TAKAMAKI', 'SOJIRO SAKURA', 'KITAGAWA', 'YUSUKE KITAGAWA', 'OKUMURA', 'HARU OKUMURA', 'MAKOTO NIJIMA']

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

def findBestAnswer(parts):
    scores = []
    indicies = []
    count = 0
    for part in parts:
        ## If a + is there a single digit follows guaranteed
        if part[0] == '+':
            scores.append(part[1])
            indicies.append(count)
        count += 1

    maxVal = -99999 ## initialize to low val
    index = 0 ## idx of highest value answer
    count = 0
    allSame = True
    ## indicies will only be size 1 when all same value
    for score in scores:
        if int(score) > int(maxVal):
            maxVal = int(score)
            index = count
        if count > 0 and scores[count] != scores[count - 1]:
            allSame = False
        count += 1

    ## If all the options have the same score
    if allSame:
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
        # if bestAnswer[0][0:1] == '\t':
        #     bestAnswer = bestAnswer[2:]
    ## best answer = an array containing each word in the answer
    bestAnswer = ' '.join(bestAnswer)
    return bestAnswer

def printDialogueAnswers(confidant):
    pathToScript = os.path.realpath(__file__)
    filepath = pathToScript[0:pathToScript.rfind('/')]
    if confidant == 'Sadayo Kawakami':
        filepath += '/KawakamiRomance.txt'
    elif confidant == 'Makoto Nijima':
        filepath += '/MakotoRomance.txt'
    with open(filepath) as f:
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
                print(parts[0], parts[1])
            elif parts[0] == 'Level' or parts[0] == 'MAX':
                ## make entire Level # X required bold
                temp = f'{bcolors.BOLD}'
                for i in range(len(parts)):
                    temp += ' ' + parts[i]
                print(temp)
                continue
            elif parts[0] == '(ROMANCE)':
                temp = f'{bcolors.WARNING}'
                temp += parts[0]
                print(temp)
                continue
            else:
                best = findBestAnswer(parts)
                print(f'{bcolors.ENDC}Best Answer: ', best)
