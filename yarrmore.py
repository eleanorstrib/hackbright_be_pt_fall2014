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

inventory = {
	"glug o' rum": 3,
	"slug o' whisky": 3,
	"splash of gin": 3,
	"olive on a stick": 3,
	"salt-dusted rim": 3,
	"rasher o' bacon": 3,
	"shake of bitters": 3,
	"splash of tonic": 3,
	"twist o' lemon peel": 3,
	"sugar cube": 3,
	"spoonful of honey": 3,
	"splash o' cola": 3,
	"slice of orange": 3,
	"dash of cassis": 3,
	"cherry on top": 3
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

# def increment_inventory():
# 	for individual_ingredient, quantity in increment_inventory:
# 		if individual_ingredient in drink:
# 			quantity -= 1
# 		else:
# 			continue

# yer_drink(preference)
drink_name_adjective = ['Lazy', 'Shifty', 'Crusty', 'Sleepy', 'Winsome', 'Crazy', 'Wired', 'Smooth']
drink_name_noun = ['Suitor', 'Sailor', 'Traitor', 'Lady', 'Syncophant', 'Instigator', 'Criminal', 'Daisy']
drink_name = []
def yer_drink_name():
	drink_name.append(random.choice(drink_name_adjective))
	drink_name.append(random.choice(drink_name_noun))
	return drink_name

def main():
	order = yer_preference()
	components = yer_drink(preference)
	name = yer_drink_name()
	# stock = increment_inventory()
	print "Arr, yer drink I'll be concocting..."
	print "Here ye go, this be a " + " " + drink_name[-2] + " " + drink_name[-1]
	print "This will put some hair on yer chest, it's:"
	for ingredients in drink:
		print "{}".format(ingredients)

		# if inventory[x] <= 3:
		# 	print "Yarr, I be running low on " + inventory[x]
	print "Hope ye enjoyed yer drink, matey.  Would ye like another?"
	have_another = raw_input().lower()
	if have_another == 'yes' or have_another == 'y':
		main()
	else: 
		print "Goodnight to ye then"

if __name__=="__main__":
	main()
