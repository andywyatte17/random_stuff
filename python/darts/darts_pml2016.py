#!/bin/python
import os, sys
from pprint import pprint
os.chdir(os.path.dirname(sys.argv[0]))

tmp_darts = "/tmp/darts.txt"
cmd = "bash darts_pml2016.sh {} > {}".format(sys.argv[1], tmp_darts)
#os.system( cmd )

# filters lines from tmp_darts
lines = [line.lstrip().rstrip() for line in open(tmp_darts, "r").readlines()]
x = 0
while x < len(lines):
  if (x%2)==1 and lines[x][:5]=="https":
    lines.insert(x, "???")
    x -= 1
  else:
    x += 1
  
lines = [(lines[i],lines[i+1]) for i in range(0,len(lines),2)]
lines = [x for x in lines if ("2016" in x[1]) and (" {}".format(sys.argv[1]) in x[1])]

for x in range(0,len(lines)):
  print("{:3d} - {}\n      {}".format(x, lines[x][0], lines[x][1]))
print "Which videos? ",
nums = [int(x.strip("\n")) for x in sys.stdin.readline().split(" ")]
for x in nums:
  os.system('python -m youtube_dl --format 18 "{}"'.format(lines[x][0]))

