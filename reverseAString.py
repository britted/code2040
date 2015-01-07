import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})

r = requests.post('http://challenge.code2040.org/api/register', data=data)

json_response = r.json()
my_id = json_response['result'] 

data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/getstring',data=data)

word_response = r.json()
print word_response
word = word_response['result']

newWord = word[::-1]
print newWord

data = json.dumps({'token': my_id, 'string': newWord})
s = requests.post('http://challenge.code2040.org/api/validatestring', data=data)
print s.json() 

# newWord = ''


# for each in word: 
# 	newWord = each + newWord
# print newWord