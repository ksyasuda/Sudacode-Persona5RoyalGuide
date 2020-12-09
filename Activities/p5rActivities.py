from colors.colors import color_mapper
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
                temp = color_mapper['bold'] + color_mapper['underline']
                temp += line + color_mapper['end'] 
                line = temp
            print(line)
