import json
from sys import stdout

js = json.loads( open("/tmp/moor_park.txt", "r").read() )

for x in (0,1,2,3,4,5,6,7):
  name, knownJourneys = None, None
  try:
    name = js["timetable"]["routes"][0]["schedules"][x]["name"]
    knownJourneys = js["timetable"]["routes"][0]["schedules"][x]["knownJourneys"]
  except:
    pass
  if not (name and knownJourneys):
    continue
  print(name)
  n = 0
  for kj in knownJourneys:
    stdout.write("{:02d}:{:02d} ".format(int(kj["hour"]), int(kj["minute"])))
    n += 1
    if n==12:
      n = 0
      stdout.write("\n")
  if n!=0: stdout.write("\n")

