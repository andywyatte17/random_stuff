import sys
import pprint

TOTAL = 9178578
PROG = (2**8)-1
lastPct = ""
n = 0
pageStart = 0
pageStartsEnds = list()
NBIG=2**31
nForLast = NBIG
found = list()
filterWords = ["computers","programming"]

def print_stderr(str):
  sys.stderr.write(str + "\n")

def LineCount(fname):
  rv = 0
  with open(sys.argv[1], 'r') as f:
    for line in f:
      rv = rv + 1
  return rv

def ProgressWrite(a,b,last):
  s = "{0}%".format( int((a*100.0)/b) )
  s = s + len(s)*"\b"
  if last==s:
    return last
  sys.stderr.write(s)
  sys.stderr.flush()
  return s

TOTAL = LineCount(sys.argv[1])

print_stderr("\nSearching...")

with open(sys.argv[1], 'r') as f:
  for line in f:
    lineLC = line.lower()
    for x in filterWords:
      if lineLC.find(x)>=0:
        if nForLast>n:
          # print n
          found.append(n)
          nForLast = pageStart
        break
    if lineLC.find('<page>')>=0:
      pageStart = n
      nForLast = NBIG
      #print " 0x{0:08x}".format(n)
    if lineLC.find('</page>')>=0:
      pageStartsEnds.append( (pageStart,n) )
      nForLast = NBIG
      #print "/0x{0:08x}".format(n)
    if (n & PROG)==PROG :
      lastPct = ProgressWrite(n, TOTAL, lastPct)
      #print "@ {0:x}".format(n)
      pass
    n = n + 1

print_stderr("\n")

#pprint.pprint(pageStartsEnds)

print_stderr("\n\nFinding ranges...")

ranges = list()
jc = 0
lastPct = ""
for j in found:
  lastPct = ProgressWrite(jc, len(found), lastPct)
  # print jc, len(found)
  jc=jc+1
  for i in pageStartsEnds:
    if i[0]<=j and j<=i[1]:
      ranges.append(i)
      break

print_stderr("\n")

# pprint.pprint(ranges)

n = 0
with open(sys.argv[1], 'r') as f:
  for line in f:
    for lh in ranges:
      if lh[0]<=n and n<=lh[1]:
        print(line.strip('\n'))
    n = n + 1