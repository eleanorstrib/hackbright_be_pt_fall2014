questions = {
	"strong": "Do ye like yer drinks strong, eh?",
	"salty": "Do ye like it with a wee salty tang?",
	"bitter": "Arrr ye a lubber what likes it bitter?",
	"sweet": "Would ye like some sweet with yer poison, yarr?",
	"fruity": "Are ye one for a fruity finish, matey?"
}

ingredients = {
	"strong": ["glug o' rum", "slug o' whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher o' bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist o' lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "splash o' cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

preference = {}

import random

def yer_preference():
	for key, value in questions.items():
		for x in range (0, 6):
			print value
			user_preference = raw_input().lower()
			if user_preference == 'yes' or user_preference == 'y':
				preference[key] = True
				break
			else: 
				preference[key] = False
				break
	# return preference
	return preference

# yer_preference()
drink = []
def yer_drink(preference):

	for taste, ok in preference.iteritems():
		if ok:
			drink.append(random.choice(ingredients[taste]))
		else:
			continue 

	return drink

# yer_drink(preference)


def main():
	order = yer_preference()
	components = yer_drink(preference)
	print "Arr, yer drink I'll be concocting..."
	print "This will put some hair on yer chest, it's:"
	for ingredients in drink:
		print"{}".format(ingredients)


if __name__=="__main__":
	main()
