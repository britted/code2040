import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})
# post info to url to get id
r = requests.post('http://challenge.code2040.org/api/register', data=data)
# save id for later use
json_response = r.json()
my_id = json_response['result'] 
# get the needle and haystack information
data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/haystack',data=data)
# get the needle and haystack values
response = r.json()
print response
needle = response['result']['needle']
haystack = response['result']['haystack']
# search for the needle in the haystack and return index
needleIndex = haystack.index(needle)
# post the result of the index
data = json.dumps({'token': my_id, 'needle': needleIndex})
s = requests.post('http://challenge.code2040.org/api/validateneedle', data=data)
# see result and if correct
print s.json()
