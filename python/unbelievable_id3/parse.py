#!/bin/python

from lxml import etree
from pprint import pprint
import bz2
root = etree.parse(open('Unbelievable.xml'))
count = 1
for x in root.iter('item'):
  title = x.find('title').text
  link = x.find('link').text
  print '{:3d}'.format(count), title + '\n\t' + link
  count += 1
  if count==20:
    break
