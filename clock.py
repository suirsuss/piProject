from segment import *

 #Clears out any unncessary information held before the code was run
#Segments. Declared as a dictionary with key-value pairs
right = {'SDI' : 21, 'RCLK' : 20, 'SRCLK' : 16 }
left = {'SDI' : 18, 'RCLK' : 17, 'SRCLK' : 27 }

setup(right)
setup(left)

# 15 second countdown example

##leftNum = setValue('1', left)
##rightNum = setValue('5', right)
##
##while leftNum != 0 or rightNum != 0:
##    while rightNum != 0:
##        time.sleep(1)
##        rightNum = rightNum - 1;
##        setValue(str(rightNum), right)
##    time.sleep(1)
##    if leftNum == 0:
##        break
##    leftNum = leftNum - 1
##    setValue(str(leftNum), left)
##    rightNum = 9
##    setValue(str(rightNum), right)
##
##GPIO.cleanup()   
##
##     

def timer(digits):
    #I made it simple. All you gotta do is set time equal to the time you want
    #to countdown from. That's it!
    #Make sure that time is two-digits only.
    strtime = str(digits)

    leftNum = setValue(strtime[0], left)
    rightNum = setValue(strtime[1], right)

    while leftNum != 0 or rightNum != 0:
        while rightNum != 0:
            time.sleep(1)
            rightNum = rightNum - 1;
            setValue(str(rightNum), right)
        time.sleep(1)
        if leftNum == 0:
            break
        leftNum = leftNum - 1
        setValue(str(leftNum), left)
        rightNum = 9
        setValue(str(rightNum), right)
    return 0;

