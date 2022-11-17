from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json

class Player:
    points = 0
    def __init__(self, id):
        self.id = id

    def stats(self):
        client.regular_season_player_box_scores(
        player_identifier=self.id, 
        season_end_year=2023,
        output_type=OutputType.JSON,
        output_file_path="./stats.json")


cat = Player("westbru01")
cat.stats()
with open('stats.json') as f:
   data = json.load(f)
points = 0
for i in range(len(data)):
    cat.points += data[i]['points_scored']
cat.points = points/len(data)
print(cat.points/len(data))
