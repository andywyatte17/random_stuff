from poker_ranks import *
from pprint import pprint

def make(str):
  rv = list()
  for bits in str.split(';'):
    bits2 = bits.split(',')
    rv.append( (bits2[0], bits2[1]) )
  return rv

s = "A,Sp;J,Dm;10,Dm;J,Cb;A,Ht"
pprint( ("is_two_pairs", s, is_two_pairs( make(s) ) ) )
s = "A,Sp;J,Dm;10,Dm;4,Cb;A,Ht"
pprint( ("is_two_pairs", s, is_two_pairs( make(s) ) ) )
