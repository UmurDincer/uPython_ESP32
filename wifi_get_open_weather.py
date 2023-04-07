import network
import urequests as requests
import ujson as json

with open("/wifi_settings_open_weather.json") as credentials_json:
    settings = json.loads(credentials_json.read())
    
headers = {"Content-Type" : "application/json"}

url = "https://api.openweathermap.org/data/2.5/weather?id=739549&units=metric&appid=" + settings["open_weather_key"]

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
    print("My IP address: ", wlan.ifconfig()[0])
else:
    print("Not Connected!")
    
response = requests.get(url)
print("Raw Response: ", response)
weather_back = json.loads(response.content)

print("---------------------------------------")

for x in weather_back['weather']:
    print('The weather in %s is %s with %s.' % (weather_back["name"], x['main'], x['description']))

print('Wind is %.2f meter/sec at %s degrees.' % (weather_back['wind']['speed'], weather_back['wind']['deg']))
print('Pressure at sea level is %s hPa.' % weather_back['main']['pressure'])
print('Current conditions: Humidity %s%%, temp min %.2f°C, temp max %.2f°C.' % (weather_back['main']['humidity'], weather_back['main']['temp_min'], weather_back['main']['temp_max']))
print('Feels like %.2f°C.' % weather_back['main']['feels_like'])

print("---------------------------------------")


    