### FUNCTIONALITY FOR THE BUTTONS ###

### Setup for the buttons###
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup('''leftButtonGPIO''', GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup('''rightButtonGPIO''', GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def pressed():
    #Will return which button is pressed as a string
    while True:
        if GPIO.input('''leftButtonGPIO''') == 1 #If Left is pressed
            return 'left'
        if GPIO.input('''rightButtonGPIO''') == 1 #if right is pressed
            return 'right'
    
