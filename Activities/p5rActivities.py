from colors.colors import color_mapper, putColor
import os

def getActivities():
    pathToScript = os.path.realpath(__file__)
    filepath = pathToScript[0:pathToScript.rfind('/')]
    filepath += '/DailyActivities.txt'
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(' ')
            if len(parts) == 1 or parts[0] in ('Rainy', 'Seasonal'):
                line = putColor(line, color_mapper['bold'] + color_mapper['underline'])
            elif '円' in line:
                ## if the last part has the yen kanji
                part = parts[-1]
                parts[-1] = putColor(part, color_mapper['red'])
                line = ' '.join(parts[:])
            if '(Afternoon)' in line:
                part = parts[-1]
                parts[-1] = putColor(part, color_mapper['yellow'])
                line = ' '.join(parts[:])
            print(line)
