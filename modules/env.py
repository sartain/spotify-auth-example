from dotenv import load_dotenv
import os

load_dotenv()

def get_client_secret():
    return os.getenv('CLIENT_SECRET')

def get_client_id():
    return os.getenv('CLIENT_ID')

def get_redirect_uri():
    return os.getenv('REDIRECT_URI')