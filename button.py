# FUNCTIONALITY FOR THE BUTTONS ###

### Setup for the buttons###
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def pressed():
    #Will return which button is pressed as a string
    while True:
        if GPIO.input(12) == GPIO.LOW: #If Left is pressed
            return 'left'
        if GPIO.input(24) == GPIO.LOW: #if right is pressed
            return 'right'
