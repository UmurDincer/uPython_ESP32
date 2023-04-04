from machine import Pin, PWM
from hc_sr04 import HCSR04
from utime import sleep

led_pwm = PWM(Pin(2))
sensor = HCSR04(trigger_pin = 16, echo_pin = 17)

def led_brightness_control():
    distance = sensor.distance_cm()
    print('Distance: ', distance, 'cm')
    brightness_value = 1023 * (distance / 250) #max 250 cm can be measured
    print('Brightness: ', brightness_value)
    led_pwm.duty(int(brightness_value))

while True:
    led_brightness_control()
    sleep(0.5)