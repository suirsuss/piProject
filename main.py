from clock import timer
import Adafruit_CharLCD as LCD

###=========SET-UP==========###
lcd_rs        = 23
lcd_en        = 5
lcd_d4        = 6
lcd_d5        = 13
lcd_d6        = 19
lcd_d7        = 26
lcd_backlight = 4
lcd_columns = 16
lcd_rows    = 2
###==========================###

if __name__ == "__main__":
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                               lcd_columns, lcd_rows, lcd_backlight)

    result = timer(15)

    if result:
        lcd.clear()
        lcd.message("Time's up!")
        GPIO.cleanup()
