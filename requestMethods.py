import requests

'these are the methods used to interact with api'
#get, post, put, patch, delete


#retrieve data GET method
response = requests.get('https://api.example.com/users')

#Create new resource eg.new user POST method
new_user = {'name' : 'John Doe', 'email': 'john@email.com'} 
response = requests.post('https://api.example.com/users', json=new_user)

#Update user PUT method
updated_user = {'id': 1, 'name' : 'John Doe', 'email': 'john@email.com'}
reponse = requests.put('https://api.example.com/users/1', json=updated_user)

#partial update PATCH method
partial_update = {'email': 'john@email.com'}
response = requests.patch('https://api.example.com/users/1', json=partial_update)

response = requests.delete('https://api.example.com/users/1')

