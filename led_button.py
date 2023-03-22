from machine import Pin
from utime import sleep_ms, ticks_ms

led = Pin(2, Pin.OUT)
button_pin4 = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    if button_pin4.value() == 0:
        led.on()
        print("Button pressed at ", ticks_ms())
        sleep_ms(10)
    else:
        led.off()