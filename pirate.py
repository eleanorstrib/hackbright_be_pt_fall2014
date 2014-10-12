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

import random


# Write a function to ask what style of drink a customer likes.

# The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary.
# The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean (True or False) value.
# If the customer answers y or yes to the question then the value should be True, otherwise the value should be False.
# The function should return the new dictionary.

for flavor, question in questions.iteritems():
	
def ask_taste():
	preferences = {}
	questions_list = list(questions.values())

	for taste in questions:
		print (random.choice(questions_list))
		question_response = raw_input()
		if question_response == 'yes' or 'y':
			preferences[questions.key(random.choice(questions_list))] = True
		else:
			preferences[questions.key(random.choice(questions_list))] = False

	return preferences
ask_taste()






# def main(): 
# 	your_drink = []
# 	print "How do ye like yer poison? Strong, salty, bitter, sweet or fruity?",
# 	question_response = raw_input()

# 	print 'Ye like it ' + question_response + ', eh?  Will some' + random.choice(ingredients.question_response) +' be agreeable with ye?'
# 	ingredient_response1 = raw_input()

# 	if ingredient_response1 == 'yes':
# 		ingredient_response1.append(your_drink)
# 		print 'Got it, ' + ingredient_response1 + '.  Would ye care for some '+ random.choice(ingredients.question_response) + '?'
# 	else:
# 		print 'No ' + ingredient_response1 +'eh? Big mistake, it puts hair on yer chest.  So will ye