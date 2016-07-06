#!/bin/python

import random as R
from sys import argv

def DJB(data):
  import numpy as np
  hash = np.uint32(5381);
  for x in data:
    hash = hash * np.uint32(31) + np.uint32(x)
  return hash

def DumpLoop(fn, hash_code):
  N = 2000000
  try: N = int(argv[1])
  except: pass

  R.seed(0)
  def ur8(): return R.randint(0,255)
  to_encode = [ ur8() for x in range(0,N) ]

  for nFile in range(0,10000000):
    size = min(R.randint(1000,5000), len(to_encode))
    if size==0: break
    head = to_encode[0:size]
    to_encode = to_encode[size:]
    fn(head, nFile)
    print("\nconstexpr unsigned djb_{} = 0x{:08x};\n".format(nFile, DJB(head)))

  print("\n{}\n".format(hash_code))
  print(\
'''

#include <stdio.h>

int main() {
  printf("hash(%d)=0x%08x\\n", 0, hash(0));
  printf("djb(%d)=0x%08x\\n", 0, djb_0);
  return 0;
}
''')

hash_code = \
'''
#include <stdint.h>
#include <stdio.h>

uint32_t hash(int x)
{
  uint32_t hash = 5381;
  for(int i = 0; i<n_0; ++i)
    hash = hash*31 + (uint8_t)x_0[i];
  return hash;
}
'''