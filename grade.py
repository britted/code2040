# check grade from challenges
import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})

r = requests.post('http://challenge.code2040.org/api/register', data=data)
json_response = r.json()
my_id = json_response['result'] 

data = json.dumps({'token': my_id})
s = requests.post('http://challenge.code2040.org/api/status', data=data)
print s.json()
