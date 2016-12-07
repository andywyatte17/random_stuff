#!/bin/python

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

def TextForCountdown(busStopID, useCache):
    cache_file_name = "." + str(busStopID) + ".html"
    cache_file = None
    if useCache: cache_file = open(cache_file_name,'r')
    if not (useCache and cache_file):
        from io import BytesIO
        f = urlopen(R'http://m.countdown.tfl.gov.uk/arrivals/{}'.format(busStopID))
        data = f.read()
        with open(cache_file_name, 'wb') as fo:
            fo.write(data)
        cache_file = BytesIO(data)

    from bs4 import BeautifulSoup
    import html2text
    soup = BeautifulSoup(cache_file, 'html.parser')

    # Looking for this...
    # <li class="live-board-feed-item clearfix" data-destination-id="" data-line-name="123">
    results = ""
    for x in soup.find_all("li", class_="live-board-feed-item clearfix"):
        soup2 = BeautifulSoup(str(x), 'html.parser')
        s = html2text.html2text(str(x)).replace("\n", "")
        if len(s)>6: results = results + s + "\n"
    return results

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Pull tfl bus arrivals info for a specific stop and show the times.')
    parser.add_argument('--use-cache', dest='use_cache', action='store_const',
                        const=True, default=False,
                        help='Use a cached fix for the bus-stop info if present.')
    parser.add_argument('BusStopID', metavar='N', type=int, nargs=1,
                         help='Bus stop ID whose information you wish to display.')
    args = parser.parse_args()
    print(TextForCountdown(args.BusStopID[0], args.use_cache))
