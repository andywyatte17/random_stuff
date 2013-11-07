import os

d = dict()txt_file = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'prime_poker_ranks.txt')
with open(txt_file, 'rb') as f:  for line in f:    if not '#' in line :      bits = line.split(',')      prime = int(bits[0])      value = int(bits[1])      d[prime] = value

primes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43)
flush_prime_suits = ( primes[0]**5, primes[1]**5, primes[2]**5, primes[3]**5 )

def card_to_high_value(card):
  if card=='T': return 10
  if card=='J': return 11
  if card=='Q': return 12
  if card=='K': return 13
  if card=='A': return 14
  return int(card)

def PrimeSuit(card_suit):
  if card_suit=='D' : return primes[0]
  if card_suit=='S' : return primes[1]
  if card_suit=='H' : return primes[2]
  if card_suit=='C' : return primes[3]
  raise RuntimeError('Unexpected card_suit')

def get_card_values(cards):
  prime = 1
  prime_suit = 1
  for card in cards:
    prime = prime * primes[card_to_high_value(card[0])-2]
    prime_suit = prime_suit * PrimeSuit(card[1])
  if prime_suit in flush_prime_suits:
    prime *= primes[13]
  return d[prime]
