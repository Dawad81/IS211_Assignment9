#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import json

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
print '*=' * 30
print
print '2018\'s Top 20 players in the NFL, according to Touchdowns.'
print
print '*=' * 30
print

Player_data = soup.find_all(class_={'row1', 'row2'})
top20 = Player_data[:20]
for player in top20:
    player_name = player.contents[0].get_text()
    player_position = player.contents[1].get_text()
    player_team = player.contents[2].get_text()
    player_tds = player.contents[6].get_text()
    print '{} is on the {} team. He plays at the position of {}. He has ' \
          'scored {} touchdowns.'.format(
        player_name, player_team, player_position, player_tds)

    PlayerDict = {'Name': player_name,
                  'Team': player_team,
                  'Players Position': player_position,
                  'Touchdowns': player_tds}


    #print json.dumps(PlayerDict, sort_keys=True)
    print
