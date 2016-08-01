import underground_gps
import os

n = -1
for stationName, lati, longi in underground_gps.gps:
  n += 1
  print(stationName)
  url = underground_gps.latlon2OpenStreetmapTileUrl(lati, longi, 17)
  os.system('cd /tmp && curl "{}" > {}.png'.format(url, stationName))

