#https://maker.ifttt.com/use/cgjjaHo628UVgDOgIfuJGF
from machine import Pin
import network, usys
import urequests as requests
import ujson as json
import dht

dht11 = dht.DHT11(Pin(4))

with open("/wifi_settings_ifttt.json") as credentials_json: #this allows to open and read
         settings = json.loads(credentials_json.read())     #an existing file
         
headers = {"Content-Type" : "application/json"}

url = "https://maker.ifttt.com/trigger/uPython/with/key/" + settings["ifttt_key"]

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
    print("My IP address: ")
    print(wlan.ifconfig()[0]) #prints IP address
else:
    print("Not Connected")
    
dht11.measure()
temp = dht11.temperature()
humi = dht11.humidity()

data = {"value1": temp, "value2": humi}

print("Sending POST request to IFTTT with this content: ", data)
response = requests.post(url, headers = headers, data = json.dumps(data))
ifttt_back = response.content
print("Response from IFTTT: ", ifttt_back)
