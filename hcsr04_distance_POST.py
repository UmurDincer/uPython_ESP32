from machine import Pin, Timer
import network, usys
import urequests as requests
import ujson as json
import random
from hc_sr04 import HCSR04

sensor = HCSR04(trigger_pin = 16, echo_pin = 17)

with open("/hcsr04_settings_dweet.json") as credentials_json:
    settings = json.loads(credentials_json.read())
    
headers = {"Content-Type" : "application/json"}

# https://dweet.io/play/#!/dweets/postDweet_post_1 website is used to POST/GET data 
url = "https://dweet.io:443/dweet/for/" + settings["thing"]

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

if wlan.isconnected() == True:
    print("Connected")
    print("My IP address: ", wlan.ifconfig()[0]) #prints the acquired IP address
else:
    print("Not Connected!")

def post_to_dweet_isr(event):
    
    distance = sensor.distance_cm()
    data = { "distance": distance }
    
    response = requests.post(url, headers = headers, data = json.dumps(data)) #make POST request
    dweet_back = json.loads(response.content)
    print("\nResponse from dweet.io: ", dweet_back)
    print("Created: ", dweet_back["with"]["created"])
    print("Transaction: ", dweet_back["with"]["transaction"])
    print("thing: ", dweet_back["with"]["thing"])
    print("Distance: ", dweet_back["with"]["content"]["distance"])
    
dht_timer = Timer(1)
dht_timer.init(period = 2000, mode = Timer.PERIODIC, callback = post_to_dweet_isr)
    
