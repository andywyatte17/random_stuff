import urllib2
import autocomplete
import station_data
from autocomplete import get_autocomplete_string
from bs4 import BeautifulSoup

R"""
https://tfl.gov.uk/tube/timetable/northern?FromId=940GZZLUFYC&fromText=&toText=&ToId=940GZZLUKNG

<span class="label">Depart</span>
<span class="time">05:56</span>
</div>
<div class="arrive">
<span class="visually-hidden">and</span>
<span class="label">Arrive</span>
<span class="time">06:31</span>
"""


class GetStation:
  def __init__(self, stationData):
    self.stationData = stationData
    self.stations = [(x,x.lower()) for x in stationData.AllStations()]

  def autocomplete_fn(self, test):
    if len(test)<3:
      return None
    test = test.lower()
    result = []
    for x in self.stations:
      if x[1].startswith(test):
        result.append(x[0])
    result = list(set(result)) # remove duplicates
    return result

  def get(self):
    ac = get_autocomplete_string( lambda x : self.autocomplete_fn(x) )
    return self.stationData.LookupStation(ac, True)


def autocomplete_fn(x):
  x = x.lower()
  result = []
  for v in [ "northern", "victoria", "jubilee", "district", "central", "piccadilly", "metropolitan",
             "hammersmith-city", "circle", "bakerloo" ]:
    if v.startswith(x):
      result.append(v)
  return result


def ToMins(hhmm):
  return 60 * int(hhmm[0:2]) + int(hhmm[3:5])


def ExtractDepartArrive(html_data):
  soup = BeautifulSoup(html_data, "lxml")
  depart = None
  arrive = Nonepy
  for span in soup.find_all("span"):
    cl = span.get("class")
    if cl == ["label"]:
      last_label = span.string
    if cl == ["time"]:
      if last_label == "Depart": depart = span.string
      if last_label == "Arrive": arrive = span.string
    if depart and arrive:
      return (ToMins(arrive) - ToMins(depart))
  return None


if __name__=="__main__":
  stationData = station_data.StationData()
  getStation = GetStation(stationData)
  while True:
    print("\nfrom?")
    sidFrom = stationData.GetStationIDFromName( getStation.get() )
    print(sidFrom)
    print("to?")
    sidTo = stationData.GetStationIDFromName( getStation.get() )
    print(sidTo)
    print("which?")
    which = get_autocomplete_string( autocomplete_fn )

    url = """https://tfl.gov.uk/tube/timetable/{}?FromId={}&fromText=X&toText=Y&ToId={}""" \
           .format(which, sidFrom, sidTo)
    print(url)
    f = urllib2.urlopen(url)
    print(ExtractDepartArrive( f.read() ))
    #print(ExtractDepartArrive(open("/tmp/n.html", "r").read()))
