"""
Using the standard implementation of micropython on ESP32, only the ADC1 GPIOs
can be used for ADC. These pins are GPIO 36, 39, 34, 35, 32, 33.

"""

from machine import ADC, Pin, Timer

x = ADC(Pin(34))
y = ADC(Pin(32))
z = ADC(Pin(35))

x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)
z.atten(ADC.ATTN_11DB)

def adxl335_sensor_isr(event):
    x_value = x.read()
    y_value = y.read()
    z_value = z.read()
    
    print("x: ", x_value, "y: ", y_value, "z: ", z_value)
    
blink_timer = Timer(1)
blink_timer.init(period = 50, mode = Timer.PERIODIC, callback = adxl335_sensor_isr)
    