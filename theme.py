### FILE FOR ALL THE TYPES OF THEME FOR THE GAME ###
import random

def getTopic(theme):
    #This code will randomly get the type of topic you want based on the theme

    All = {'nature' : ['Dog', 'Cat', 'Hamster', 'Butterfly', 'Flower', '...'],
           'animals' : ['Lion', 'Zebra', '...']
           #...etc...#
           }
    items = All[theme.lower()]
    item = random.randint(0,len(items)-1)

    return All[theme.lower()][item]
