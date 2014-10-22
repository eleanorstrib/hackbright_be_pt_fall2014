#write a function that returns the temperature
# import requests
# r = requests.get('http://api.wunderground.com/api/d1830ed0485f4e6a/conditions/q/CA/San_Francisco.json')

# def weather():
# 	j = r.json()
# 	temperature = j['current_observation']['temperature_string']
# 	return temperature

# weather()

# #write a function that takes city and state as parameters
# def weather(state,city):
# 	r = requests.get('http://api.wunderground.com/api/d1830ed0485f4e6a/conditions/q/'+ state +'/' + city + '.json')
# 	j = r.json()
# 	temperature = j['current_observation']['city']['state']['temperature_string']
# 	print temperature

# weather('CA', 'San Francisco')

import requests

def weather(state,city):
	api_url = 'http://api.wunderground.com/api/d1830ed0485f4e6a/conditions/q'
	city = city.replace(" ", "_")
	r = requests.get('{}/{}/{}.json'.format(api_url, state, city))
	j = r.json()
	print r.status_code
	print j
	if r.status_code == 200:
		temperature = j['current_observation']['temperature_string']
		return temperature
		print temperature
	else:
		print 'Oops - there was an error'
weather('CA', 'San Francisco')


def forecast(state,city):
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
forecast('CA', 'San Francisco')



