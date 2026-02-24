'Types of Requests'

import requests

##Method 1 API key in headers

headers = {
    'X-API-Key' : 'your_api_key_here'
    'Content_type' : 'application/json'
}

response = requests.get('https://api.example.com/data', headers=headers)

#Method 2 API Key in Parameters

params = {
    'api-key': 'your_api_key_here', 
    'param' : 'value1'
}

reponse = request.get('https://api.example.com/data', params = params)

#Method 3 API key in url (less common, less secure)

api_key = 'your_api_here'
url = 'https://api.example.com/{api_key}/data'
response = requests.get(url)