from django.test import TestCase
#!/usr/bin/python
#coding -*- coding: utf-8 -*-
from xml.etree.ElementTree import ElementTree
from urllib import urlopen
import MySQLdb
import datetime
xml = ElementTree(file=urlopen('http://xurrency.com/jpy/feed'))

rss = 'http://purl.org/rss/1.0/'
dc = 'http://purl.org/dc/elements/1.1/'

con = MySQLdb.connect(db="exchange", host="127.0.0.1", port=3306, user='root')

base_sql = 'insert into currencies(base, target, value, inverse, created, modified)values("%(base)s", "%(target)s", %(value)f, %(inverse)f, "%(date)s", now());';

for items in xml.findall('.//{' + rss + '}item'):
    currency = {}
    for item in items.getiterator():
        if item.tag == '{' + dc + '}value':
            currency['value'] = float(item.text)
        if item.tag == '{' + dc + '}baseCurrency':
            currency['base'] = item.text
        if item.tag == '{' + dc + '}targetCurrency':
            currency['target'] = item.text
        if item.tag == '{' + dc + '}date':
            currency['date'] = datetime.datetime.strptime(item.text, "%a %b %d %H:%M:%S UTC %Y")
    currency['inverse'] = 1.0 / currency['value']

    sql = base_sql%{'base':currency['base'], 'target':currency['target'], 'value':currency['value'], 'inverse':currency['inverse'], 'date':currency['date']}
    cur = con.cursor()
    cur.execute(sql)

con.commit()