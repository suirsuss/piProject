import RPi.GPIO as GPIO
import time

# Here is going to be the code & the setup for the timer.

#Segments. Declared as a dictionary with key-value pairs
right = {'SDI' : 21, 'RCLK' : 20, 'SRCLK' : 16 }
left = {'SDI' : 18, 'RCLK' : 17, 'SRCLK' : 27 }

def setup(segment):
    GPIO.setmode(GPIO.BCM)    #Number GPIOs by its PI value
    GPIO.setup(segment['SDI'], GPIO.OUT)
    GPIO.setup(segment['RCLK'], GPIO.OUT)
    GPIO.setup(segment['SRCLK'], GPIO.OUT)
    GPIO.output(segment['SDI'], GPIO.LOW)
    GPIO.output(segment['RCLK'], GPIO.LOW)
    GPIO.output(segment['SRCLK'], GPIO.LOW)

def setValue(value, segment):
    key = {'0' : 0x3f, '1' : 0x06, '2' : 0x5b, '3' : 0x4f, '4' : 0x66, '5' : 0x6d, '6' : 0x7d,
      '7' : 0x07, '8' : 0x7f, '9' : 0x6f, 'A' : 0x77, 'B' : 0x7c, 'C' : 0x39, 'D' : 0x5e, 'E' : 0x79, 'F' : 0x71, '.' : 0x80}

    number = key[value]
    for bit in range(0, 8): 
        GPIO.output(segment['SDI'], 0x80 & (number << bit))
        GPIO.output(segment['SRCLK'], GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(segment['SRCLK'], GPIO.LOW)

    GPIO.output(segment['RCLK'], GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(segment['RCLK'], GPIO.LOW)
    return int(value)
