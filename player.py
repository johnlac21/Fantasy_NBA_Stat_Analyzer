from . import LeagueStats
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json

class Player:
    points = 0
    assists = 0
    rebounds = 0
    averageFg = 0
    steals = 0
    blocks = 0
    gp = 0
    tray = 0
    name = ""
    totalFg = 0
    fgMade = 0
    ftTaken = 0
    ftMade = 0
    turnovers = 0
    ftAverage = 0



client.players_season_totals(
    season_end_year=2023, 
    output_type=OutputType.JSON, 
    output_file_path="./stats.json"
)
with open('stats.json') as f:
   data = json.load(f)
players = []
leagueStats = LeagueStats(20)
for i in range(len(data)):
    cat = Player
    cat.name = data[i]['name']
    cat.points = data[i]['points'] / range(len(data))
    cat.assists = data[i]['assists'] / range(len(data))
    cat.rebounds = data[i]['rebounds'] / range(len(data))
    cat.steals = data[i]['steals'] / range(len(data))
    cat.blocks = data[i]['blocks'] / range(len(data))
    cat.tray = data[i]['made_three_point_field_goals'] / range(len(data))
    cat.turnovers = data[i]['turnovers'] / range(len(data))
    cat.gp = data[i]['games-played']
    cat.totalFg = data[i]['attempted_field_goals']
    cat.fgMade = data[i]['made_field_goals']
    cat.averageFg = cat.totalFg / cat.fgMade
    cat.ftTaken = data[i]['attempted_free_throws']
    cat.ftMade = data[i]['made_free_throws']
    cat.ftAverage = cat.ftTaken / cat.ftAverage
    players.append(cat)
    leagueStats.getLeagueTotals(cat)
averageStats = leagueStats.getLeagueAverage(len(players))
print(players[0].points)
print(players[0].name)
