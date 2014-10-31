# pip install requests
# pip install requests-oauthlib

# API secrets. NEVER share these with anyone!

# import twitter_oauth_testeleanor
CLIENT_KEY = "vfGC5EWr1k2R8K1fHgAckJ0Gx"
CLIENT_SECRET = "j1338xMxc9dpQVom59mn3qkLVSKdAL02KJaZHNiW7JEyEWluYP"


API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TWEET_URL = API_URL + "/1.1/statuses/update.json"
MENTION_URL = API_URL + "/1.1/statuses/mentions_timeline.json"
SEARCH_URL = API_URL + "/1.1/search/tweets.json"



import urlparse
import json
import requests
from requests_oauthlib import OAuth1


def get_request_token():
    """ Get a token allowing us to request user authorization """
    oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
    response = requests.post(REQUEST_TOKEN_URL,
                             auth=oauth)
    credentials = urlparse.parse_qs(response.content)

    request_token = credentials.get("oauth_token")[0]
    request_secret = credentials.get("oauth_token_secret")[0]
    return request_token, request_secret


def get_access_token(request_token, request_secret, verifier):
    """"
    Get a token which will allow us to make requests to the API
    """
    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=request_token,
                   resource_owner_secret=request_secret,
                   verifier=verifier)

    response = requests.post(ACCESS_TOKEN_URL, auth=oauth)
    credentials = urlparse.parse_qs(response.content)
    access_token = credentials.get('oauth_token')[0]
    access_secret = credentials.get('oauth_token_secret')[0]
    return access_token, access_secret


def get_user_authorization(request_token):
    """
    Redirect the user to authorize the client, and get them to give us the
    verification code.
    """
    authorize_url = AUTHORIZE_URL
    authorize_url = authorize_url.format(request_token=request_token)
    print 'Please go here and authorize: ' + authorize_url
    return raw_input('Please input the verifier: ')


def store_credentials(access_token, access_secret):
    """ Save our access credentials in a json file """
    with open("access_test.json", "w") as f:
        json.dump({"access_token": access_token,
                   "access_secret": access_secret}, f)


def get_stored_credentials():
    """ Try to retrieve stored access credentials from a json file """
    with open("access_test.json", "r") as f:
        credentials = json.load(f)
        return credentials["access_token"], credentials["access_secret"]


def authorize():
    """ A complete OAuth authentication flow """
    try:
        access_token, access_secret = get_stored_credentials()
    except IOError:
        request_token, request_secret = get_request_token()
        verifier = get_user_authorization(request_token)
        access_token, access_secret = get_access_token(request_token,
                                                       request_secret,
                                                       verifier)
        store_credentials(access_token, access_secret)

    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=access_token,
                   resource_owner_secret=access_secret)
    return oauth

def find_relevant_mentions(handles,words):
    list_handles = {}
    handle =  user['user']
    words = user['text']
    for mention in handles:
        if words == 'Can I get a weather forecast @eleanorstrib?':
            list_handles.append(handle)
            print handle
        else: 
            continue
    return list_handles


def main():
    """ Main function """
    auth = authorize()
    # data = { 'status' : '@{}, forecast is: {}'}.format()

    find_mentions = requests.get(MENTION_URL, auth=auth)
    print json.dumps(find_mentions.json(), indent=4)

    # search_mentions = requests.get(SEARCH_URL, auth=auth)
    # print json.dumps(search_mentions.json(), indent=4)

    # send_weather = requests.post(SEARCH_URL, data=data2, auth=auth)
    # print json.dumps(send_weather.json(), indent=4)


if __name__=="__main__":
    main()




