#!/usr/bin/env python3
'''
mmind.py
Mastermind Game
'''

import random
import sys

class Code:
  def __init__(self, code=None):
    self.code = code if code!=None else [random.randint(1,6) for x in range(4)]
    self.code2 = set(enumerate(self.code))

  def guess(self, guessString):
    guess = [int(x) for x in guessString \
            if ord('1') <= ord(x) and \
                 ord(x) <= ord('6')]
    guess2 = set([x for x in enumerate(guess)])
    xm = len(self.code2.intersection(guess2))
    c = self.code2.difference(guess2)
    g = guess2.difference(self.code2)
    pm = 0
    for i in g:
      for j in c:
        if i[1]==j[1]:
          c.remove(j)
          pm += 1
          break
    return (4-xm-pm, pm, xm)

code = Code()

assert Code([2, 6, 6, 1]).guess("1122") == (2, 2, 0), Code([2, 6, 6, 1]).guess("1122")
assert Code([1, 2, 3, 4]).guess("1234") == (0, 0, 4), Code([1, 2, 3, 4]).guess("1234")
assert Code([1, 1, 2, 2]).guess("2211") == (0, 4, 0), Code([1, 1, 2, 2]).guess("2211")
assert Code([1, 1, 2, 3]).guess("5211") == (1, 3, 0), Code([1, 1, 2, 3]).guess("5211")

print(r"""Mastermind game.

The computer has chosen her code.
Repeatedly try to guess the code by typing in a
4-digit number such as 1356, ie using digits 1-6.

The count of exact-, partial- and none-matching symbols
will display with the symbols X,/,. respectively.
""")

for nGuess in range(1,1000):
  guessString = input("    ")
  if guessString=='': sys.exit(0)
  if guessString=='show':
    print("    {}".format(code.code))
    continue
  nm, pm, xm = code.guess(guessString)
  print("{:2d}: {}".format(nGuess, '.'*nm + '/'*pm + 'X'*xm))
  if (nm, pm, xm) == (0, 0, 4):
    print('You won!')
    sys.exit(0)
