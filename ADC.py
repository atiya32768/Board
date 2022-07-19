#use 12-bit ADC
#how to read analog values with pico
import machine
import utime
#define adc input connected at pin 28
adc_read=machine.ADC(28)

while True:
    reading = adc_read.read_u16()
    print("ADC: ", reading)
    utime.sleep(0.1)