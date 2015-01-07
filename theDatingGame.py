import requests
import json
data = json.dumps({'email': 'bsp.edwards@gmail.com', 'github': 'https://github.com/britted/code2040.git'})
# post to url to get id 
r = requests.post('http://challenge.code2040.org/api/register', data=data)
# get id from endpoint and save for later use
json_response = r.json()
my_id = json_response['result'] 
# post to url and get time and date data
data = json.dumps({'token': my_id})
r = requests.post('http://challenge.code2040.org/api/time',data=data)
# save time and interval data
dateAndTime = r.json()
print dateAndTime
datestamp = dateAndTime['result']['datestamp']
interval = dateAndTime['result']['interval']
# import datetime library to be used to do date arithmetic 
import datetime
from datetime import timedelta
import dateutil.parser
# parse iso8601 date so datetime can be used
day = dateutil.parser.parse(datestamp)
# add interval to date
newDate = day + datetime.timedelta(seconds = interval)
# convert back to is08601 format
newDate = newDate.isoformat()
print newDate
# post the new date to url 
data = json.dumps({'token': my_id, 'datestamp': newDate})
s = requests.post('http://challenge.code2040.org/api/validatetime', data=data)
# see result and if correct
print s.json()
