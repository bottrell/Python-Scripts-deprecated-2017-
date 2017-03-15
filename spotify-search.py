# Search songs on Spotify based on song name and the amount of results you want!

import requests
import json

def makeChoice():
    user_song = raw_input("What song would you like to search? (type quit to exit)")
    user_song = user_song.strip()
    user_song = user_song.replace(" ", "+")
    return user_song

def limitChoice():
    limit = raw_input("How many results would you like?")
    return limit


def spotifySong():
    spotify_result = requests.get('https://api.spotify.com/v1/search?q=' + user_song + '&type=track&limit=' + str(limit))
    spotify_object = json.loads(spotify_result.text)
    print "-------------------------------------------------------------------"
    print "*******************************************************************"
    print "-------------------------------------------------------------------"
    for x in spotify_object["tracks"]:
        if x == "items":
            for item in spotify_object["tracks"][x]:
                for thing in item:
                    if thing == "name":
                        print "Song: "
                        print item[thing]
                        print "---------------------------"
                    elif thing == "popularity":
                        print "Popularity: "
                        print str(item[thing]) + " / 100"
                        print "---------------------------"
                    elif thing == "artists":
                        print "Artist: "
                        print (item[thing])[0]['name']
                    elif thing == "external_urls":
                        print "Link: "
                        print item[thing]['spotify']
                        print "---------------------------"
                print "-------------------------------------------------------------------"
                print "*******************************************************************"
                print "-------------------------------------------------------------------"
    print "\n \n"
    return


print "******************************************************************"
print "**********                                              **********"
print "**********             Spotify Song Search              **********"
print "**********             By Jordan Bottrell               **********"
print "**********                  3/13/2017                   **********"
print "**********                                              **********"
print "******************************************************************"
from datetime import datetime
now = datetime.now()
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour % 12, now.minute, now.second)
print "\n \n \n"


user_song = makeChoice()
limit = limitChoice()

while user_song != 'quit':
    spotifySong()
    user_song = makeChoice()
    limit = limitChoice()
    


exit()  


                
    
