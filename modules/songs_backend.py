import requests
import random
import string
import base64
from modules.env import get_client_id, get_client_secret, get_redirect_uri
from modules.token import store_state, store_tokens, get_refresh_token, get_state, get_token

#Get random string used to verify the same user is making authorization steps 1&2
def initialize_state():
    letters = string.ascii_letters
    state = ''.join(random.choice(letters) for _ in range(16))
    store_state(state)

#Compare state values
def invalid_state(state_to_compare):
    return get_state() != state_to_compare

#Get form values required to make authorization step 1 request
#Scope is a single string based upon the use of the future API requests
def get_auth_params():
    return {
        'client_id': get_client_id(),
        'response_type': 'code',
        'redirect_uri': get_redirect_uri(),
        'state': get_state(),
        'scope': 'user-library-read',
        'show_dialog': 'true'
    }

#Get clientID and clientSecret values encrypted, used for step 1 request
def get_encrypted_credentials():
    client_id = get_client_id()
    client_secret = get_client_secret()
    credentials = f'{client_id}:{client_secret}'
    return base64.b64encode(credentials.encode()).decode()

#Get header values for step 1 and 2 request
def get_auth_headers(encoded_credentials):
    return {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

#Get form values required to make authorization step 2 request
def get_token_params(code):
    return {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': get_redirect_uri(),
    }

#Make the POST request to retrieve and store the tokens in authorization step 2
def request_token(code):
    encoded_credentials = get_encrypted_credentials()
    headers = get_auth_headers(encoded_credentials)
    form_params = get_token_params(code)
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=form_params)
    if response.status_code == 200:
        store_tokens(response.json()['access_token'], response.json()['refresh_token'])
    else:
        return response.json()['error']
    
#Get form values required to make a refresh token request    
def get_refresh_token_params():
    return {
        'grant_type': 'refresh_token',
        'refresh_token': get_refresh_token()
    }

#Make the POST request to retrieve and store refreshed tokens provided a token already exists for the user
def refresh_token():
    if get_refresh_token() != None:
        refresh_token = get_refresh_token()
        encoded_credentials = get_encrypted_credentials()
        headers = get_auth_headers(encoded_credentials)
        form_params = get_refresh_token_params()
        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=form_params)
        if response.status_code == 200:
            store_tokens(response.json()['access_token'], refresh_token)
            return True
    return False

#Get header values for future Spotify API Requests, using token
def get_token_headers():
    return {
        'Authorization': f'Bearer {get_token()}',
    }

#Example GET request using the token
def get_liked_songs():
    headers = get_token_headers()
    response = requests.get('https://api.spotify.com/v1/me/tracks', headers=headers)
    print(response.json())
    return response