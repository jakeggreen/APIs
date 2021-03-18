import requests
import json

class Legend:
	def __init__(self, player, name, kills):
		self.player = player
		self.name = name
		self.kills = kills
	def getPlayer(self):
		return self.player
	def getKills(self):
		return self.kills
	def getName(self):
		return self.name

def getLegendKills(legend):
	return legend.getKills()

#setup

#pull in API key from text file
APIKey_file = open("Apex.txt", "rt")
APIKey = APIKey_file.read()

#get list of player names from separate text file
player_name_file = open("Players.txt", "rt")
players = player_name_file.read()
player_names = players.split("\n")

all_legend_names_list = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

all_legend_names_set = set(all_legend_names_list)

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

segment_type = 'legend'

payload = {}

headers = {'TRN-Api-Key': APIKey}

legend_data = list();

#end setup

#HTTP request to tracker.gg api looping through available players
for player in player_names:
	full_url = url + player + "/segments" + "/" + segment_type
	response = requests.request("GET", full_url, headers=headers, data=payload)
	player_data = response.json()
	#process reponse data
	for legend in all_legend_names_set:
		#set default kills to 0
		kills = 0;
		player = player;
		#check to see if player data is available
		try:
			for item in player_data["data"]:
				#if legend name matches a player data legend name then try to get kill data
				if item.get("metadata").get("name") == legend:
					#if kill data is available then set value of kills
					if item.get("stats") and item.get("stats").get("kills") and item.get("stats").get("kills").get("value"):
						kills = int(item["stats"]["kills"]["value"])
		except Exception:
			pass
		#initialise Legend object for each legend using player name, legend name and kills as parameters.
		legend_data.append(Legend(player, legend, kills));

	#sort based by kill count (descending)
	legend_data.sort(key= getLegendKills, reverse = True)
	#print name with formatting
	print("-----\r" + player + "\r-----")
	#print all legend data
	for legend in legend_data:
		print(str(legend.getKills()) + " kills with " + legend.getName())
	#clear the list to start loop again - this can be done better but it's midnight and i'm pooped	
	legend_data.clear()