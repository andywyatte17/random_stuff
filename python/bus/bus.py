import argparse
parser = argparse.ArgumentParser(description='Pull tfl bus arrivals info for a specific stop and show the times.')
parser.add_argument('--use-cache', dest='use_cache', action='store_const',
                    const=True, default=False,
                    help='Use a cached fix for the bus-stop info if present.')
parser.add_argument('BusStopID', metavar='N', type=int, nargs=1,
                     help='Bus stop ID whose information you wish to display.')
args = parser.parse_args()
args.N = args.BusStopID[0]

cache_file_name = "." + str(args.N) + ".html"
cache_file = None
if args.use_cache: cache_file = open(cache_file_name,'r')
if not (args.use_cache and cache_file):
    import urllib2
    from io import BytesIO
    f = urllib2.urlopen(R'http://m.countdown.tfl.gov.uk/arrivals/{}'.format(args.N))
    data = f.read()
    with open(cache_file_name, 'wb') as fo:
        fo.write(data)
    cache_file = BytesIO(data)

from bs4 import BeautifulSoup
import html2text
soup = BeautifulSoup(cache_file, 'html.parser')

# Looking for this...
# <li class="live-board-feed-item clearfix" data-destination-id="" data-line-name="123">
for x in soup.find_all("li", class_="live-board-feed-item clearfix"):
    soup2 = BeautifulSoup(str(x), 'html.parser')
    s = html2text.html2text(str(x)).replace("\n", "")
    if len(s)>6: print(s)
