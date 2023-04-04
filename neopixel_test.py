from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms
from random import *

pin = Pin(13, Pin.OUT) # set GPIO13 to output to drive neopixels
np = NeoPixel(pin, 8)  # create NeoPixel driver on GPIO0 for 8 pixels

while True:
    for x in range(8):
        np[x] = (randint(0, 10), randint(0, 10), randint(0, 10)) #keeping the  brightness low
    
    np.write()
    sleep_ms(15)