#!/bin/python

from itertools import *
import random
import sys

numbers = [4,2,7,1,4,50] # 2]
ops = ['+','-','*','/','(',')',' ']
n = 315

# numbers = [[str(x), '(' + str(x), str(x) + ')'] for x in numbers]

# print(numbers) 

def make_map(bracket_count, op_count):
    d = dict()
    for b in range(1, bracket_count):
        k = 'b' + str(b)
        d[k] = ' ()'[random.randint(0,2)]
        k = 'B' + str(b)
        d[k] = ' ()'[random.randint(0,2)]
    for b in range(1, op_count+1):
        k = 'op' + str(b)
        d[k] = '+*-/'[random.randint(0,3)]
    return d

r = dict()
for count in range(2, len(numbers)+1):
    for p in permutations(numbers, count):
        template = ''
        c = 1
        for x in p:
            template += '~B{}! {} ~b{}! '.format(c, x, c) \
                        .replace('~','{').replace('!','}')
            if c < count:
                template += ' ~op{}! '.format(c) \
                        .replace('~','{').replace('!','}')
            c += 1
        # print(template)
        # sys.exit(0)

        for x in range(0, 1000):
            m = make_map(c, c-1)
            t = template.format(**m)
            try:
                e = eval(t)
                if e>0 and not e in r:
                    r[e] = t.replace(' ','')
                    # print('{} = {}'.format(e,r[e]))
                    print(sorted(r.keys()))
            except:
                continue

# ,1, a ,2,
# ,1, a ,2, b ,3,
# ,1, a ,2, b ,3, c ,4,
 
