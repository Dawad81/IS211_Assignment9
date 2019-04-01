#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module parses the NASDAQ.com site for apples historical closing
stock prices, for last 3 months. """


import urllib2
from bs4 import BeautifulSoup


URL = 'https://www.nasdaq.com/symbol/aapl/historical'
PAGE = urllib2.urlopen(URL)
SOUP = BeautifulSoup(PAGE.read(), 'lxml')
TABLE_DATA = SOUP.tr
TABLE_DATA.decompose()
APPLE_DATA = SOUP.find_all('tbody')

print '*=' * 30
print
print 'Apples\' stock closing prices for the last 90 days.'
print
print '*=' * 30
print

for table in APPLE_DATA:
    table_rows = table.find_all('tr')
    for row in table_rows:
        table_data = row.find_all('td')
        date = table_data[0].get_text()
        closing = table_data[4].get_text()
        print 'Apples\' stock closing price for {} was {}'.format(
            date.strip(), closing.strip())
        print
