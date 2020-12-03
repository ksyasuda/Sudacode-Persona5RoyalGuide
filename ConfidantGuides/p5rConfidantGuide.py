#!/usr/bin/env python3

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
