from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json

class LeagueStats:
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

    def __init__(self, threshold):
        self.threshold = threshold
    
    def getLeagueTotals(self, player):
        if(player.gp >= self.threshold):
            self.points += player.points
            self.assists += player.assists
            self.rebounds += player.rebounds
            self.steals += player.steals
            self.blocks += player.blocks
            self.tray += player.tray
            self.totalFg += player.totalFg
            self.fgMade += player.fgMade
            self.turnovers += player.turnovers
            self.ftTaken += player.ftTaken
            self.ftMade += player.ftMade

    def getLeagueAverage(self, totalPlayers):
        averageStats = LeagueStats(self.threshold)
        averageStats.points = self.points / totalPlayers
        averageStats.assists = self.assists / totalPlayers
        averageStats.rebounds = self.rebounds / totalPlayers
        averageStats.steals = self.steals / totalPlayers
        averageStats.blocks = self.blocks / totalPlayers
        if(self.ftMade != 0):
            averageStats.ftAverage = self.ftMade / self.ftTaken
        if(self.fgMade != 0):
            averageStats.averageFg = self.fgMade / self.totalFg
        averageStats.turnovers = self.turnovers / totalPlayers
        averageStats.tray = self.tray / totalPlayers
        return averageStats
