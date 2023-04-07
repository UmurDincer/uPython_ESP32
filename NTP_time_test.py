import network, usys
import ujson as json
import ntptime
import utime
from machine import RTC
from time import sleep

week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

with open("/wifi_settings_test.json") as credentials_json:
    settings = json.loads(credentials_json.read())
    
def do_connect():
    wlan.active(True) #activate the interface 
    if not wlan.isconnected(): 
        print('connecting to network...')
        wlan.connect(settings["wifi_name"], settings["password"])
        
        if not wlan.isconnected():
            print("Cannot connect to network with given credentials.")
            usys.exit(0)
    print('network config: ', wlan.ifconfig())

wlan = network.WLAN(network.STA_IF)

do_connect()

ntptime.host = "0.tr.pool.ntp.org" # find your local NTP server here:https://www.ntppool.org/

rtc = RTC()

if wlan.isconnected() == True:
    try:
        print("Local time before synchronization: %s", %str(utime.localtime()))
        ntptime.settime()
        print("Local time after synchronization: %s", %str(utime.localtime()))
    except:
        print("Error syncronizing time!")
        usys.exit()
else:
    print("Not connected")
    usys.exit()
    
current_timedate_utc = utime.localtime()
current_timedate_local = utime.mktime(current_timedate_utc)
current_timedate_local += 3 * 3600 #turkey is 3 hours ahead of UTC.
print("Local Time: ", utime.localyime(current_timedate_local))

utc_date_time = rtc.datetime()

print()
print("UTC time: ", utc_date_time)
print("UTC date (year, month, day, day of week): ", utc_date_time[0], "/",
                                                       utc_date_time[1], "/",
                                                       utc_date_time[2], "|",
                                                       utc_week_day[date_time[3]])
print("UTC time (hour:minute:second): ",           utc_date_time[4], ":",
                                                       utc_date_time[5], ":",
                                                       utc_date_time[6])

print("Local time:, ", utime.localtime(current_time_date_local))
print("Local date (year, month, day, day of week): ",   utime.localtime(current_time_date_local)[0],
                                                        "/",
                                                        utime.localtime(current_time_date_local)[1],
                                                        "/",
                                                        utime.localtime(current_time_date_local)[2],
                                                        " | ",
                                                        utime.localtime(current_time_date_local)[3])
print("Local time (hour:minute:second): ",   utime.localtime(current_time_date_local)[3],
                                              ":",
                                              utime.localtime(current_time_date_local)[4],
                                              ":",
                                              utime.localtime(current_time_date_local)[5])                                


while True:
    date_time = rtc.datetime()
    print(date_time) # print date and time
    print("Current date (year, month, day, day of week): ",  date_time[0],
                                                              "/",
                                                              date_time[1],
                                                              "/",
                                                              date_time[2],
                                                              " | ",
                                                              date_time[3])
    print("Current time (hour:minute:second): ",   date_time[4],
                                                  ":",
                                                  date_time[5],
                                                  ":",
                                                  date_time[6])                                
    sleep(1)    
