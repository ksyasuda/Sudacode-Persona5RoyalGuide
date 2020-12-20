import os
import re


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


# Mapper from first name or last name to full name
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
          KITAKAWA': 'Yusuku Kitagawa', 'SOJIRO SAKURA': 'Sojiro Sakura',
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


# List of available names for input
clist = ['KAWAKAMI', 'MORGANA', 'MAKOTO', 'HARU', 'YUSUKE', 'SOJIRO', 'ANN',
         'RYUJI', 'GORO', 'FUTABA', 'CHIHAYA', 'TWINS', 'IWAI', 'TAE',
         'SADAYO', 'ICHOKO', 'HIFUMI', 'YUUKI', 'TORANOSUKE', 'SAE', 'KASUMI',
         'TAKUTO', 'MARUKI', 'TAKUTO MARUKI', 'YOSHIZAWA', 'KASUMI YOSHIZAWA',
         'SAE NIJIMA', 'YOSHIDA', 'TORANOSUKE YOSHIDA', 'MISHIMA',
         'YUUKI MISHIMA', 'TOGO', 'HIFUMI TOGO', 'SHINYA ODA', 'ODA',
         'SHINYA', 'OHYA', 'ICHIKO OHYA', 'TAKEMI', 'TAE TAKEMI', 'MUNEHISA',
         'IWAI MUNEHISA', 'MIFUNE', 'CHIHAYA MIFUNE', 'FUTABA SAKURA',
         'AKECHI', 'GORO AKECHI', 'SAKAMOTO', 'RYUJI SAKAMOTO', 'TAKAMAKI',
         'ANN TAKAMAKI', 'SOJIRO SAKURA', 'KITAGAWA', 'YUSUKE KITAGAWA',
         'OKUMURA', 'HARU OKUMURA', 'MAKOTO NIJIMA']


def isConfidant(name):
    """Checks whether [name] is a valid confidant"""
    return name.strip().upper() in clist


def normalizeName(name):
    """
    Gets the name of the confidant used in the program from the name/keyword
    inputted by the user
    """
    if name.strip().upper() in mapper:
        return mapper[name.strip().upper()]
    return None


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
    """
    Prints the list of available names/keywords that can be used when
    selecting a confidant
    """
    clist.sort()
    print('\nList of available confidant keywords:\n')
    i = 0
    for name in clist:
        if i != 0 and i % 7 == 0:
            print(name+'\n')
        else:
            print(name, end=' | ')
        i += 1


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
    """
    Cleans up the line by removing and leading 'Response' or 'Followup'
    strings and remove unwanted spaces
    """
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
    # Account for instance where + and value are separate values at end of list
    if bestAnswer[len(bestAnswer) - 2] == '+':
        if isVerbose:
            print('Extra space detected')
            print('Appending to second to last element', end='')
            print('and pop off last element of the list')
        bestAnswer[len(bestAnswer) - 2] += bestAnswer[len(bestAnswer) - 1]
        bestAnswer.pop()


def findRomanceAnswer(parts, isVerbose):
    line = ' '.join(parts[:])
    rom = re.compile(r'\(ROMANCE\)')
    rom_idx = rom.search(line)
    end = re.compile(r'END')
    end_idx = end.search(line)
    if rom_idx is not None and end_idx is None:
        plus = re.compile(r'\+\d\s')
        plus_idx = plus.search(line)
        if parts[-2] == '(ROMANCE)':
            return line[plus_idx.end():].strip()
        else:
            return line[10:rom_idx.end()].strip()
    if rom_idx.start() < end_idx.start():
        return line[10:rom_idx.end()].strip()
    else:
        return line[end_idx.end():rom_idx.end()].strip()


def check_scores(scores, isVerbose):
    """
    Checks the array of scores to see if all of the values are the same
    """
    all_same = True
    if isVerbose:
        print('SCORES', scores)
    for i in range(len(scores)):
        if i == 0:
            continue
        if scores[i-1] != scores[i]:
            all_same = False
    return all_same


def findBestAnswer(parts, isVerbose):
    """Parses the parts vector for the best answer for each dialogue option"""
    line = ' '.join(parts[:])
    # Shouldn't happen but want to know if it does
    if len(line) == 0:
        print('BLANK LINE')
        exit(1)
    pattern = re.compile(r'\+\d')
    matches = pattern.finditer(line)
    match_objs = []
    scores = []
    highest_score = -1
    count = 0
    for match in matches:
        # each group is '+SCORE'
        score = int(match.group()[1])
        if isVerbose:
            print('SCORE', score)
        scores.append(score)
        match_objs.append(match)
        if score > highest_score:
            highest_score = count
        count += 1

    # Akechi level 9
    if len(scores) == 0:
        return (f'{bcolors.BOLD}' + ' '.join(parts[0:])) + f'{bcolors.ENDC}'

    all_same = check_scores(scores, isVerbose)
    if all_same:
        return 'Pick any answer'

    if isVerbose:
        print('HIGHEST SCORE INDEX', highest_score)
    if highest_score == 0:
        first_word = line[:line.find(' ')]
        # 'Response X '
        if first_word == 'Response':
            return (line[10:match_objs[0].end()]).strip()
        # 'Followup '
        elif first_word == 'Followup':
            return (line[9:match_objs[0].end()]).strip()
    elif highest_score == 1:
        begin = int(match_objs[0].end()) + 1
        end = int(match_objs[1].end())
        return (line[begin:end]).strip()
    elif highest_score == 2:
        return (line[int(match_objs[1].end()) + 1:]).strip()
    return 'Pick any answer'


def printDialogueAnswers(confidant, isVerbose):
    """
    Prints the best (or first if there is a tie) answers for
    dialogue with the chosen confidant
    """
    clrs = '{bcolors.UNDERLINE}{bcolors.BOLD}{bcolors.HEADER}'
    print(f'{clrs}Dialog Answers for', confidant + f':{bcolors.ENDC}')
    if isVerbose:
        print('Getting path to dialogue file for', confidant)
    filepath = get_path_to_file(confidant, isVerbose)
    filepath = getPathToDialogue(filepath, confidant, isVerbose)
    if isVerbose:
        print('Path =', filepath)
    ranknine = False
    try:
        with open(filepath) as f:
            if isVerbose:
                print(filepath, 'opened')
            lines = f.readlines()
            first = 0
            for line in lines:
                # get rid of unwanted blank lines
                if len(line) == 0 or line == '\n':
                    continue
                parts = line.split(' ')
                if parts[0] == 'Rank':
                    # make the Rank # bold
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
                    # make entire Level # X required bold
                    temp = f'{bcolors.BOLD}'
                    attribute = ''
                    if parts[0] == 'Level':
                        # Level # [attribute] Required
                        attribute = parts[2]
                    elif parts[0] == 'MAX':
                        # MAX X Required
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
    except IsADirectoryError:
        print(f'Support for {confidant} has not been added yet')
        exit(1)
