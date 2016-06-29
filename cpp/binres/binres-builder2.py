#!/bin/python
'''
  Make a cpp file with some random binary data.
  Compile it with:
     python binres-builder2.py > binres.cpp
     ls -l binres.cpp
     time g++ binres.cpp
       (14.75 million bytes in ~?? seconds)
'''

import random as R
from random import random
from sys import stdout
from sys import stderr

R.seed(0)
def ur8(): return R.randint(0,255)
to_encode = [ ur8() for x in range(0,2000000) ]
#to_encode = [ ur8() for x in range(0,200000) ]

for nFile in range(0,10000000):
  size = min(R.randint(1000,5000), len(to_encode))
  if size==0: break
  part = to_encode[0:size]
  to_encode = to_encode[size:]

  part = list( (x,"\\x{:02x}".format(x)) for x in part )

  # map A-Z,a-z,0-9 to raw ascii char
  for n in range(0, len(part)):
    v = part[n][0]
    if ord('A')<=v and v<=ord('Z') : part[n] = (n,"{:c}".format(v))
    elif ord('a')<=v and v<=ord('z') : part[n] = (n,"{:c}".format(v))
    elif ord('0')<=v and v<=ord('9') : part[n] = (n,"{:c}".format(v))

  # Try octal
  for n in range(0, len(part)-1):
    c2 = part[n+1][1]
    if n<8 and not (0<=ord(c2[0:1]) and ord(c2[0:1])<=9):
      part[n] = (n,"\\{}".format(n))

  stdout.write('const char* x_{}="q'.format(nFile))

  for b in range(0,size):
    stdout.write(part[b][1])
  print("\";\n")
print("\nint main() { return 0; }")

