from machine import Pin, Timer

led = Pin(2, Pin.OUT) # create output on GPIO2

def blink_isr(event):
    if led.value() == False:
        led.on()
    else:
        led.off()
        
blink_timer = Timer(1)
blink_timer.init(period = 500, mode = Timer.PERIODIC, callback = blink_isr)
    
