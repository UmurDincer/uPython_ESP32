import esp32
from time import sleep

while True:
    print("Raw temperature in Fahrenheit: ", esp32.raw_temperature(), "F")
    celcius =(esp32.raw_temperature() - 32) / 1.8 # conversion from Fahrenheit to Celcius
    print("Raw temperature in Celcius: ", celcius, "°C")
    sleep(1)