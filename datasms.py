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
	else:
		print 'Oops - there was an error'

(city, state) = get_place()
todays_forecast = forecast(city,state)
greeting = "The forecast for {} tomorrow: {}".format(get_place(),todays_forecast)
number = 4157301468

from twilio.rest import TwilioRestClient
account_sid = "ACf2a9b8598b66f57b7728da6d2d7eee92"
auth_token = "ccbfa40bb030e0ce11b6ff6a5f8c0e6e"
client = TwilioRestClient(account_sid, auth_token)

def text_me(number,content):
	message = client.messages.create(to=number, from_="+16507630949",
                                     body=content)
	if number > 1111111 and len(greeting) > 1:
		print 'It worked!'
	else:
		print 'Oops, something went wrong!'

text_me(number,greeting)

