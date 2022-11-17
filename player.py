from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json

class Player:
    points = 0
    name = ""



client.players_season_totals(
    season_end_year=2023, 
    output_type=OutputType.JSON, 
    output_file_path="./stats.json"
)
with open('stats.json') as f:
   data = json.load(f)
Players = []
for i in range(len(data)):
    cat = Player
    cat.name = data[i]['name']
    cat.points = data[i]['points'] / len(data)
    Players.append(cat)
print(Players[0].points)
print(Players[0].name)
