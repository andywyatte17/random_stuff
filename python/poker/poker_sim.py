import pprint
import itertools
from random import shuffle
from prime_poker_ranks import get_card_values
import sys
from optparse import OptionParser

def make_pack():
  pack = list()
  for i in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
    for j in ['S','C','D','H']:
      pack.append( (i,j) )
  return pack

def draw_and_remove(pack):
  shuffle( pack )
  draw = pack[0]
  pack.remove(draw)
  return draw

def draw_and_remove_value(pack, val):
  shuffle( pack )
  for i in pack:
    if i[0]==val:
      draw = i
      pack.remove(i)
      return draw
  return None

def draw_and_remove_value(pack, val, suit):
  shuffle( pack )
  for i in pack:
    if i[0]==val and i[1]==suit:
      draw = i
      pack.remove(i)
      return draw
  return None

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
  best_value = 0
  for combin in combins:
    new_value = get_card_values(combin)
    if not hand_tuple or new_value > best_value:
      hand_tuple = combin
      best_value = new_value
  return ( hand_tuple, best_value )

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
  my_hand_value = ( my_hand, hand_poker_value(my_hand, pool) )
  other_hands = list()
  for i in range(1, no_players):
    other_hand = ( draw_and_remove(pack), draw_and_remove(pack) )
    other_hands.append( ( other_hand, hand_poker_value(other_hand, pool) ) )
    # pprint.pprint( ("other_hands", other_hands ) )

  best_hand_value = my_hand_value
  for other_hand in other_hands:
    if other_hand[1][1] > my_hand_value[1][1] :
      best_hand_value = other_hand

  return ( best_hand_value, my_hand_value )

def main(runs = 4096):
  # pprint.pprint(pack)

  pack = make_pack()
  shuffle( pack )
  # pprint.pprint( pack )

  print "Texas Hold 'Em Simulator"
  no_players = 4
  print "Number of players =", no_players

  # my_hand = ( draw_and_remove(pack), draw_and_remove(pack)
  my_hand = ( draw_and_remove_value(pack, '2', 'H'), draw_and_remove_value(pack, '7', 'S') )
  print "Your hand:"
  pprint.pprint( my_hand )
  print "Number remains:", len(pack)

  win_count = 0
  lose_count = 0
  end = runs
  for i in range(0, end+1):
    win_hand = winning_hand(pack, my_hand, None, no_players)
    #print "<"
    #pprint.pprint( win_hand )
    #print ">"
    if win_hand[0][0]==my_hand:
      win_count = win_count + 1
    else:
      lose_count = lose_count + 1
    if i==end or ((i%512)==511):
      pprint.pprint( ("win v loss", win_count, lose_count, "{0}%".format(100.0*win_count / (win_count+lose_count))) )

if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option("--profile", "-p", dest="profile", default=False, action="store_true",
                    help="Profile the performance of the program")
  parser.add_option("--runs", "-r", dest="runs",
                    help="Perform RUNS number of tests", default=4096, metavar="RUNS")
  (options, args) = parser.parse_args()
  if options.profile:
    import cProfile
    cProfile.run( 'main({0})'.format( int(options.runs) ) )
  else:
    main( int(options.runs) )
