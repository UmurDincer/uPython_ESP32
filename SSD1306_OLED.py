from machine import Pin, SoftI2C
import SSD1306
from time import sleep
 
i2c = SoftI2C(scl = Pin(25), sda = Pin(26), freq = 400000)
 
oled_width = 128
oled_height = 64
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    oled.fill(0)
    oled.text('Welcome', 0, 0)
    oled.text('OLED Display', 0, 10)
    oled.text('Line 3', 0, 20)
    oled.text('Line 4', 0, 30)
    oled.show()
    sleep(1)
    oled.fill(1)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.show()
    sleep(1)
    oled.line(0, 0, 110, 50, 1)
    oled.show()
    sleep(1)