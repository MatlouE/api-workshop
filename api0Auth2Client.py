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

    def get_access_token(self):
        'retrieve access token usng client credentials grant'
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        response = requests.post(self.token_url, data=data)
        if response.status_code == 200: 
            token_data = response.json()
            self.access_token = token_data.get('access_token')
            self.refresh_token = token_data.get('refresh_token')
            return self.access_token 
        else:
            raise exception(f'failed to get token: {response.text}')

    def make_authenticated_request(self, url, method=G='GET', **kwargs)
        'Make an authenticated api request'
        if not self.access_token:
            self.get_access_token()

        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f'Bearer {self.access_token}'

        response = requests.request(method, url, headers = headers, **kwargs) 

        #if token is expired, refresh and retry
        if response.status_code == 401 :
            self.get_access_token =()
            headers['Authorization'] = f'bearer {self.access_token}'
            response = requests.request(method, url, headers=headers, **kwargs)

        return response

0auth_client = 0Auth2Client(
    client_id ='your_client_id',
    client_secret = 'your_client_secret',
    token_url = 'https://auth.example.com/auth/token'
)

response = 0auth_client.make_authenticated_request()