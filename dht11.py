from machine import Pin, Timer
import dht

dht11 = dht.DHT11(Pin(4))

def take_measurement_isr(event):
    dht11.measure()
    print("Temperature: ", dht11.temperature(),"°C, Humidity: ", dht11.humidity(), "%")
    
dht_timer = Timer(1)
dht_timer.init(period = 5000, mode = Timer.PERIODIC, callback = take_measurement_isr)