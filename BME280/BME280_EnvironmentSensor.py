from machine import SoftI2C, Pin, Timer
import BME280_Float as bme280

i2c = SoftI2C(scl = Pin(22), sda = Pin(4), freq = 400000)

bme = bme280.BME280(  i2c = i2c,
                      mode = bme280.BME280_0SAMPLE_8,
                      address = bme280.BME280_I2CADDR )

def read_sensor_isr(event):
    print(bme.values)
    print("")
    print("Temp: ", bme.values[0], ", Pressure: ", bme.values[1], ", Humidity: ", bme.values[2])
    
blink_timer = Timer(1)
blink_timer.init(period = 1000, mode = Timer.PERIODOC, callback = read_sensor_isr)