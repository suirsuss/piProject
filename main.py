from picamera import PiCamera
from clock import timer
from theme import *
from button import *
import random
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
    return {'Difficulty': 'Medium', 'Players' : 1}

def play(bundle):
    #Takes in a bundle that will be used as the paramaters of the game
    #API & Other functionality will be encapsulated in here
    lcd.clear()
    lcd.message('Let the game\nbegin!!')
    time.sleep(2)
    lcd.clear()
    lcd.message('Emotion')
    result = timer(10)


    if result:
        lcd.clear()
        lcd.message("Time's up!")
        print "taking picture..."
        camera = PiCamera()
        camera.start_preview()
        time.sleep(2)
        camera.capture('/home/pi/piProject/image.jpg')
        camera.stop_preview()
        
        #Send this image to google analysis
        #Vision('''image''') --> returns result. Saves result if multiplayer
        #send results back in the findWinner() function

        

    if bundle['Players'] == 2:
        lcd.clear()
        lcd.message("Player 2 Turn")

def option():
    #Modifies and returns a non-default bundle for different gamemodes
    lcd.clear()
    lcd.message("Option Menu")
    time.sleep(2)
    lcd.clear()
    lcd.message("Difficulty\nEasy        Next")
    if pressed() == 'right':
        lcd.clear()
        lcd.message("Difficulty\nMedium      Next")
        if pressed() == 'right':
            lcd.clear()
            lcd.message("Difficulty\nHard        Back")
            if pressed() == 'left':
                difficulty = 'Hard'
            elif pressed() == 'right':
                difficulty = 'Medium'
        elif pressed() == 'left':
            difficulty = 'Medium'
    elif pressed() == 'left':
        difficulty = 'Easy'
        lcd.clear()
    lcd.message('Players\nOne          Two')
    if pressed() == 'left':
         players = 1
    elif pressed() == 'right':
         players = 2
    lcd.clear()
    lcd.message("Difficulty:    %s\nPlayers:       %s" % (difficulty[0], players))
    time.sleep(3)
    lcd.clear()
    lcd.message("Options Saved")


    newBundle = {'Difficulty' : difficulty, 'Players' : players}
    return newBundle #To be passed into play.






### LET THE GAME BEGIN ###
if __name__ == "__main__":
    #While loop here that will end when the user no longer wants to play.
    #Returns to initial state.
    #We don't need to end the code, we can just put it on stand-by.
    defaultBundle = startup()
    lcd.message("## GAME_TITLE ##\nStart    Options")
    whichButton = pressed()
    if whichButton == 'left':
        print "We're gonna play with default!"
        play(defaultBundle)
    elif whichButton == 'right':
        print "To the option menu!"
        bundle = option()
        play(bundle)
    

