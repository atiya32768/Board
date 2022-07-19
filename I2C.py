from machine import Pin, I2C

# To start the an I2C port we use this line
i2c= I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

#Display device address
print("I2C Address       : " + hex(i2c.scan()[0].upper()))
# Using the i2c.scan() function we can see if we have an I2C device connected