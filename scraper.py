import urllib2
import os
import json
from secret import API_KEY as api_key

def save(obj, file_name):
    with open(file_name, 'w') as outfile:
        json.dump(obj, outfile)

def api_call(url):
    return urllib2.urlopen(url + '?apikey=' + api_key)

def json_call(url):
    return json.load(api_call(url))

if not os.path.exists('data'):
    os.makedirs('data')

lists = json_call('http://api.rottentomatoes.com/api/public/v1.0/lists.json')

for category in lists['links']:
    print category
    for list in json_call(lists['links'][category]):
        pass