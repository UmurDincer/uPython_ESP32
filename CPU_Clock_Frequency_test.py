import machine
from time import sleep

while True:
    machine.freq(240000000) #47mA consumption
    print(machine.freq())
    sleep(5)
    
    machine.freq(80000000) #31mA consumption
    print(machine.freq())
    sleep(5)
    
    machine.freq(40000000) #22mA consumption
    print(machine.freq())
    sleep(5)