import time
import digitalio
import board
import usb_hid
from adafruit_hid.keybpard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP01
#USB hiv interface 
keyboard=Keyboard(usb_hid.devices)



keyboard=Keyboard()
btn1=digitalio.DigitalInOut(btn1_pin)
#when we press a button we are getting an input
btn1.direction=digitalio.Direction.INPUT
#The pull: UP or DOWN ; 0 or 1; True or False - UP means the GPIO has a value 1, means it has voltage going throught that GPIO
#Down- The pin is on a grounded state and we have to send power to it to switch it from 0 to 1
btn1.pull=digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("button 1 : pressed")
        keyboard.press(Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.A)

    time.sleep(0.1)

