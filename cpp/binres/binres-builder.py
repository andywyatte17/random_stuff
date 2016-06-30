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
from sys import argv
from binres_core import *

def DataWriter(to_encode, nFile):
  print("constexpr unsigned char x_{}[]={{".format(nFile))
  size = len(to_encode)
  last = size-1
  for b in range(0,size):
    term = "," if b!=last else ""
    stdout.write("0x{:02x}{}".format(to_encode[b], term))
    if ((b%10)==9) : stdout.write("\n")
  print(\
'''}};

constexpr unsigned n_{}={};
'''.format(nFile, len(to_encode)))

DumpLoop(DataWriter, hash_code)