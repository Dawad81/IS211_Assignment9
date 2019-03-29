#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import csv
import json

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
#print soup.prettify()


Player_data = soup.find_all(class_={'row1', 'row2'})
for player in Player_data:
    player_stats0 = player.contents[0].get_text()
    player_stats1 = player.contents[1].get_text()
    player_stats2 = player.contents[2].get_text()
    player_stats3 = player.contents[3].get_text()
    player_stats4 = player.contents[4].get_text()
    player_stats5 = player.contents[5].get_text()
    player_stats6 = player.contents[6].get_text()
    player_stats7 = player.contents[7].get_text()
    player_stats8 = player.contents[8].get_text()
    player_stats9 = player.contents[9].get_text()
    player_stats10 = player.contents[10].get_text()
    print player_stats0
    print player_stats1
    print player_stats2
    print player_stats3
    print player_stats4
    print player_stats5
    print player_stats6
    print player_stats7
    print player_stats8
    print player_stats9
    print player_stats10
#table = soup.find_all('tr', 'td')

#for table_data in table:
#    print table_data
#trs = soup.find_all(class_={})
#for tr in trs:
    #print tr
