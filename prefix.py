import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})

r = requests.post('http://challenge.code2040.org/api/register', data=data)

json_response = r.json()
my_id = json_response['result'] 

data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/prefix',data=data)

response = r.json()
print response
prefix = response['result']['prefix']
array = response['result']['array']
newArray = []

for string in array:
	if not string.startswith(prefix):
		newArray.append(string)

data = json.dumps({'token': my_id, 'array': newArray})
s = requests.post('http://challenge.code2040.org/api/validateprefix', data=data)
print s.json()

