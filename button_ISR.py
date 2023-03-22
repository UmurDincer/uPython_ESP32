from machine import Pin, disable_irq, enable_irq
from time import sleep_ms

led = Pin(2, Pin.OUT)
button_pin4 = Pin(4, Pin.IN, Pin.PULL_UP)
button_pressed = False
press_counter = 0

def button_pressed_isr(pin):
    state = disable_irq()
    global button_pressed
    global button_pin
    global press_counter
    
    button_pressed = True
    button_pin = pin
    press_counter = press_counter + 1
    enable_irq(state)
    
button_pin4.irq(trigger = Pin.IRQ_FALLING, handler = button_pressed_isr)

while True:
    if button_pressed == True:
        button_pressed = False
        led.on()
        print("Button pressed at", button_pin)
        print("Press Counter: ", press_counter)
        press_counter = 0
        sleep_ms(500)
    else:
        led.off()
        
    
    
    