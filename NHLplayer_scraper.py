import requests
from bs4 import BeautifulSoup

nhl_url="https://www.hockey-reference.com/leagues/NHL_2017_skaters.html"

r_reqs=requests.get(nhl_url)
soup=BeautifulSoup(r_reqs.content,'lxml')

links = soup.find_all('a')

rank_data = soup.find_all("th", {"data-stat": "ranker"})
player_data = soup.find_all("td", {"data-stat": "player"})
age_data = soup.find_all("td", {"data-stat": "age"})
pos_data = soup.find_all("td", {"data-stat": "pos"})
team_data = soup.find_all("td", {"data-stat": "team_id"})
games_data = soup.find_all("td", {"data-stat": "games_played"})
goals_data = soup.find_all("td", {"data-stat": "goals"}) 
assists_data = soup.find_all("td", {"data-stat": "assists"})
points_data = soup.find_all("td", {"data-stat": "points"})
plusMinus_data = soup.find_all("td", {"data-stat": "plus_minus"})
penaltyMin_data = soup.find_all("td", {"data-stat": "pen_min"})
pointShares_data = soup.find_all("td", {"data-stat": "ps"})
evenStrength_data = soup.find_all("td", {"data-stat": "goals_ev"})
powerPlay_data = soup.find_all("td", {"data-stat": "goals_pp"})
shortHand_data = soup.find_all("td", {"data-stat": "goals_sh"})
gameWinGoal_data = soup.find_all("td", {"data-stat": "goals_gw"})
evenStrAssist_data = soup.find_all("td", {"data-stat": "assists_ev"})
ppAssist_data = soup.find_all("td", {"data-stat": "assists_pp"})
shAssist_data = soup.find_all("td", {"data-stat": "assists_sh"})
shots_data = soup.find_all("td", {"data-stat": "shots"})
shotPCT_data = soup.find_all("td", {"data-stat": "shot_pct"})
toi_data = soup.find_all("td", {"data-stat": "time_on_ice"})
toiAVG_data = soup.find_all("td", {"data-stat": "time_on_ice_avg"})
blocks_data = soup.find_all("td", {"data-stat": "blocks"})
hits_data = soup.find_all("td", {"data-stat": "hits"})
fow_data = soup.find_all("td", {"data-stat": "faceoff_wins"})
fol_data = soup.find_all("td", {"data-stat": "faceoff_losses"})
fop_data = soup.find_all("td", {"data-stat": "faceoff_percentage"})

stat_dict = {}
ranks = []
players = []
ages = []
pos = []
teams = []
games = []
goals = []
assists = []
points = []
plus_minus = []
penalty_mins = []
point_shares = []
evenStr_goals = []
pp_goals = []
sh_goals = []
gw_goals = []
ev_assists = []
pp_assists = []
sh_assists = []
shots = []
shot_pct = []
toi = []
toiAVG = []
blocks = []
hits = []
fow = []
fol = []
fop = []

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
	
for stat in pos_data:
	pos.append(stat.text)
	stat_dict['pos']=pos
	
for stat in team_data:
	teams.append(stat.text)
	stat_dict['team']=teams

for stat in games_data:
	games.append(stat.text)
	stat_dict['games']=games	

for stat in goals_data:
	goals.append(stat.text)
	stat_dict['goals']=goals

for stat in assists_data:
	assists.append(stat.text)
	stat_dict['assists']=assists

for stat in points_data:
	points.append(stat.text)
	stat_dict['points']=points

for stat in plusMinus_data:
	plus_minus.append(stat.text)
	stat_dict['plus_minus']=plus_minus

for stat in penaltyMin_data:
	penalty_mins.append(stat.text)
	stat_dict['pen_mins']=penalty_mins

for stat in pointShares_data:
	point_shares.append(stat.text)
	stat_dict['PS']=point_shares

for stat in evenStrength_data:
	evenStr_goals.append(stat.text)
	stat_dict['EVG']=evenStr_goals

for stat in powerPlay_data:
	pp_goals.append(stat.text)
	stat_dict['PPG']=pp_goals

for stat in shortHand_data:
	sh_goals.append(stat.text)
	stat_dict['SH']=sh_goals

for stat in gameWinGoal_data:
	gw_goals.append(stat.text)
	stat_dict['GW']=gw_goals

for stat in evenStrAssist_data:
	ev_assists.append(stat.text)
	stat_dict['EVA']=ev_assists

for stat in ppAssist_data:
	pp_assists.append(stat.text)
	stat_dict['PPA']=pp_assists

for stat in shAssist_data:
	sh_assists.append(stat.text)
	stat_dict['SHA']=sh_assists

for stat in shots_data:
	shots.append(stat.text)
	stat_dict['shots']=shots

for stat in shotPCT_data:
	shot_pct.append(stat.text)
	stat_dict['S%']=shot_pct

for stat in toi_data:
	toi.append(stat.text)
	stat_dict['TOI']=toi

for stat in toiAVG_data:
	toiAVG.append(stat.text)
	stat_dict['ATOI']=toiAVG

for stat in blocks_data:
	blocks.append(stat.text)
	stat_dict['BLK']=blocks

for stat in hits_data:
	hits.append(stat.text)
	stat_dict['HITS']=hits

for stat in fow_data:
	fow.append(stat.text)
	stat_dict['FOW']=fow

for stat in fol_data:
	fol.append(stat.text)
	stat_dict['FOL']=fol

for stat in fop_data:
	fop.append(stat.text)
	stat_dict['FOP']=fop


print(stat_dict)
