#!/bin/python
'''
  Make a cpp file with some random binary data.
  Compile it with:
     python binres-builder.py > binres.cpp
     ls -l binres.cpp
     time g++ binres.cpp
       (14.75 million bytes in ~12 seconds)
'''
import random as R
from random import random
from sys import stdout
from sys import stderr

R.seed(0)
def ur8(): return R.randint(0,255)
to_encode = [ ur8() for x in range(0,2000000) ]

for nFile in range(0,10000000):
  size = min(R.randint(1000,5000), len(to_encode))
  if size==0: break
  part = to_encode[0:size]
  to_encode = to_encode[size:]
  print("const unsigned char x_{}[]={{".format(nFile))
  last = size-1
  for b in range(0,size):
    term = ", " if b!=last else ""
    stdout.write("0x{:02x}{}".format(part[b], term))
    if ((b%10)==9) : stdout.write("\n")
  print("};\n")
print("\nint main() { return 0; }")

