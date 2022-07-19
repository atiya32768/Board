from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
#oled display width & height
WIDTH=128  
HEIGHT=32
# To start the an I2C port we use this line
i2c= I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

#Display device address

print("I2C Address       : " + hex(i2c.scan()[0].upper()))
# Using the i2c.scan() function we can see if we have an I2C device connected
print("I2C Configuration: " + str(i2c))

oled=SSD1306_I2C(WIDTH, HEIGHT, i2c)

#clear the oled display in case it has junk in it
oled.fill(0) 

#Add some text
oled.text("ELECTRONOOBS", 5, 8)
oled.text("2021", 5, 18)

#Finally update the oled displat so the image & text is displayed
oled.show()
