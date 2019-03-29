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
    player_stats = str(player.get_text())
    print player_stats
#table = soup.find_all('tr', 'td')

#for table_data in table:
#    print table_data
#trs = soup.find_all(class_={})
#for tr in trs:
    #print tr
