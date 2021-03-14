import requests
import json
from datetime import datetime
import time, threading

#setup

#pull in API key from text file
APIKey_file = open('Steam API Key.txt', 'rt')
APIKey = APIKey_file.read()

#get list of company numbers from text file
App_ID_File = open('App IDs.txt', 'rt')
App_IDs = App_ID_File.read()
App_ID_List = App_IDs.split('\n')

payload = {}
headers = {}

players_url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/'

global_stats_url = 'https://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v1/'
count = 100
stat_name = ''

#end setup

# https://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>

current_user_data = list()

WAIT_SECONDS = 300

def get_current_players():
	for App_ID in App_ID_List:
		full_url_users =  players_url + '?key=' + APIKey + '&appid=' + App_ID
		response = requests.request('GET', full_url_users, headers=headers, data=payload)
		user_data =  response.json()
		current_players = user_data.get('response').get('player_count')
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print(current_time + ' ' + str(current_players))
		current_user_data.append([current_time, current_players])
		# threading.Timer(WAIT_SECONDS, get_current_players).start()

def get_global_game_stats():
	for App_ID in App_ID_List:
		full_url_stats =  global_stats_url + '?key=' + APIKey + '&appid=' + App_ID + '&count=' + count + '&name[0]=' + stat_name
		response = requests.request('GET', full_url_stats, headers=headers, data=payload)
		game_data =  response.json()
		print(game_data)
    
get_current_players()

# get_global_game_stats()





