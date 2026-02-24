import requests
from requests.auth import HTTPBasicAuth
import json

class 0Auth2Client:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.access_token = None 
        self.refresh_token = None