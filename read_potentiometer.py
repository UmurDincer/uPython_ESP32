"""
By default, ADC values are 12 bits, therefore they range from 0 to 4095.
By default, PWM values are 10 bits, therefore they range from 0 to 1023
**Scale ADC value to the PWM range to correctly control the LED, so divide
1023/4095 = 0.25, and multiply actual ADC value by 0.25
"""

from machine import ADC, Pin, PWM
from time import sleep

pwm = PWM(Pin(2))
adc = ADC(Pin(34))			

adc.atten(ADC.ATTN_11DB)	#full range: 3.3V

while True:
    pot_value = adc.read()
    pwm_value = int(pot_value * 0.25)
    print("pot: ", pot_value, ", pwm: ", pwm_value)
    pwm.duty(pwm_value)
    sleep(0.1)