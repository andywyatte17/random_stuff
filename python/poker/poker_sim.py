import pprint
import itertools
from prime_poker_ranks import get_card_values, card_to_high_value
import sys
from optparse import OptionParser

def hand_as_string(hand, sort):
  hand = hand if not sort else sorted(hand,
                                      key=lambda card: card_to_high_value(card[0]),
                                      reverse=True)
  s = ""
  for part in hand:
    s = s + part[0]
  s = s + ";"
  for part in hand:
    s = s + part[1]
  return s
    
def make_pack():
  pack = list()
  for i in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
    for j in ['S','C','D','H']:
      pack.append( (i,j) )
  return pack

def draw_and_remove(pack, rng):
  draw = pack[ rng.randint(0,len(pack)-1) ]
  pack.remove(draw)
  return draw

def draw_and_remove_value(pack, val):
  for i in pack:
    if i[0]==val:
      draw = i
      pack.remove(i)
      return draw
  return None

def draw_and_remove_value(pack, val, suit):
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

# returns:
# ( best_hand_value... ( ( card1, card2 ), ( ( card1... card5 ), score ) ),
#   my_hand_value...   (..as above..) )
def winning_hand(pack_in, my_hand, pool, no_players, rng):
  if not pool:
    pool = list()
  pack = list( pack_in[:] )
  while len(pool)<5:
    pool.append( draw_and_remove(pack, rng) )
  # print "Other hands"
  # pprint.pprint( other_hands )
  # print "Pool"
  # pprint.pprint( pool )
  my_hand_value = ( my_hand, hand_poker_value(my_hand, pool) )
  other_hands = list()
  for i in range(1, no_players):
    other_hand = ( draw_and_remove(pack, rng), draw_and_remove(pack, rng) )
    other_hands.append( ( other_hand, hand_poker_value(other_hand, pool) ) )
    # pprint.pprint( ("other_hands", other_hands ) )

  best_hand_value = my_hand_value
  for other_hand in other_hands:
    if other_hand[1][1] > my_hand_value[1][1] :
      best_hand_value = other_hand

  return ( best_hand_value, my_hand_value )

def main(runs = 4096, debug_it = False, card_hand="????", no_players=4):
  import random
  rng = random.Random()
  rng.seed(0)

  # pprint.pprint(pack)

  pack = make_pack()
  # pprint.pprint( pack )

  print "Texas Hold 'Em Simulator"
  print "Number of players =", no_players

  if card_hand != '' and card_hand[0]!='?':
    print card_hand
    my_hand = ( draw_and_remove_value(pack, card_hand[0], card_hand[1].upper()),
                draw_and_remove_value(pack, card_hand[2], card_hand[3].upper()) )
  else:
    my_hand = ( draw_and_remove(pack, rng), draw_and_remove(pack, rng) )
    # my_hand = ( draw_and_remove_value(pack, '2', 'H'), draw_and_remove_value(pack, '7', 'S') )
  
  print "Your hand:"
  print hand_as_string(my_hand, False)

  win_count = 0
  lose_count = 0
  end = runs
  display_results_points = []
  for i in range(1,11):
    display_results_points.append( (end*i)/10 )
  
  for i in range(0, end+1):
    win_hand = winning_hand(pack, my_hand, None, no_players, rng)

    if debug_it:
      #print "<"
      #pprint.pprint(win_hand)
      print " Your hand", hand_as_string(win_hand[1][0], True), hand_as_string(win_hand[1][1][0], True)
      if win_hand[1][0]!=win_hand[0][0]:
        print "..Win hand", hand_as_string(win_hand[0][0], True), hand_as_string(win_hand[0][1][0], True)
      #print ">"
      if i==0 : print "Press <enter>"
      raw_input()
    
    if win_hand[0][0]==my_hand:
      win_count = win_count + 1
    else:
      lose_count = lose_count + 1
    if i in display_results_points:
      print "\twin v loss: {0:8d}, {1:8d}, {2:2.2f}%".format(
	    win_count, lose_count, 100.0*win_count / (win_count+lose_count))

if __name__ == "__main__":
  # Heads-up pre-flop odds:
  # http://www.caniwin.com/texasholdem/preflop/heads-up.php
  parser = OptionParser()
  parser.add_option("--profile", "-p", dest="profile", default=False, action="store_true",
                    help="Profile the performance of the program")
  parser.add_option("--debug", "-d", dest="debug_it", default=False, action="store_true",
                    help="Show the results of each hand for debugging")
  parser.add_option("--runs", "-r", dest="runs",
                    help="Perform RUNS number of tests", default=4096, metavar="RUNS")
  parser.add_option("--hand", "", dest="hand",
                    help="Supply a card hand, in the form AdKs", default="????", metavar="CARD_HAND")
  parser.add_option("--no_players", "-n", dest="no_players",
                    help="Number of players", default=4, metavar="NUM_PLAYERS")
  (options, args) = parser.parse_args()
  if options.profile:
    import cProfile
    cProfile.run( 'main({0})'.format( int(options.runs) ) )
  else:
    main( int(options.runs), options.debug_it, options.hand, int(options.no_players) )
