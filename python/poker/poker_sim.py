import pprint
import itertools
from random import shuffle
from poker_ranks import *

def make_pack():
  pack = list()
  for i in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
    for j in ['Sp','Cb','Dm','Ht']:
      pack.append( (i,j) )
  return pack

def card_value_less(card_pair1, card_pair2):
  # pprint.pprint( ("card_pair1", card_pair1 ) )
  # pprint.pprint( ("card_pair2", card_pair2 ) )
  return card_to_high_value( card_pair1[0] ) < card_to_high_value( card_pair2[0] )

def compare_hand_tuple_less(hand_tuple1, hand_tuple2):
  # pprint.pprint( ("hand_tuple1", hand_tuple1 ) )
  # pprint.pprint( ("hand_tuple2", hand_tuple2 ) )
  if hand_tuple1[0]<hand_tuple2[0]:
    return True
  if hand_tuple2[0]<hand_tuple1[0]:
    return False
  for i in range(0,5):
    if card_value_less( hand_tuple1[2][i], hand_tuple2[2][i] ):
      return False
    if card_value_less( hand_tuple2[2][i], hand_tuple1[2][i] ):
      return True
  return False

def draw_and_remove(pack):
  shuffle( pack )
  draw = pack[0]
  pack.remove(draw)
  return draw

'''
  returns tuple( hand_type, hand_name, card_value_high_to_low )
'''
def hand_poker_value(hand, pool):
  '''
    0 - High card - hand_type = hi...lo
    1 - One pair - XXhi?lo
    2 - Two pairs - YYXX.
    3 - Three of a kind - XXX hi.lo
    4 - Straight (number sequence) - hi...lo
    5 - Flush (all same suit) - hi...lo
    6 - Full house - XXX,YY
    7 - Four of a kind - XXXX?
    8 - Straight flush - hi...lo
  '''
  hand_tuple = None
  hand_plus_pool = list()
  for i in hand[:]: hand_plus_pool.append(i)
  for i in pool[:]: hand_plus_pool.append(i)
  # pprint.pprint( ("hand_plus_pool", hand_plus_pool ) )
  combins = list( itertools.combinations(hand_plus_pool, 5 ) )
  for combin in combins:
    tup = find_poker_value(combin)
    if not hand_tuple or compare_hand_tuple_less(hand_tuple, tup):
      hand_tuple = tup
  return tup

def winning_hand(pack_in, my_hand, pool, no_players):
  if not pool:
    pool = list()
  pack = list( pack_in[:] )
  shuffle( pack )
  while len(pool)<5:
    pool.append( draw_and_remove(pack) )
  # print "Other hands"
  # pprint.pprint( other_hands )
  # print "Pool"
  # pprint.pprint( pool )
  my_hand_value = hand_poker_value(my_hand, pool)
  other_hands = list()
  for i in range(1, no_players):
    other_hand = ( draw_and_remove(pack), draw_and_remove(pack) )
    other_hands.append( ( other_hand, hand_poker_value(other_hand, pool) ) )
  # Compare
  # pprint.pprint( other_hands )
  return ( my_hand, hand_poker_value(my_hand, pool) )

# pprint.pprint(pack)

pack = make_pack()
shuffle( pack )
pprint.pprint( pack )

print "Texas Hold 'Em Simulator"
no_players = 4
print "Number of players =", no_players

my_hand = ( draw_and_remove(pack), draw_and_remove(pack) )
print "Your hand:"
pprint.pprint( my_hand )
print "Number remains:", len(pack)
win_hand = winning_hand(pack, my_hand, None, no_players)
pprint.pprint( ("win_hand", win_hand, win_hand==my_hand) )
