from picamera import PiCamera
from clock import timer
from segment import *
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
camera = PiCamera()

def startup():
    #Returns a default bundle that will be passed into the play function
    return {'Topic': 'random', 'Players' : 1}

def analyze(list,bundle,emotion):
    """ takes the list of dictionaries returned by face
        data and outputs messages
        -input is dumo
        -returns nothing"""
    grades={'UNKNOWN':'F','VERY_UNLIKELY':'D', 'UNLIKELY':'C','POSSIBLE':'B', 'VERY_LIKELY':'A'}
    gradeValue = {'A' : random.randint(90,99), 'B' : random.randint(80,89), 'C' : random.randint(70,79),
                  'D' : random.randint(60,69), 'F' : random.randint(30, 50) }


    grade1=grades[list[0][emotion]]
    grade1V = str(gradeValue[grade1])
    
    print(grade1)
    if bundle['Players']!=1:  # more than one player
        grade2=grades[list[1][emotion]]
        
        if grade2 <  grade1:
            lcd.message('Player two wins!')
            
            time.sleep(2)
            lcd.clear()
        elif grade1 < grade2:
            time.sleep(2)
            lcd.clear()
            lcd.message('Player one wins!')
        elif  grade1 == grade2:
            time.sleep(2)
            lcd.clear()
            lcd.message('Its a tie! :D')
            time.sleep(3)
            lcd.clear()
        lcd.message('Scores: Player 1: %s\nPlayer 2: %s' % (grade1,grade2))

    else: #one player
        print('got into the 1 player')
        setValue(grade1V[0], left)
        setValue(grade1V[1], right)
        
        lcd.clear()
        time.sleep(1)
        lcd.message('Score:  %s' % (grade1))
        if grade1<='B':
            time.sleep(5)
            lcd.clear()
            lcd.message('Good Job!')
            time.sleep(3)
            lcd.clear()
        else:
            time.sleep(3)
            lcd.clear()
            lcd.message('Not convincing\nTry again!')
            time.sleep(3)
            lcd.clear()

    
    return 0

def play(bundle):
    #Takes in a bundle that will be used as the paramaters of the game
    #API & 0ther functionality will be encapsulated in here
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
        camera.start_preview()
        time.sleep(2)
        camera.capture('/home/pi/piProject/image.jpg')
        camera.stop_preview()
        img = '/home/pi/piProject/image.jpg'
        try:
            dumo = getFaceData.Main(img, bundle['Players'])
            reString1 = dumo[0][str(emotion)]
            analyze(dumo,bundle, emotion)
        except KeyError:
            lcd.clear()
            lcd.message("Could not detect\nface. Try again.")
            time.sleep(5)
            print "Key error raised."
            return -1
            
        
    lcd.clear()
    return 0

def getTopic(theme):
    #This code will randomly get the type of topic you want based on the theme

    All = ['joyLikelihood','sorrowLikelihood', 'angerLikelihood','surpriseLikelihood']
    if theme == 'random':
        return random.choice(All)

    return theme
  
def option():
    #Modifies and returns a non-default bundle for different gamemodes
    newTopic = 'random'
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
         players = fac2
    lcd.clear()
    lcd.message("Topic:    %s\nPlayers:       %s" % (newTopic, players))
    time.sleep(3)
    lcd.clear()
    lcd.message("Options Saved")


    newBundle = {'Topic' : newTopic, 'Players' : players}
    return newBundle #To be passed into play.

def playMore():
    #determines if we play again
    #returns bool
        lcd.clear()
        lcd.message('Play again?\nYes        No')
        if pressed() == 'left':
             lcd.clear()
             return 1
        elif pressed() == 'right':
             lcd.clear()
             lcd.message('Goodbye!')
             
             return 0


### LET THE GAME BEGIN ###
if __name__ == "__main__":
    #While loop here that will end when the user no longer wants to play.
    #Returns to initial state.
    #We don't need to end the code, we can just put it on stand-by.
    again=1
    while again!=0:
        "Again is true!"
        defaultBundle = startup()
        lcd.message("## GAME_TITLE ##\nStart    Options")
        whichButton = pressed()
        if whichButton == 'left':
            print defaultBundle
            play(defaultBundle)
        elif whichButton == 'right':
            bundle = option()
            print bundle
            play(bundle)
        again=playMore()

        

