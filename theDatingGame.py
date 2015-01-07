import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})

r = requests.post('http://challenge.code2040.org/api/register', data=data)

json_response = r.json()
my_id = json_response['result'] 

data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/time',data=data)

dateAndTime = r.json()
print dateAndTime
datestamp = dateAndTime['result']['datestamp']
interval = dateAndTime['result']['interval']

import datetime
from datetime import timedelta
import dateutil.parser

day = dateutil.parser.parse(datestamp)
newDate = day + datetime.timedelta(seconds = interval)
newDate = newDate.isoformat()
print newDate

data = json.dumps({'token': my_id, 'datestamp': newDate})
s = requests.post('http://challenge.code2040.org/api/validatetime', data=data)
print s.json()