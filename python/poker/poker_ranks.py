'''
    High card - hand_type = hi...lo
    One pair - XXhi?lo
    Two pairs - YYXX.
    Three of a kind - XXX hi.lo
    Straight (number sequence) - hi...lo
    Flush (all same suit) - hi...lo
    Full house - XXX,YY
    Four of a kind - XXXX?
    Straight flush - hi...lo
'''

import pprint
from itertools import groupby

def card_to_high_value(card):
  if card=='J': return 11
  if card=='Q': return 12
  if card=='K': return 13
  if card=='A': return 14
  return int(card)

def card_to_high_value_ace_low(card):
  if card=='J': return 11
  if card=='Q': return 12
  if card=='K': return 13
  if card=='A': return 1
  return int(card)

def distance(card_tup_1, card_tup_2):
  v1 = ( card_to_high_value(card_tup_1[0]), card_to_high_value_ace_low(card_tup_1[0]) )
  v2 = ( card_to_high_value(card_tup_2[0]), card_to_high_value_ace_low(card_tup_2[0]) )
  return min( abs(v1[0]-v2[0]), abs(v1[0]-v2[1]), abs(v1[1]-v2[0]), abs(v1[1]-v2[1]) )

def card_to_high_value_x(card, x):
  if card==x: return 1000
  if card=='J': return 11
  if card=='Q': return 12
  if card=='K': return 13
  if card=='A': return 14
  return int(card)

def card_to_high_value_xy(card, x, y):
  if card==x: return 2000
  if card==y: return 1000
  if card=='J': return 11
  if card=='Q': return 12
  if card=='K': return 13
  if card=='A': return 14
  return int(card)

def group_for_pairs(combin):
  combinS = sorted(combin, key=lambda x : card_to_high_value(x[0]), reverse=True)
  runs = [len(list(group)) for key, group in groupby(combinS, key=lambda x:x[0])]
  return ( runs, combinS )

def is_four_of_kind(combin, g4p):
  if g4p[0]==[4,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][3][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,4]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][4][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv

def is_full_house(combin, g4p):
  if g4p[0]==[3,2]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][0][0]), reverse=True )
    #pprint.pprint( ("is_full_house", rv) )
    return rv
  if g4p[0]==[2,3]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][2][0]), reverse=True )
    #pprint.pprint( ("is_full_house", rv) )
    return rv

def is_flush(combin, g4p):
  for i in range(1,5):
    if combin[i-1][1]!=combin[i][1]:
      return None
  #pprint.pprint( ("flush!", g4p[1]) )
  return g4p[1]

def is_straight(combin, g4p):
  combinS = g4p[1]
  if distance(combinS[0], combinS[4])>5:
    return None
  for i in range(1,5):
    if distance(combinS[i-1], combinS[i])!=1:
      return None
  #pprint.pprint( ("straight!", g4p[1]) )
  return None

def is_straight_flush(combin, g4p):
  straight = is_straight(combin, g4p)
  if straight and is_flush(combin, g4p):
    return straight
  return None

def is_three_of_kind(combin, g4p):
  if g4p[0]==[3,1,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][2][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,3,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][3][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,1,3]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][4][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  return None

def is_two_pairs(combin, g4p):
  if g4p[0]==[1,2,2]:
    rv = sorted(combin, key = lambda x : card_to_high_value_xy(x[0], g4p[1][2][0], g4p[1][4][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[2,1,2]:
    rv = sorted(combin, key = lambda x : card_to_high_value_xy(x[0], g4p[1][1][0], g4p[1][4][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[2,2,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_xy(x[0], g4p[1][0][0], g4p[1][2][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  return None

def is_pair(combin, g4p):
  if g4p[0]==[2,1,1,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][0][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,2,1,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][1][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,1,2,1]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][2][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  if g4p[0]==[1,1,1,2]:
    rv = sorted(combin, key = lambda x : card_to_high_value_x(x[0], g4p[1][3][0]), reverse=True )
    # pprint.pprint( ("is_two_pairs", rv) )
    return rv
  return None

def is_high_card(combin):
  rv = sorted(combin, key = lambda x : card_to_high_value(x[0]), reverse=True )
  # pprint.pprint( ("is_high_card", rv ) )
  return rv

def find_poker_value(combin):
  g4p = group_for_pairs(combin)
  sorted = is_straight_flush(combin, g4p)
  if sorted: return ( 9, "Straight Flush", sorted )
  sorted = is_four_of_kind(combin, g4p)
  if sorted: return ( 8, "Four of a kind", sorted )
  sorted = is_full_house(combin, g4p)
  if sorted: return ( 7, "Full House", sorted )
  sorted = is_four_of_kind(combin, g4p)
  if sorted: return ( 6, "Four of a kind", sorted )
  sorted = is_flush(combin, g4p)
  if sorted: return ( 5, "Flush", sorted )
  sorted = is_straight(combin, g4p)
  if sorted: return ( 4, "Straight", sorted )
  sorted = is_three_of_kind(combin, g4p)
  if sorted: return ( 3, "Three of a kind", sorted )
  sorted = is_two_pairs(combin, g4p)
  if sorted: return ( 2, "Two pairs", sorted )
  sorted = is_pair(combin, g4p)
  if sorted: return ( 1, "Pair", sorted )
  sorted = is_high_card(combin)
  if sorted: return ( 0, "High card", sorted )
