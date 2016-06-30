#!/bin/python

'''
  Make a cpp file with some random binary data.
  Compile it with:
     python binres-builder2.py > binres.cpp
     ls -l binres.cpp
     time clang++ -std=c++11 binres2.cpp
     time g++ binres.cpp
       (14.75 million bytes in ~?? seconds)
'''

import random as R
from random import random
from sys import stdout
from sys import stderr
from binres_core import *

def DataWriter(input, nFile):
  to_encode = [ (x,"\\{:03o}".format(x)) for x in input ]

  # map A-Z,a-z,0-9 to raw ascii char
  for n in range(0, len(to_encode)):
    v = to_encode[n][0]
    if ord('A')<=v and v<=ord('Z') : to_encode[n] = (n,"{:c}".format(v))
    elif ord('a')<=v and v<=ord('z') : to_encode[n] = (n,"{:c}".format(v))
    elif ord('0')<=v and v<=ord('9') : to_encode[n] = (n,"{:c}".format(v))

  # Try optimal octal
  #for n in range(len(to_encode)-2, -1, -1):
  #  v = to_encode[n][0]
  #  c2 = to_encode[n+1][1]
  #  if v<8 and not (ord('0')<=ord(c2[0:1]) and ord(c2[0:1])<=ord('9')):
  #    to_encode[n] = (v, "\\{}".format(v))

  stdout.write('const char* x_{}="'.format(nFile))

  cur_len = 0
  for v in to_encode:
    stdout.write(v[1])
    cur_len += len(v[1])
    if cur_len > 100:
      stdout.write('"\n"')
      cur_len = 0

  print(\
'''";

constexpr unsigned n_{}={};
'''.format(nFile, len(input)))

DumpLoop(DataWriter, hash_code)

