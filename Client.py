from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json
from LeagueStats import LeagueStats
from player import Player

client.players_season_totals(
    season_end_year=2023, 
    output_type=OutputType.JSON, 
    output_file_path="./stats.json"
)
with open('stats.json') as f:
   data = json.load(f)
players = []
leagueStats = LeagueStats(5)
for i in range(len(data)):
    cat = Player
    cat.gp = data[i]['games_played']
    cat.name = data[i]['name']
    cat.points = data[i]['points'] / cat.gp
    cat.assists = data[i]['assists'] / cat.gp
    cat.rebounds = (data[i]['defensive_rebounds'] + data[i]['offensive_rebounds']) / cat.gp
    cat.steals = data[i]['steals'] / cat.gp
    cat.blocks = data[i]['blocks'] / cat.gp
    cat.tray = data[i]['made_three_point_field_goals'] / cat.gp
    cat.turnovers = data[i]['turnovers'] / cat.gp
    cat.totalFg = data[i]['attempted_field_goals']
    cat.fgMade = data[i]['made_field_goals']
    if(cat.totalFg != 0):
        cat.averageFg = cat.fgMade / cat.totalFg
    cat.ftTaken = data[i]['attempted_free_throws']
    cat.ftMade = data[i]['made_free_throws']
    if(cat.ftTaken != 0):
        cat.ftAverage = cat.ftMade / cat.ftTaken
    players.append(cat)
    leagueStats.getLeagueTotals(cat)
averageStats = leagueStats.getLeagueAverage(len(players))

print(averageStats.ftAverage)