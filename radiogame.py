# -*- coding: utf-8 -*-
"""
Created on Sat Jan 7 12:51:34 2019

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

1923 RADIO MONOPOLY
Genres: RPG, strategy, educational

Description: You think you know 1923? You think you're so cool that you're the bee's knees?
Horsefeathers! Relive the Roaring Twenties experience as a DC radio mogul under direct
appointment of the Illuminati (or under direction of the United States Secret Service) to
prepare for "Great Struggles to Come" by bringing as many people as possible in the nation
under mass media and radio. Scenario may or may not be fictional.

Instructions: You start with a radio station in Washington DC and 50,000 listeners.
Use the references provided to you to type in the name of a city to attempt a takeover.
You can start by typing in 'washington' to develop your radio station.

Suggested citation as computer software for reference:
Pan, Alan J. (2019). 1923 Radio Monopoly [Computer software]. Github repository <https://github.com/alanjpan/1923-Radio-Monopoly>

Note this software's license is GNU GPLv3.
"""

import time
import sys

def dramatype(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

import random
secure_random = random.SystemRandom()

import math

cities = ['washington', 'new york', 'philadelphia', 'boston', 'baltimore', 'pittsburgh', 'chicago', 'detroit', 'cleveland', 'st louis', 'buffalo', 'milwaukee', 'newark', 'cincinnati', 'minneapolis', 'kansas city', 'indianapolis', 'jersey city', 'rochester', 'toledo', 'providence', 'columbus', 'louisville', 'st paul', 'akron', 'atlanta', 'worcester', 'birmingham', 'syracuse', 'richmond', 'new haven', 'memphis', 'dayton', 'bridgeport', 'hartford', 'scranton', 'grand rapids', 'jacksonville', 'new orleans', 'oklahoma city', 'san antonio', 'dallas']
citiespop = [437600, 5620000, 1800000, 748000, 733800, 588000, 2702000, 993000, 796800, 772900, 507000, 457000, 414500, 401000, 380500, 324500, 314000, 298000, 296000, 243000, 237500, 237000, 234500, 234500, 208500, 200500, 179500, 179000, 171500, 171500, 162500, 162000, 152500, 143500, 138000, 138000, 137500, 91500, 387000, 91000, 256500, 161000]
citiesgps = [[39, -77], [40, -74], [40, -75], [42, -71], [39, -76], [40, -80], [41, -87], [42, -83], [41, -82], [38, -90], [43, -79], [43, -88], [41, -74], [49, -84], [45, -94], [39, -94], [40, -86], [39, -74], [43, -77], [42, -83], [41, -71], [40, -83], [38, -85], [45, -93], [41, -81], [34, -84], [42, -72], [33, -87], [43, -76], [37, -77], [41, -73], [35, -90], [39, -84], [42, -74], [42, -73], [41, -76], [43, -86], [30, -82], [30, -90], [35, -97], [29, -98], [33, -97]]
citieslisteners = [50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

high = ['BREAKING NEWS a ']
praise = ['bees knees', 'cats meow', 'cats pajamas', 'berries', 'ritz', 'swank', 'hotsy-totsy']
low = ['in todays news, a ', 'a local ', 'believe it or not, a ', 'a ', 'low-town blues... a ', 'heard on the street, a ']
person = ['granny ', 'big cheese ', 'bluenose ', 'dumb dora ', 'fall guy ', 'hoofer ', 'lounge lizard ', 'moll ', 'pushover ', 'sheba ', 'swell ', 'drugstore cowboy ']
verb = ['bumped off a ', 'carries a torch to a ', 'has a crush on a ', 'framed a ', 'drank giggle water with a ', 'gives the heebie-jeebies to ', 'is being hotsy-totsy to ', 'landed a fist right in the kisser of a ', 'necks a ', 'scrammed to a ', 'is stuck on a ', 'upchucked on ', 'had a whoopee with ']
#http://www.huffenglish.com/gatsby/slang.html

def lownews():
    news = ''
    news += secure_random.choice(cities) + ': '
    news += secure_random.choice(low)
    news += secure_random.choice(person)
    news += secure_random.choice(verb)
    news += secure_random.choice(person)
    print()
    dramatype(news)
    print()

def highnews():
    news = ''
    news += secure_random.choice(cities) + ': '
    news += secure_random.choice(high)
    news += secure_random.choice(person)
    news += secure_random.choice(verb)
    news += secure_random.choice(person) 
    news = news[:-1] + '! '
    news += 'its the ' + secure_random.choice(praise) + '!'
    print()
    dramatype(news)
    print()

minx = citiesgps[0][1]
maxy = citiesgps[0][0]
for i in citiesgps:
    if i[1] < minx:
        minx = i[1]
    if i[0] > maxy:
        maxy = i[0]

maxx = citiesgps[0][1]
miny = citiesgps[0][0]
for i in citiesgps:
    if i[1] > maxx:
        maxx = i[1]
    if i[0] < miny:
        miny = i[0]

xpos = minx
ypos = maxy

def drawmap():
    for i in range(maxy+2, miny-2, -1):
        output = ''
        for j in range(minx-2, maxx+2, 1):
            try:
                if [i, j] == [39, -77]:
                    output += '[DC]'
                elif cities[citiesgps.index([i, j])] in owned_stations:
                    output += '[I]'
                elif [i, j] in citiesgps:
                    output += '[c]'
                else:
                    output += ' . '
            except:
                if [i, j] in citiesgps:
                    output += '[c]'
                else:
                    output += ' . '
        print(output)

def distance(city1, city2):
    x = 0
    y = 0
    x = citiesgps[city1][1] - citiesgps[city2][1]
    y = citiesgps[city1][0] - citiesgps[city2][0]
    xy = math.pow(x, 2) + math.pow(y, 2)
    return (math.pow(xy, .5))

owned_stations = []
game = True
dramatype('it is 1923...')
print()
dramatype('you are appointed by the Illuminati (or the Secret Service) a mission of Great Importance.')
print()
dramatype('you are given an unrestricted budget to bring as much of the United States under mass media via radio')
print()
dramatype('as possible. you start with a radio station in Washington DC')
print()
dramatype('. . . . . . . . . . ')
print()
dramatype('you are tasked with 24 turns to make American radio great again!')
print()
print()
dramatype('instructions: type the name of a city to attempt a takeover')
owned_stations.append('washington')
print()

print('(input any key)')
input()

roll = 0
turn = 1
cash = 500
multiplier = 2
while turn <= 24:
    print()
    dramatype('TURN ' + str(turn))
    print()
    drawmap()
    roll = random.randrange(1, 6, 1)
    if roll == 1:
        highnews()
    else:
        lownews()
    response = input().lower()
    if response.startswith(('beer', 'alcohol', 'mead', 'liquor', 'wine')):
        print()
        dramatype('you have been detained by the police.')
        print()
        dramatype('you are released the next day.')
        turn += 1
        print()
    for i in cities:
        if response.startswith(i[:5]):
            print()
            dramatype('you attempt to take over the radio station in ' + str(i))
            print()
            dramatype('. . . . . . . . . .')
            print()
            route = distance(0, cities.index(i))
            
            listeners = 0
            for j in citieslisteners:
                listeners += j
            listenersneeded = int(route * 50000)
            if roll == 1:
                listenersneeded = listenersneeded / multiplier
            if listeners > listenersneeded:
                print()
                if i in owned_stations:
                    print()
                    dramatype('station upgraded')
                    citieslisteners[int(cities.index(i))] += 50000
                else:
                    dramatype('new radio station acquired')
                    citieslisteners[int(cities.index(i))] = 50000
                    print()
                    lookup = cities.index(i)
                    owned_stations.append(cities[lookup])
            else:
                print()
                dramatype('acquisition failed. not enough supporters (' + str(listenersneeded) + ' needed)')
                print()

    totallisteners = 0
    for i in range(len(citieslisteners)):
        citieslisteners[i] = int(citieslisteners[i] * 1.1)
        if citieslisteners[i] > citiespop[i]:
            citieslisteners[i] = citiespop[i]
        totallisteners += citieslisteners[i]
    totalcities = 0
    for i in owned_stations:
        totalcities += 1

    print()
    dramatype('total listeners: ' + str(totallisteners))
    print()
    dramatype('total cities: ' + str(totalcities))
    print()
    print()
    turn += 1

print()
print()
dramatype('~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~')
print()
print()
dramatype('the Illuminati (or Secret Service) evaluates your results...')
print()
dramatype('you prepare ' + str(totallisteners) + ' Americans for Great Struggles to Come in ' + str(totalcities) + ' cities.')
print()
percent = int(100*totallisteners/106000000)
dramatype('(or ' + str(percent) + ' percent of the US population)')
print()
dramatype('. . . . . . . . . . . . . . . . . . .')
print()
print()
