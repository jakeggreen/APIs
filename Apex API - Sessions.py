import requests
import json
import datetime

#define class for a match

class Match:
	def __init__(self, player, startdate, enddate, legend, rankscore):
		self.player = player
		self.startdate = startdate
		self.enddate = enddate
		self.legend = legend
		self.rankscore = rankscore
	def getPlayer(self):
		return self.player
	def getStart(self):
		return self.startdate
	def getEnd(self):
		return self.enddate
	def getLegend(self):
		return self.legend
	def getRank(self):
		return self.rankscore

def getPlayerName(player):
	return Match.getPlayer()

#setup

#pull in API key from text file
APIKey_file = open('Apex.txt', 'rt')
APIKey = APIKey_file.read()

#get list of player names from separate text file
player_name_file = open('Players.txt', 'rt')
players = player_name_file.read()
player_names = players.split('\n')

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

payload = {}

headers = {'TRN-Api-Key': APIKey}

session_data = list();

#end setup

for player in player_names:
	full_url = url + player + '/sessions'
	response = requests.request('GET', full_url, headers=headers, data=payload)
	player_data = response.json()
	player = player
	#check to see if player data is available
	if player_data.get('data') and player_data.get('data').get('items'):
		#get the start and end dates for matches
		for dates in player_data.get('data').get('items'):
			startdate = datetime.datetime.strptime(dates['metadata']['startDate']['value'],'%Y-%m-%dT%H:%M:%S.%fZ')
			enddate = datetime.datetime.strptime(dates['metadata']['endDate']['value'],'%Y-%m-%dT%H:%M:%S.%fZ')
			#for each match get the legend used and the ending rank score
			for matches in dates.get('matches'):
				legend = matches['metadata']['character']['displayValue']
				rankscore = matches['stats']['rankScore']['value']
				session_data.append(Match(player, startdate, enddate, legend, rankscore));

for match in session_data:
	# print('-----\r' + Match.getPlayer(match) + '\r-----')
	print(Match.getPlayer(match) + ' - Start: ' + str(Match.getStart(match)) + ', End: ' 
	+ str(Match.getEnd(match)) + ', Played With: ' + str(Match.getLegend(match)) + ', Rank: ' + str(Match.getRank(match)))