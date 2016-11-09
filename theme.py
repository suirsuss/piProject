### FILE FOR ALL THE TYPES OF THEME FOR THE GAME ###
import random

def getTopic(difficulty):
    #This code will randomly get the type of topic you want based on the theme

    All = {'easy' : ['Happy','Sad','Mad', 'Surprised'],
           'medium' : ['Med1', 'Med2', 'Med3'],
           'hard':[ 'Hard1', 'Hard2', 'Hard3'] }
           #...etc...#

    items = All[difficulty.lower()]
    item = random.randint(0,len(items)-1)

    return All[difficulty.lower()][item]
