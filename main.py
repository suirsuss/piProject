from clock import timer
from theme import *
from button import *
import Adafruit_CharLCD as LCD


###=========SET-UP==========###
lcd_rs        = 23
lcd_en        = 5
lcd_d4        = 6
lcd_d5        = 13
lcd_d6        = 19
lcd_d7        = 26
lcd_backlight = 4
lcd_columns =   16
lcd_rows    =   2
###==========================###

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

def startup():
    #Returns a default bundle that will be passed into the play function
    return {'Theme': 'Animals', 'Time' : 15, 'Players' : 1}

def play(bundle):
    #Takes in a bundle that will be used as the paramaters of the game
    #API & Other functionality will be encapsulated in here
    Theme = bundle['Theme']
    Topic = getTopic(Theme)
    lcd.clear()
    lcd.message(Topic)

    result = timer(bundle['Time'])


    if result:
        lcd.clear()
        lcd.message("Time's up!")
        time.sleep(5)

    if bundle['Players'] == 2:
        lcd.clear()
        lcd.message("Player 2 Turn")

def option():
    #Modifies and returns a non-default bundle for different gamemodes
    lcd.clear()
    lcd.message('...')
    if pressed() == 'left':
        #Left Button code
    elif pressed() == 'right':
        #right button code


    newBundle = {'Theme' : '...', 'Time' : '...', 'Players' : '...'}
    return newBundle #To be passed into play.




### LET THE GAME BEGIN ###
if __name__ == "__main__":
    defaultBundle = startup()
    lcd.message("## GAME_TITLE ##\nStart    Options")
    #Button functionality here to allow the game to start or whatever
    whichButton = pressed()
    if whichButton == 'left'
        play(defaultBundle)
    elif whichButton == 'right'
        newBundle = option()


    play(newBundle)
