import requests
import json

#setup

#pull in API key from text file
APIKey_file = open('MozHere API Key.txt', 'rt')
APIKey = APIKey_file.read()

payload = {}
headers = {}
platform = 'PC'
player = 'GrumpyEconomist'

# url = 'https://api.mozambiquehe.re/bridge?player=' + player + '&platform=' + platform + '&auth=' + APIKey + '&history=1&action=get'

url = 'https://api.mozambiquehe.re/maprotation?auth=' + APIKey

response = requests.request('GET', url, headers=headers, data=payload)

map_rotation_data = response.json()

# print(map_rotation_data)

#end setup

map_name = map_rotation_data.get('current').get('map')
start = map_rotation_data.get('current').get('readableDate_start')
end = map_rotation_data.get('current').get('readableDate_end')
map_time_remaining = map_rotation_data.get('current').get('remainingTimer')
next_map_name = map_rotation_data.get('next').get('map')
next_map_start = map_rotation_data.get('next').get('readableDate_start')

print('Current map is ' + map_name + ', for another ' + str(map_time_remaining))
print('Next map is ' + next_map_name + ' from ' + str(next_map_start))
