from machine import Pin, I2C
import SH1106
from time import sleep_ms

i2c = I2C(1) #hardware i2c

display = SH1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display.init_display()
display.sleep(False)

display.fill(0)
display.text('Testing 1', 20, 25, 1)
display.show()
slep_ms(1000)

display.fill(1)
display.text('Testing 2', 20, 25, 0)
display.show()
slep_ms(1000)


display.rotate(True)
display.show()
sleep_ms(1000)

display.fill(0)
display.fill_rect(61, 30, 5, 5, 1)
display.show()
slep_ms(1000)


for x in range(127):
    display.fill_rect(x, 0, 5, 63, 1)
    diplay.show()
    sleep_ms(10)
    
display.fill(0)

while True:
    for x in range(0, 127, 5):
        display.fill(0)
        display.fill_rect(x, 30, 5, 5, 1)
        display.show()

    for x in range(122, 0, -5)
        display.fill(0)
        display.fill_rect(x, 30, 5, 5, 1)
        display.show()
