from machine import Pin, Timer # In order to use pins we use e we use pin, use timer to create delay

led = Pin(25,Pin.OUT) # define LED as a pin for the GPIO25 and define it as an output
LED_state=True    #create a boolean LED state that is equal to true
tim=Timer()#create a Timer to blink each one hertz, so it will blink each one secound

#each time the timer ticks we will invert the LED state
#true is LED on and false is the LED off
def tick(timer):
    global led, LED_state
    LED_state=not LED_state
    led.value(LED_state)

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick )

#save this to Rasberry Pi Pico and rename main.py