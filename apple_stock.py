#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import json

url = 'https://www.nasdaq.com/symbol/aapl/historical'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')
#print soup.prettify()
tabledata= soup.tr
tabledata.decompose()
apple_data = soup.find_all('tbody')
#print apple_data
for table in apple_data:
    table_rows = table.find_all('tr')
    for row in table_rows:
        table_data = row.find_all('td')
        date= table_data[0].get_text()
        closing= table_data[4].get_text()
        print 'Apples closing price for {} was {}'.format(date.strip(), closing.strip())



        #print table_data.contents[0].get_text()
        #print table_data
#trs = apple_data.find_all('tr')
#print trs
#for tr in trs:
    #print tr
    #tds = tr.find_all('td')
    #print tds
    #for td in tds:
    #tds= tr.find('td')
        #for td in tr:
        #date=tds[0].get_text()
        #print date

