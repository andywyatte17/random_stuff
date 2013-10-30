import pprint
from random import shuffle

def make_pack():
  pack = list()
  for i in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
    for j in ['Sp','Cb','Dm','Ht']:
      pack.append( (i,j) )
  return pack

def card_string_as_number(card_value):
  cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
  for i in range(0, len(cards)):
    if cards[i]==card_value:
      return i
  return -1

def card_value_less(card_pair1, card_pair2):
  return card_string_as_number( card_pair1[0] ) < card_string_as_number( card_pair2[0] )

def compare_hand_tuple_less(hand_tuple1, hand_tuple2):
  if hand_tuple1[0]<hand_tuple2[0]:
    return True
  if hand_tuple2[0]<hand_tuple1[0]:
    return False
  for i in range(0,5):
    if card_value_less( hand_tuple1[i], hand_tuple2[i] ):
      return False
    if card_value_less( hand_tuple2[i], hand_tuple1[i] ):
      return True
  return False

def draw_and_remove(pack, number):
  shuffle( pack )
  draw = list( pack[0:number] )
  for item in draw:
    pack.remove(item)
  return draw

'''
  returns tuple( hand_type, hand_name, card_value_high_to_low )
'''
def hand_poker_value(hand, pool):
  '''
    High card - hand_type = 1
    One pair
    Two pairs
    Three of a kind
    Straight (number sequence)
    Flush (all same suit)
    Four of a kind
    Straight flush - hand_type = 8
  '''
  hand_tuple = None
  for i in 

def winning_hand(pack_in, my_hand, pool, no_players):
  if not pool:
    pool = list()
  pack = list( pack_in[:] )
  shuffle( pack )
  while len(pool)<5:
    pool.append( draw_and_remove(pack, 1) )
  # print "Other hands"
  # pprint.pprint( other_hands )
  # print "Pool"
  # pprint.pprint( pool )
  my_hand_value = hand_poker_value(my_hand, pool)
  other_hands = list()
  for i in range(1, no_players):
    other_hand = draw_and_remove(pack, 2)
    other_hands.append( ( other_hand, hand_poker_value(other_hand, pool) ) )
  # Compare
  pprint.pprint( other_hands )
  return ( my_hand, hand_poker_value(my_hand, pool) )

# pprint.pprint(pack)

pack = make_pack()
shuffle( pack )
pprint.pprint( pack )

print "Texas Hold 'Em Simulator"
no_players = 4
print "Number of players =", no_players

my_hand = draw_and_remove(pack, 2)
print "Your hand:"
pprint.pprint( my_hand )
print "Number remains:", len(pack)
win_hand = winning_hand(pack, my_hand, None, no_players)
print winning_hand, win_hand==my_hand
