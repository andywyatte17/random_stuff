#!/bin/python

from BeautifulSoup import BeautifulSoup
from itertools import groupby
import urllib, sys

def GetBusStopText(bus_stop_code, count_limit=1000):
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

  f = urllib.urlopen("http://m.countdown.tfl.gov.uk/arrivals/{}".format(bus_stop_code))
  html = f.read()

  soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)

  count = 0
  rdd = [(route,dir,due) for route, dir, due in zip( grabByClass(soup, "resRoute"),
                        grabByClass(soup, "resDir"),
                        grabByClass(soup, "resDue"))]
  rdd = [list(a[1]) for a in groupby(rdd, key = lambda x : (x[0],x[1]))]
  # rdd = [ [('123','Place','5 mins')], [('179',...), ('179',...)] ]
  rdd = [ (list_items[0][0], list_items[0][1], [x[2] for x in list_items]) for list_items in rdd ]
  # rdd -> [ ('123','Ilford',['5 mins', '8 mins', ...]), ('179'....) ]

  result = ""
  for route,dir,due_list in rdd:
    due = " and ".join(due_list)
    x = "Bus {} towards {} is due in {}.".format(numbersToWords(route),
                                           dir, due.replace("min", "minutes"))
    for _ in range(0,10): x = x.replace("  ", " ")
    x = x.replace("towards", "to")
    x = x.replace("due in due and due", "due now and")
    x = x.replace("due in due and", "due now and")
    x = x.replace("due in due", "due now")
    result = x if result=="" else (result + "\n" + x)
    count += 1
    if count==count_limit: break
  return result

if __name__=='__main__':
  import sys
  print(GetBusStopText(sys.argv[1], int(sys.argv[2])))

