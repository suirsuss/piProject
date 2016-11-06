### FILE FOR ALL THE TYPES OF THEME FOR THE GAME ###


def getTopic(theme):
    #This code will randomly get the type of topic you want based on the theme

    All = {'nature' : ['dog', 'cat', 'hamster', 'butterfly', 'flower', '...'],
           'animals' : ['lion', 'zebra', '...']
           #...etc...#
           }

    return All[theme.lower()][2]
