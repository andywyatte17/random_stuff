import BeautifulSoup
from css import style
import urllib2
import time
import sys

'''
Scrape up html from live.dartsdata.com, which shows match darts live scores.

Usage:
python scraper.py 130935
  where '130935' corresponds to the game id. Find this by browsing to
    live.dartsdata.com.
'''

URL = """http://live.dartsdata.com/MatchView.aspx?MatchId={}""".format(sys.argv[1])
lastText = None
for x in range(1,10000):
    time.sleep(5)
    lastH = "{}_{}.htm".format(sys.argv[1], x-1)
    thisH = "{}_{}.htm".format(sys.argv[1], x)
    nextH = "{}_{}.htm".format(sys.argv[1], x+1)
    response = urllib2.urlopen(URL)
    html = response.read()
    # print(html)

    soup = BeautifulSoup.BeautifulSoup(html)

    theDiv = soup.find('div', {'id':'conMainContent_conPageContent_ucMatchPlayerSegment1_pnlScore'})
    theDiv2 = soup.find('div', {'id':'conMainContent_conPageContent_ucMatchPlayerSegment2_pnlScore'})
    #print(theDiv)
    #print(theDiv2)

    thisText = """<html>
<head>
{style}
</head>
<body>
_lastH_
_nextH_
{body}
{body2}
</body>
</html>""".format(style=style,body=theDiv,body2=theDiv2)

    if lastText and lastText==thisText: continue
    lastText = thisText
    thisText = thisText.replace("_lastH_", """<a class="button" href={}>Last</a>""".format(lastH))
    thisText = thisText.replace("_nextH_", """<a class="button" href={}>Next</a>""".format(nextH))
    o = open(thisH, 'w')
    o.write(thisText)

