import requests
import json
import time
import sys
import pyttsx3

city = ''
URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=06b551ac9240da779607a8f1603d8999&units=metric'



def get_weather():
	full = URL.format(city)
	repsonse = requests.get(full)

	#get and write to the file
	with open('weatherdata.json', "w") as json_w:
		repsonse = requests.get(full)
		data = json.dump(repsonse.json(), json_w)

	#read the file
	with open("weatherdata.json") as json_r:
		data = json.load(json_r)
		print(data['main']['temp'])

	return data['main']['temp']

