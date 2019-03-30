#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module parses the NASDAQ.com site for apples historical closing
stock prices, for last 3 months. """


import urllib2
from bs4 import BeautifulSoup


url = 'https://www.nasdaq.com/symbol/aapl/historical'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
tabledata = soup.tr
tabledata.decompose()
apple_data = soup.find_all('tbody')

for table in apple_data:
    table_rows = table.find_all('tr')
    for row in table_rows:
        table_data = row.find_all('td')
        date = table_data[0].get_text()
        closing = table_data[4].get_text()
        print 'Apples closing price for {} was {}'.format(
            date.strip(), closing.strip())
        print
