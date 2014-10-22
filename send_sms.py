# # Download the twilio-python library from http://twilio.com/docs/libraries
# from twilio.rest import TwilioRestClient
# import requests
 
# # Find these values at https://twilio.com/user/account
# account_sid = "ACf2a9b8598b66f57b7728da6d2d7eee92"
# auth_token = "ccbfa40bb030e0ce11b6ff6a5f8c0e6e"
# client = TwilioRestClient(account_sid, auth_token)
 
# message = client.messages.create(to="+1.415.730.1468", from_="+1650-7630949",
#                                      body="I sent this with PYTHON -- and put in periods!")


#make this into a function

from twilio.rest import TwilioRestClient
account_sid = "ACf2a9b8598b66f57b7728da6d2d7eee92"
auth_token = "ccbfa40bb030e0ce11b6ff6a5f8c0e6e"
client = TwilioRestClient(account_sid, auth_token)

def text_me(number,greeting):
	message = client.messages.create(to=number, from_="+16507630949",
                                     body=greeting)
	if number > 1111111 and len(greeting) > 1:
		print 'It worked!'
	else:
		print 'Oops, something went wrong!'

text_me(4157301468,"This is a function -- try 10!")





	
