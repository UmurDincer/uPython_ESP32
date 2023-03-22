from machine import Pin, PWM
from time import sleep_ms

pwm_0 = PWM(Pin(2))  #all pin supported PWM

while True:
    for duty_cycle in range(0, 1023, 5):
        pwm_0.duty(duty_cycle)
        sleep_ms(10)
    
    for duty_cycle in range(1023, 0, -5):
        pwm_0.duty(duty_cycle)
        sleep_ms(10)
    
