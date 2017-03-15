import json
import requests
import random
import sys
import os

def printMenu():
    choice = raw_input("Pick another game: <press a> \nNew Account: <press n>")
    if choice == 'a':
        restart = False
    else:
        restart = True
    return restart
    
def getPlayerID():
    player = str(raw_input("What is your SteamID? --> "))
    print "******************************************************************"
    return player

def chooseGame(playerid):
    games_lib = []
    player_result = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=67884AA4EAEA34CB6FDDDF9EE25680FD&steamid=' + playerid + '&format=json')
    player_object = json.loads(player_result.text)
    print "\n\nGame Count: "
    print player_object["response"]["game_count"]
    
    print "--------------------------------------------------------------"
    
    for x in player_object["response"]["games"]:
        games_lib.append(str(x["appid"]))
    #chooses random game from your library
    appid = (random.choice(games_lib))
    return appid



def getGameInfo(appid):
    game_result = requests.get('http://store.steampowered.com/api/appdetails?appids=' + appid)
    game_object = json.loads(game_result.text)
    print "You should play: " + game_object[appid]['data']["name"]
    print "--------------------------------------------------------------"
    print "Release Date: " + game_object[appid]['data']['release_date']["date"]
    print "-------------------------------------------------------------- \n \n"
    return


print "******************************************************************"
print "**********                                              **********"
print "**********               Steam Roulette                 **********"
print "**********             By Jordan Bottrell               **********"
print "**********                  3/15/2017                   **********"
print "**********                                              **********"
print "******************************************************************"
from datetime import datetime
now = datetime.now()

def main():
    restart = False
    player = str(getPlayerID())

    while restart != True:
    
        game = str(chooseGame(player))
        getGameInfo(game)
        restart = printMenu()
    print '''\n \n****************************************************************** \n PROGRAM RESTART \n******************************************************************\n \n'''
    main()
    return


main()
