import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})
# post to url to get id
r = requests.post('http://challenge.code2040.org/api/register', data=data)
# get id and save for later use
json_response = r.json()
my_id = json_response['result'] 
# post id to url to get the prefix and array
data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/prefix',data=data)
# save the prefix and array from info sent from endpoint
response = r.json()
print response
prefix = response['result']['prefix']
array = response['result']['array']
# create new array to add the strings that do not start with the prefix
newArray = []
# iterate through array and determine what does not start with the prefix and add those to the newArray
for string in array:
	if not string.startswith(prefix):
		newArray.append(string)
# post the resulting array to the endpoint
data = json.dumps({'token': my_id, 'array': newArray})
s = requests.post('http://challenge.code2040.org/api/validateprefix', data=data)
# see result and if correct
print s.json()

