#!/bin/python

from BeautifulSoup import BeautifulSoup
from itertools import groupby
import urllib, sys

NUMBERS = ("oh","one","two","three","four","five","six","seven","eight","nine")

def grabByClass(soup, className):
  return [x.getText().lstrip().rstrip() for x in soup.findAll("td",{"class":className})]

def numbersToWords(s):
  for a,b in ( ("1"," one "), ("2"," two "), ("3"," three "), ("4"," four "),
               ("5"," five "), ("6"," six "), ("7"," seven "), ("8"," eight "),
               ("9"," nine "), ("0"," oh ") ):
    s = s.replace(a,b)
  # Group two-word numbers like "one four" back to "14"
  return s

f = urllib.urlopen("http://m.countdown.tfl.gov.uk/arrivals/%s" % sys.argv[1])
html = f.read()

soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)

count = 0
rdd = [(route,dir,due) for route, dir, due in zip( grabByClass(soup, "resRoute"),
                            grabByClass(soup, "resDir"),
                            grabByClass(soup, "resDue"))]
rdd = [list(a[1]) for a in groupby(rdd, key = lambda x : (x[0],x[1]))]
# rdd = [ [('123','Place','5 mins')], [('179',...), ('179',...)] ]
rdd = [ (list_items[0][0], list_items[0][1], [x[2] for x in list_items]) for list_items in rdd ]

for route,dir,due_list in rdd:
  due = " and ".join(due_list)
  x = "Bus {} towards {} is due in {}.".format(numbersToWords(route),
                                               dir, due.replace("min", "minutes"))
  for _ in range(0,10): x = x.replace("  ", " ")
  x = x.replace("towards", "to")
  x = x.replace("due in due and due", "due now and")
  x = x.replace("due in due and", "due now and")
  x = x.replace("due in due", "due now")
  print(x)
  count += 1
  if count==int(sys.argv[2]): break
