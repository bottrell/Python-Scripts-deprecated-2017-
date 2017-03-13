import requests
import json
def bf4stats():
    print "--- Battlefield 4 ---"
    bf4_result = requests.get('http://api.bf4stats.com/api/onlinePlayers')
    bf4_object = json.loads(bf4_result.text)
    print "*******************************************************"
    for x in bf4_object:
        print "Platform: " + bf4_object[x]['label']
        print  "Current plyers: " + str(bf4_object[x]['count'])
        print "24 Hour Peak: " + str(bf4_object[x]['peak24'])
        print "*******************************************************"
    
    return

def bf3stats():
    print "--- Battlefield 3 ---"
    bf3_result = requests.get("http://api.bf3stats.com/global/onlinestats/")
    bf3_object = json.loads(bf3_result.text)
    print "*******************************************************"
    print "Status: " + bf3_object["status"]
    print "*******************************************************"
    print "Platform: PC"
    print "Current players: " + str(bf3_object['pc'])
    print "*******************************************************"
    print "Platform: Xbox 360"
    print "Current players: " + str(bf3_object['360'])
    print "*******************************************************"
    print "Platform: Playstation 3"
    print "Current players: " + str(bf3_object['ps3'])
    print "*******************************************************"
    return

def bfhstats():
    print "--- Battlefield Hardline ---"
    bfh_result = requests.get('http://api.bfhstats.com/api/onlinePlayers')
    bfh_object = json.loads(bfh_result.text)
    print "*******************************************************"
    for x in bfh_object:
        print "Platform: " + bfh_object[x]['label']
        print  "Current plyers: " + str(bfh_object[x]['count'])
        print "24 Hour Peak: " + str(bfh_object[x]['peak24'])
        print "*******************************************************"
    
    return

def makeChoice():
    print "Which game?"
    print "1) Battlefield 3"
    print "2) Battlefield 4"
    print "3) Battlefield Hardline"
    print "4) Quit"
    choice = str(raw_input("-->"))
    print "\n \n \n \n"
    return choice

print "******************************************************************"
print "**********                                              **********"
print "**********             Battlefield Stats                **********"
print "**********             By Jordan Bottrell               **********"
print "**********                  3/13/2017                   **********"
print "**********                                              **********"
print "******************************************************************"
from datetime import datetime
now = datetime.now()
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour % 12, now.minute, now.second)
print "\n \n \n"

choice = makeChoice()
while choice != 'q':

    if choice == '1':
        bf3stats()
        print "\n \n \n \n"
        while choice == '1':
            choice = makeChoice()

    elif choice == '2':
        bf4stats()
        print "\n \n \n \n"
        while choice == '2':
            choice = makeChoice()

    elif choice == '3':
        bfhstats()
        print "\n \n \n \n"
        while choice == '3':
            choice = makeChoice()
        
    elif choice == '4':
        exit()

        
