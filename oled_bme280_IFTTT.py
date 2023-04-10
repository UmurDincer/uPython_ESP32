"""
Components
 ----------
  - ESP32
  - 1.3" OLED with the SH1106 controllerm 128x64
  -     GND --> GND
  -     VCC --> 3.3V
  -     SDA --> GPIO 19
  -     SCL --> GPIO 18
  - BME/BMP280 breakout
  -   Vcc to 3.3V
  -   GND to GND
  -   SDA to GPIO 19 (HW SDA ID 0)
  -   SCL to GPIO 18 (HW SCL ID 0) 
  - 330Ohm resistor for the LED
  - 5mm LED  
  - Wires
  - Breadboard
"""
from machine import I2C, Pin, Timer
import SH1106 as sh1106
import BME280_Float as bme280
from time import sleep
import network, sys
import ujson as json
import ntptime
import utime
from machine import RTC
import urequests as requests

internet_time_acquired = False
iftt_notification_counter = 0 #use this counter to prevent too many IFTTT notifications
                              #A notification will be sent at most once every 10 minutes
iftt_notification_interval_sec = 60
iftt_notification_sent = False

led = Pin(2, Pin.OUT)

i2c = I2C(0)

display= sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)

bme = bme280.BME280(i2c = i2c, mode = bme280.BME280_0SAMPLE_8, address = bme280.BME280_I2CADDR) #works okay with explicit settings

with open("/wifi_settings_ifttt.json") as credentials_json:
    settings = json.loads(credentials_json.read())

headers = {"Content-Type" : "application/json"}

url = "https://maker.ifttt.com/trigger/uPython/with/key/" + settings["ifttt_key"]

wlan = network.WLAN(network.STA_IF) # this will create a station interface object.
                                    #to create an access point, use AP_IF


def do_connect():
    wlan.active(True) #activate the interface 
    if not wlan.isconnected(): 
        print('connecting to network ', settings["wifi_name"])
        wlan.active(True)
        sleep(0.5)
        wlan.connect(settings["wifi_name"], settings["password"])
        
        sleep(0.5)
        print("Connected to Wi-Fi: ", wlan.isconnected())
        if not wlan.isconnected():
            print("Cannot connect to network with given credentials.")
            return 1
    print('network config: ', wlan.ifconfig())

def do_disconnect():
    wlan.active(False)
    print("Wi-Fi disconnected.")
    
def draw_static_screen():
    display.text('Temp: ', 5, 5, 1)
    display.text('Humi: ', 5, 15, 1)
    display.text('Pres: ', 5, 25, 1)
    display.text('Time: ', 5, 35, 1)
    display.text('Date: ', 5, 45, 1)
    display.text('Starting... ', 5, 55, 1)
    
def clear_dynamic_screen():
    display.fill_rect(45, 0, 83, 64, 0)
    display.fill_rect(0, 55, 128, 10, 0)
    
def draw_dynamic_screen(temp="N/A", humi="N/A", press="N/A"):
    local_time = "N/A"
    local_date = "N/A"
    week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print("Internet time acquired", internet_time_acquired)
    if(internet_time_acquired == True):
        rtc = RTC()
        date_time = rtc.datetime()
        print(date_time)
        print("Curren date (year, month, day, day of week): ", date_time[0], "/",
                                                           date_time[1], "/",
                                                           date_time[2], "|",
                                                           week_day[date_time[3]])
        print("Current time (hour:minute:second): ",       date_time[4], ":",
                                                           date_time[5], ":",
                                                           date_time[6])
        local_time = str(date_time[4]) + ":" + str(date_time[5]) + ":" + str(date_time[6])
        local_date = str(date_time[0]) + "/" + str(date_time[1]) + "/" + str(date_time[2])
        
    print(date_time)
    
    display.text(temp, 5, 5, 1)
    display.text(humi, 5, 15, 1)
    display.text(press, 5, 25, 1)
    display.text(local_time, 5, 35, 1)
    display.text(local_date, 5, 45, 1)
    print("iftt_notification_sent: ", iftt_notification_sent)
    print("iftt_notification_counter: ", iftt_notification_counter)
    display.text('IFTTT in', 5, 55, 1)
    display.text(str(iftt_notification_interval_sec-iftt_notification_counter) + "s", 80, 55, 1)# this will show count down

def get_internet_time():
    global internet_time_acquired
    
    print("GET TIME Connceted? ", wlan.isconnected())
    rtc = RTC()
    
    try:
        print("Utime time before synchronization: %s" %str(utime.localtime()))
        ntptime.settime()
        print("Utime/UTC time after synchronization: %s" %str(utime.localtime()))
        current_timedate_utc = utime.localtime()
        current_time_date_local = utime.mktime(current_timedate_utc)
        current_time_date_local += 3 * 3600 #turkey is 3 hours ahead of UTC.
        print("Local Time: ", utime.localtime(current_time_date_local))
          
        rtc.datetime( (utime.localtime(current_time_date_local)[0],
                       utime.localtime(current_time_date_local)[1],
                       utime.localtime(current_time_date_local)[2],
                       0,
                       utime.localtime(current_time_date_local)[3],
                       utime.localtime(current_time_date_local)[4],
                       utime.localtime(current_time_date_local)[5],
                       0))
        
        internet_time_acquired = True
        print("Internet time received: ", internet_time_acquired)
    except:
        print("Error syncing time")

def post_to_itfff(temp="N/A", humi="N/A", press="N/A"):
    global iftt_notification_counter
    global iftt_notification_sent
    
    print("post_to_itff, itff_notification_counter: ", iftt_notification_counter)
    if (iftt_notification_counter == 0):
        data = { "value1" : temp, "value2" : humi, "value3" : press }
        
        print("Sending POST request to IFTTT... with this content: ", data)
        do_connect()
        response = requests.post(url, headers = headers, data = json.dumps(data))
        ifttt_back = response.content
        print("Response from IFTTT: ", ifttt_back)
        iftt_notification_sent = True
        print("iftt_notification_sent: ", iftt_notification_sent)
        print("iftt_notification_counter: ", iftt_notification_counter)
        iftt_notification_counter = iftt_notification_counter + 1
    else:
        print("No notification sent.")
        iftt_notification_sent = False
        print("iftt_notification_sent: ", iftt_notification_sent)
        print("iftt_notification_counter: ", iftt_notification_counter)
        iftt_notification_counter = iftt_notification_counter + 1
        if (iftt_notification_counter == iftt_notification_interval_sec):
            iftt_notification_counter = 0
    do_disconnect()
        
def timer_isr(event):
    led.on()
    if not wlan.isconnected():
        do_connect()
    
    #print(bme.values)
    temperature, pressure, humidity = bme.values # multiple assignment from tuple to variables
    print("")
    print("Temp: ", temperature, ", Pressure: ", pressure, ", Humidity: ", humidity)
    
    # Get numerical value for temperature and generate an IFTTT notification if
    # it is over the threshold
    # Temperature is returned as "26.46C" by the BME280 library.
    # Use the Python substring operator with cast to float to get the numerical version.
    temperature_float = float(temperature[0:5])
    if (temperature_float > 25):
        post_to_ifttt(temp=temperature,humi=humidity,press=pressure)
    
    clear_dynamic_screen()
    draw_dynamic_screen(temp=temperature,humi=humidity,press=pressure)
    display.show()
    led.off()
    
# Execution starts here

display.init_display()
display.sleep(False)
display.rotate(True)

draw_static_screen()

display.show()

do_connect()

get_internet_time()
 
do_disconnect()

timer_isr(1)    # Used for testing
do_disconnect()       # Used for testing