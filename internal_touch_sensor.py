from machine import Pin, TouchPad
from time import sleep_ms

t = TouchPad(Pin(15))

while True:
    print(t.read())
    sleep_ms(50)
