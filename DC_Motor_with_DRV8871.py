from machine import Pin, PWM
from utime import sleep

in2 = PWM(Pin(2)) #speed
in1 = Pin(21, Pin.OUT) #direction

in2.freq(500) # set frequency 500. Default freq is 1000

while True:
   #forward. in2: 1023 --> Slower, 0 --> Faster
    in1.on()
    print("Forward")
    in2.duty(0)    # Fast
    sleep(1)
    in2.duty(100)  # Slow
    sleep(1)
    in2.duty(200)  # Slower
    sleep(1)
    in2.duty(300)  # Slower 
    sleep(1)
    in2.duty(1023) #Stop
    sleep(1)
    
    #Reverse
    #in2: 0 --> Slower, 1023 --> Faster
    in1.off()
    print("Reverse")
    in2.duty(900)  #Fast
    sleep(1)        
    in2.duty(600)  #Slow
    sleep(1)
    in2.duty(300)  #Slower
    sleep(1)
    in2.duty(0)    #Stop
    sleep(1)
    