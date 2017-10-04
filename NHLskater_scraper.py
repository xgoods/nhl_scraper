import requests
from bs4 import BeautifulSoup
import csv

nhl_url = "https://www.hockey-reference.com/leagues/NHL_2017_skaters.html"

r_reqs = requests.get(nhl_url)
soup = BeautifulSoup(r_reqs.content, 'lxml')

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
pick_stats = {"G": 5, "A": 3, "+/-": 1, "PIM": .25, "PPG": 2, "PPA": 1, "SHG": 1, "SHA": .5, "GWG": 2, "SOG": .5, "HITS": .25, "BLK": 1}
pick_players = []
fan_points = [0]
player_count = 0
fan_pointsAVG = []

for stat in rank_data:
    if (stat.text == "Rk"):
        continue
    ranks.append(stat.text)
    stat_dict['(A)Rk'] = ranks

for stat in player_data:
    players.append(stat.text)
    stat_dict['(B)Player'] = players
    player_count += 1
for stat in age_data:
    ages.append(stat.text)
    stat_dict['(C)Age'] = ages

for stat in pos_data:
    pos.append(stat.text)
    stat_dict['(D)Pos'] = pos

for stat in team_data:
    teams.append(stat.text)
    stat_dict['(E)Tm'] = teams

for stat in games_data:
        games.append(stat.text)
        stat_dict['(F)GP'] = games

if "G" in pick_stats:
    i = 0
    for stat in goals_data:
        goals.append(stat.text)
        stat_dict['(G)G'] = goals
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["G"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "A" in pick_stats:
    i = 0
    for stat in assists_data:
        assists.append(stat.text)
        stat_dict['(H)A'] = assists
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["A"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1


if "PTS" in pick_stats:
    i = 0
    for stat in points_data:
        points.append(stat.text)
        stat_dict['(I)PTS'] = points
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["PTS"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "+/-" in pick_stats:
    i = 0
    for stat in plusMinus_data:
        plus_minus.append(stat.text)
        stat_dict['(J)+/-'] = plus_minus
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["+/-"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "PIM" in pick_stats:
    i = 0
    for stat in penaltyMin_data:
        penalty_mins.append(stat.text)
        stat_dict['(K)PIM'] = penalty_mins
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["PIM"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "PS" in pick_stats:
    i = 0
    for stat in pointShares_data:
        point_shares.append(stat.text)
        stat_dict['(L)PS'] = point_shares
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["PS"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "EVG" in pick_stats:
    i = 0
    for stat in evenStrength_data:
        evenStr_goals.append(stat.text)
        stat_dict['(M)EVG'] = evenStr_goals
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["EVG"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "PPG" in pick_stats:
    i = 0
    for stat in powerPlay_data:
        pp_goals.append(stat.text)
        stat_dict['(N)PPG'] = pp_goals
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["PPG"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "SHG" in pick_stats:
    i = 0
    for stat in shortHand_data:
        sh_goals.append(stat.text)
        stat_dict['(O)SHG'] = sh_goals
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["SHG"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "GWG" in pick_stats:
    i = 0
    for stat in gameWinGoal_data:
        gw_goals.append(stat.text)
        stat_dict['(P)GWG'] = gw_goals
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["GWG"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "EVA" in pick_stats:
    i = 0
    for stat in evenStrAssist_data:
        ev_assists.append(stat.text)
        stat_dict['(Q)EVA'] = ev_assists
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["EVA"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "PPA" in pick_stats:
    i = 0
    for stat in ppAssist_data:
        pp_assists.append(stat.text)
        stat_dict['(R)PPA'] = pp_assists
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["PPA"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "SHA" in pick_stats:
    i = 0
    for stat in shAssist_data:
        sh_assists.append(stat.text)
        stat_dict['(S)SHA'] = sh_assists
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["SHA"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "SOG" in pick_stats:
    i = 0
    for stat in shots_data:
        shots.append(stat.text)
        stat_dict['(T)SOG'] = shots
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["SOG"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "SOG%" in pick_stats:
    i = 0
    for stat in shotPCT_data:
        shot_pct.append(stat.text)
        stat_dict['(U)SOG%'] = shot_pct
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["SOG%"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "TOI" in pick_stats:
    i = 0
    for stat in toi_data:
        toi.append(stat.text)
        stat_dict['(V)TOI'] = toi
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["TOI"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "ATOI" in pick_stats:
    i = 0
    for stat in toiAVG_data:
        toiAVG.append(stat.text)
        stat_dict['(W)ATOI'] = toiAVG
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["ATOI"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "BLK" in pick_stats:
    i = 0
    for stat in blocks_data:
        blocks.append(stat.text)
        stat_dict['(X)BLK'] = blocks
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["BLK"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "HITS" in pick_stats:
    i = 0
    for stat in hits_data:
        hits.append(stat.text)
        stat_dict['(Y)HITS'] = hits
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["HITS"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "FOW" in pick_stats:
    i = 0
    for stat in fow_data:
        fow.append(stat.text)
        stat_dict['(Z)FOW'] = fow
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["FOW"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "FOL" in pick_stats:
    i = 0
    for stat in fol_data:
        fol.append(stat.text)
        stat_dict['(Z1)FOL'] = fol
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["FOL"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

if "FOP" in pick_stats:
    i = 0
    for stat in fop_data:
        fop.append(stat.text)
        stat_dict['(Z2)FOP'] = fop
        fan_points.insert(i, fan_points[i] + (int(stat.text) * pick_stats["FOP"]))
        if (len(fan_points) == (player_count + 1)):
            del fan_points[i + 1]
        i += 1

stat_dict['(B1)FANPTS']=fan_points
del fan_points[player_count:]

for avg in stat_dict['(F)GP']:
    i = 0
    fan_pointsAVG.append(round(fan_points[i]/int(avg), 1))

    stat_dict['(B2)FANPTS(avg)'] = fan_pointsAVG
    i += 1

keys = sorted(stat_dict.keys())
with open('fantasy_stats.csv', "wb") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(keys)
    writer.writerows(zip(*[stat_dict[key] for key in keys]))

