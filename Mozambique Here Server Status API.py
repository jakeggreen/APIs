import requests
import json
from datetime import datetime

#setup

APIKey_file = open('MozHere API Key.txt', 'rt')
APIKey = APIKey_file.read()

payload = {}
headers = {}

url = 'https://api.mozambiquehe.re/servers?auth=' + APIKey

response = requests.request('GET', url, headers=headers, data=payload)

server_status_data = response.json()

servers_list = ('Origin_login','EA_accounts','ApexOauth_Steam','ApexOauth_Crossplay','ApexOauth_PC')

location_list = ('EU-West','EU-East')

#end setup

for server_type, item in server_status_data.items():
	if server_type in servers_list:
		for location in item.items():
			server_location = location[0]
			if server_location in location_list:
				server_status = location[1]['Status']
				time_stamp = datetime.fromtimestamp(location[1]['QueryTimestamp']).strftime('%H:%M:%S')
				print(server_type, server_location, server_status)