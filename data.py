import random

place = ('San Francisco', 'CA'), ('Boston', 'MA'), ('Cambridge', 'CA'), ('Brisbane', 'CA'), ('Rochester', 'NY'), ('Toronto', 'ON')

def get_place():
	return random.choice(place)

import requests
def forecast(city,state):
	api_url = 'http://api.wunderground.com/api/d1830ed0485f4e6a/forecast/q'
	city = city.replace(" ", "_")
	r = requests.get('{}/{}/{}.json'.format(api_url, state, city))
	j = r.json()
	print r.status_code
	if r.status_code == 200:
		forecast_temp = j['forecast']['txt_forecast']['forecastday'][4]['fcttext']
		return forecast_temp
		print forecast_temp
	else:
		print 'Oops - there was an error'

(city, state) = get_place()
todays_forecast = forecast(city,state)
print get_place()
print todays_forecast



# there needs to a line of space		
# get_weather_place = forecast(city,state)
# print get_weather_place