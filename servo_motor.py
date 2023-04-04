from machine import Pin, PWM
from time import sleep # used for delay function

servo_pin = Pin(2, Pin.OUT)
pwm = PWM(servo_pin)

pwm.freq(50) # set the pulse every 20ms
pwm.duty(0)  # set initial duty to 0 to turn off the pulse

#Create map function for mapping 0 to 180 degree to 20 to 120 pwm duty value
def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#Function for turning the servo accoırding to input angle
def servo(pwm_pin, angle):
    pwm_pin.duty(map(angle, 0, 180, 20, 120))
    
#To rotate the servo to 20 degrees:
servo(pwm, 20)
sleep(1)

#To rotate the servo to 90 degrees:
servo(pwm, 90)
sleep(1)

#To rotate the servo to 170 degrees:
servo(pwm, 170)
sleep(1)

while True:
# rotate servo motor from 20 degree to 170 degree incrementing by 10 degrees
    for i in range(20, 170, 10):
        print("20 to 170, step ", i)
        servo(pwm, i)
        sleep(0.5)
        
# rotate the servo motor reverse direction (from 170 to 20)
    for i in range(170, 20, -10):
        print("170 to 20, step ", i)
        servo(pwm, i)
        sleep(0.5)
    