from machine import Pin, Timer

r = Pin(2, Pin.OUT)
g = Pin(0, Pin.OUT)
b = Pin(4, Pin.OUT)

def red_isr(event):
    if r.value() == False:
        r.on()
    else:
        r.off()

def green_isr(event):
    if g.value() == False:
        g.on()
    else:
        g.off()
        
def blue_isr(event):
    if b.value() == False:
        b.on()
    else:
        b.off()
        
timer_red = Timer(0)
timer_red.init(period = 250, mode = Timer.PERIODIC, callback = red_isr)

timer_green = Timer(1)
timer_green.init(period = 350, mode = Timer.PERIODIC, callback = green_isr)

timer_blue = Timer(2)
timer_blue.init(period = 450, mode = Timer.PERIODIC, callback = blue_isr)
