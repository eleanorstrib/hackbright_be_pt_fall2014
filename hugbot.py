import random
HUGBOT_NAME = 'henrietta'
hugbot_actions = ['hug','wave','bow']
action_dict = {
	'dance': 'does the cha cha cha.',
	'sing': 'wharbles "la la la".',
	'wave': 'says a happy hello.',
	'hug' :'gives you a big bear hug.',
	'act': 'gives a great rendition of a classic Shakespeare monologue.',
	'cook': 'makes you a casserole.',
	'connect': 'finds you a wifi connection.'
}

def speak(user_input):
	print user_input

# def hug():
# 	speak('**hug**')

# def wave():
# 	speak('**wave**')

# def bow():
# 	speak('**bow**')

def boot():
	# will_she_boot = random.choice([True,False])
	# if will_she_boot:
	# 	speak('initiating.......')
	bot_name = raw_input('what name should the robot use?')
	if bot_name == '':
		return False
	else: 
		speak('hello!  my name is ' + bot_name)
		return bot_name
	# else: 
	# 	speak('uh oh, error, error!')
	# 	return False

def perform_action(verb, bot_name):
	phrase = action_dict.get(verb)
	if verb == 'quit':
		return False
	if phrase == None:
		speak(bot_name + ' does not know how to do that. try something else?')
	else:
		speak(bot_name + " " + phrase)
	return True

def brain():
	boot_ok = boot()
	if boot_ok:
		running = True
		while running:
			action = raw_input('what can i do for you today?')
			running = perform_action(action, boot_ok)
			# if action not in hugbot_actions: 
			# 	speak('could you type that in again? did not understand')
			# 	action = raw_input('what can i do for you today?')
			# if action == 'hug':
			# 	hug()
			# if action == 'wave':
			# 	wave()
			# if action == 'bow':
			# 	bow()
			# if action == 'quit':
			# 	return
	else:
		speak('someone call a bot doctor!')

brain()