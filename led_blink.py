from machine import Pin
from utime import sleep

led = Pin(2, Pin.OUT) #create output pin on GPIO2

while True:
    led.on()	#set pin to "on" (high) level
    sleep(0.5)
    led.off()   #set pin to "off" (low) level
    sleep(0.5)