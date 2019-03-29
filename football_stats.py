#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import json

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')



Player_data = soup.find_all(class_={'row1', 'row2'})
for player in Player_data:
    player_name = player.contents[0].get_text()
    player_position = player.contents[1].get_text()
    player_team = player.contents[2].get_text()
    player_tds = player.contents[6].get_text()

    #print player_name
    #print player_position
    #print player_team
    #print player_tds

    PlayerDict = {'Name': player_name, 'Team': player_team, 'Players Position': player_position, 'Touchdowns': player_tds}

    print PlayerDict
