from picamera import PiCamera
from clock import timer
from theme import *
from button import *
import random
import Adafruit_CharLCD as LCD
import getFaceData 

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
GOOGLE_APPLICATION_CREDENTIALS='/home/pi/piProject/piProject-f12639f6b426.json'

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

def startup():
    #Returns a default bundle that will be passed into the play function
    return {'Topic': 'random', 'Players' : 1}

def analyze(playernum):
    return 0

def play(bundle):
    #Takes in a bundle that will be used as the paramaters of the game
    #API & Other functionality will be encapsulated in here
    lcd.clear()
    lcd.message('Let the game\nbegin!!')
    time.sleep(2)
    lcd.clear()
    emotion = getTopic(bundle['Topic'])
    lcd.message('%s' % emotion) 
    result = timer(10)

    if result:
        lcd.clear()
        lcd.message("Time's up!")
        print "taking picture..."
        camera = PiCamera()
        camera.start_preview()
        time.sleep(1)
        camera.capture('/home/pi/piProject/image.jpg')
        camera.stop_preview()
        img = '/home/pi/piProject/image.jpg'
        dumo = getFaceData.Main(img, bundle['Players'])
        dumo['joyLikelihood']
    print "Successful!"
    lcd.clear()
    lcd.message("You can code!!!")
    return 0

def getTopic(theme):
    #This code will randomly get the type of topic you want based on the theme

    All = ['joyLikelihood','sorrowLikelihood', 'angerLikelihood','surpriseLikelihood']
    if theme == 'random':
        return random.choice(All)

    return theme
  
def option():
    #Modifies and returns a non-default bundle for different gamemodes
    lcd.clear()
    lcd.message("Option Menu")
    time.sleep(2)
    lcd.clear()
    lcd.message("Topic\nJoy        Next")
    if pressed() == 'right':
        lcd.clear()
        lcd.message("Topic\nSorrow      Next")
        if pressed() == 'right':
            lcd.clear()
            lcd.message("Topic\nAnger   Surprise")
            if pressed() == 'left':
                newTopic = 'angerLikelihood'
            elif pressed() == 'right':
                newTopic = 'surpriseLikelihood'
        elif pressed() == 'left':
            newTopic = 'sorrowLikelihood'
    elif pressed() == 'left':
        newTopic = 'joyLikelihood'
        lcd.clear()
    lcd.clear()
    lcd.message('Players\nOne          Two')
    if pressed() == 'left':
         players = 1
    elif pressed() == 'right':
         players = 2
    lcd.clear()
    lcd.message("Topic:    %s\nPlayers:       %s" % (newTopic, players))
    time.sleep(3)
    lcd.clear()
    lcd.message("Options Saved")


    newBundle = {'Topic' : newTopic, 'Players' : players}
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
    

