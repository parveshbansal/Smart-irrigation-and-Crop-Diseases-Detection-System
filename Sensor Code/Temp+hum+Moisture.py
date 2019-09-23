import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        temp=result.tempetature
	print("Temprature: %d F" % ((result.temperature *9/5)+32))
        print("Humidity: %d %%" % result.humidity)
        humidity=result.humidity


        feed = requests.get('https://api.thingspeak.com/channels/641798/fields/1.json?api_key=T49ZYG8UVGE6L0D7&results=1')
        soil_moisture_json = feed.json()
        soil_moisture = soil_moisture_json["feeds"][0]["field1"]
        #print(soil_moisture)


        requests.post("aws link?temperature="+temperature+"&hmidity="+humidity+"&soil_moisture="+soil_moisture)
        time.sleep(20);
