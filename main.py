from clock import * # Clock Module -- I wrote the script for the framework :)
import Adafruit_CharLCD as LCD #LCD module
# The Code Begins!



lcd_rs        = 23  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 5
lcd_d4        = 6
lcd_d5        = 13
lcd_d6        = 19
lcd_d7        = 26
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2


lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight) #create a LCD object



if __name__ == "__main__":
    result = timer(15) #Returns 0 upon succesful countdown

    if ~(result):
        lcd.clear()
        lcd.message("Time's up!")
