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

def is_four_of_kind(combin):
  return None

def is_full_house(combin):
  return None

def is_three_of_kind(combin):
  return None

def is_flush(combin):
  return None

def is_straight(combin):
  return None

def is_straight_flush(combin):
  straight = is_straight(combin)
  if straight and is_flush(combin):
    return straight
  return None

def is_three_of_kind(combin):
  return None

def is_two_pairs(combin):
  g4p = group_for_pairs(combin)
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

def is_pair(combin):
  return None

def is_high_card(combin):
  rv = sorted(combin, key = lambda x : card_to_high_value(x[0]), reverse=True )
  # pprint.pprint( ("is_high_card", rv ) )
  return rv

def find_poker_value(combin):
  sorted = is_straight_flush(combin)
  if sorted: return ( 9, "Straight Flush", sorted )

  sorted = is_four_of_kind(combin)
  if sorted: return ( 8, "Four of a kind", sorted )

  sorted = is_full_house(combin)
  if sorted: return ( 7, "Full House", sorted )

  sorted = is_four_of_kind(combin)
  if sorted: return ( 6, "Four of a kind", sorted )

  sorted = is_flush(combin)
  if sorted: return ( 5, "Flush", sorted )

  sorted = is_straight(combin)
  if sorted: return ( 4, "Straight", sorted )

  sorted = is_three_of_kind(combin)
  if sorted: return ( 3, "Three of a kind", sorted )

  sorted = is_two_pairs(combin)
  if sorted: return ( 2, "Two pairs", sorted )

  sorted = is_pair(combin)
  if sorted: return ( 1, "Pair", sorted )

  sorted = is_high_card(combin)
  if sorted: return ( 0, "High card", sorted )
