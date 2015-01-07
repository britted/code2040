import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})
# post to url to get id
r = requests.post('http://challenge.code2040.org/api/register', data=data)
# get id and save to use later
json_response = r.json()
my_id = json_response['result'] 
# post to url to get word to be reversed 
data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/getstring',data=data)
# get the word that needs to be reversed from what was sent from endpoint
word_response = r.json()
print word_response
word = word_response['result']
# reverse the word by going thoguh the word backwards one letter at a time
newWord = word[::-1]
print newWord
# post the resulting new word
data = json.dumps({'token': my_id, 'string': newWord})
s = requests.post('http://challenge.code2040.org/api/validatestring', data=data)
# see result and if correct 
print s.json() 

# alternate method
# newWord = ''
# for each in word: 
# 	newWord = each + newWord
# print newWord
