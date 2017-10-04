import requests
from bs4 import BeautifulSoup

nhl_url="https://www.hockey-reference.com/leagues/NHL_2017_skaters.html"

r_reqs=requests.get(nhl_url)
soup=BeautifulSoup(r_reqs.content,'lxml')

links = soup.find_all('a')

rank_data = soup.find_all("th", {"data-stat": "ranker"})
player_data = soup.find_all("td", {"data-stat": "player"})
age_data = soup.find_all("td", {"data-stat": "age"})
stat_dict = {}
ranks = []
players = []
ages = []

for stat in rank_data:
	if(stat.text=="Rk"):
		continue 
	ranks.append(stat.text)
	stat_dict['rank']=ranks
	
for stat in player_data:
	players.append(stat.text)
	stat_dict['player']=players

for stat in age_data:
	
	ages.append(stat.text)
	stat_dict['age']=ages
	

print(stat_dict)
