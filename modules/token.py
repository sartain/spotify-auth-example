import json

file_name = 'config.json'

def get_token():
    with open(file_name) as config_file:
        config = json.load(config_file)
    return config['token']

def get_refresh_token():
    with open(file_name) as config_file:
        try:
            config = json.load(config_file)
            refresh_token = config['refresh_token']
            return refresh_token
        except:
            return None

def get_state():
    with open(file_name) as config_file:
        config = json.load(config_file)
    return config['state']

def store_state(state):
    data = {
        "state": state,
    }
    with open(file_name, 'w') as file:
        json.dump(data, file)

def store_tokens(token, refresh_token):
    data = {
        "token": token,
        "refresh_token": refresh_token,
    }
    with open(file_name, 'w') as file:
        json.dump(data, file)