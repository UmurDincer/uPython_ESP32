import network, usys
import urequests
import ujson as json
 
with open("/wifi_settings_test.json") as credentials_json: #this allows to open and read
         settings = json.loads(credentials_json.read())     #an existing file
         
url = "https://firebasestorage.googleapis.com/v0/b/esp32-bc5c6.appspot.com/o/hello.txt?alt=media&token=e5e13887-1f5c-4f5c-af86-ee8539411feb" #url to fetch

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
    response = urequests.get(url)
    print("Fetching content from ", url, ":")
    print("----------------")
    print(response.text)
    print("----------------")
else:
    print("Not Connected!")
    print("----------------")