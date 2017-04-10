import sys
import random
from src.Utilities import DataReader
from src.Team import Team
from src.Game import Game

def printStats(name1, name2):
    """ Print the state of the play predictor

    @params:
        :name: name of the team1
        :down: down the play is on
        :distance: distance to go
        :field: position on the field
    """
    print(name1)
    print(name2)

name1 = sys.argv[1]
name2 = sys.argv[2]

# Read in team1 stats
dataReader = DataReader()
rushingData = dataReader.statReader("Rushing.csv")
passingData = dataReader.statReader("Passing.csv")
kickingData = dataReader.statReader("Kicking.csv")
returningData = dataReader.statReader("Returning.csv")
puntingData = dataReader.statReader("Punting.csv")
downData = dataReader.statReader("Down.csv")

# Read in play percentages
playData = dataReader.playReader("Percent.csv")

# Build Team
team1 = Team(name1)
team1.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, downData, playData)

team2 = Team(name2)
team2.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, downData, playData)

fileWriter = open("output.txt", 'w')
for i in range(1):
    game = Game(team1, team2)
    game.startGame()
    while(game.quarter <= 4):
        game.playGame(game.possession)
        game.displayGame()
    if game.score1 > game.score2:
        fileWriter.write(game.team1.name + "\n")
    elif game.score2 > game.score1:
        fileWriter.write(game.team2.name + "\n")
    else:
        fileWriter.write("Tie\n")
fileWriter.close()
