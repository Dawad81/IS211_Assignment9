#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module Parses the CBSsports.com NFL stats, for the top 20 players
according to most touchdowns as of 2018."""


import urllib2
from bs4 import BeautifulSoup


URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-' \
      'regular-category-touchdowns'
PAGE = urllib2.urlopen(URL)
SOUP = BeautifulSoup(PAGE.read(), 'lxml')

print '*=' * 30
print
print '2018\'s Top 20 players in the NFL, according to Touchdowns.'
print
print '*=' * 30
print

PLAYER_DATA = SOUP.find_all(class_={'row1', 'row2'})
TOP20 = PLAYER_DATA[:20]
for player in TOP20:
    player_name = player.contents[0].get_text()
    player_position = player.contents[1].get_text()
    player_team = player.contents[2].get_text()
    player_tds = player.contents[6].get_text()
    print '{} is on the {} team. He plays at the position of {}. He has ' \
          'scored {} touchdowns.'.format(player_name, player_team,
                                         player_position, player_tds)

    print
