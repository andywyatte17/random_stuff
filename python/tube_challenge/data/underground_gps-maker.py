s = open("underground_gps.py.txt", "r").read()
lines = s.split("\n")
_1 = lines[1::5]
_2 = lines[2::5]
_3 = lines[3::5]
_1 = [x[2:] for x in _1]
_2 = [x[2:] for x in _2]
_3 = [x[2:] for x in _3]
from pprint import pprint
#pprint(_1)
#pprint(_2)
#pprint(_3)
for a,b,c in zip(_1,_2,_3):
  print("  " + str((a,b,c)) + ",")
