#!/bin/python

import argparse
import StringIO
import re

def parse_characters():
    import characters
    rv = dict()
    x = StringIO.StringIO(characters.people)
    for line in x:
        rx = re.match(R' *([A-Za-z]*) *- *([A-Za-z])?,?([A-Za-z])?,?([A-Za-z])?,?([A-Za-z])?,?([A-Za-z])?,?([A-Za-z])?,?', line)
        if rx:
            c = 0
            name = ''
            for x in rx.groups():
                if c==0:
                    name = x
                    rv[name] = set()
                else:
                    if x:
                        rv[name].add(characters.mapping[x])
                c += 1
    # Add in inferred characteristics
    for name in rv.keys():
        characteristics = rv[name]
        for ik in characters.inferred.keys():
             if 0 == len(ik & characteristics):
                 rv[name].add(characters.inferred[ik])
    return rv

def dump_characters():
    import pprint
    pprint.pprint(parse_characters())
    
def main():
    pass

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Run the Guess Who game')
    parser.add_argument('--dump_characters', dest='dump_characters', action='store_const',
                        const=sum, default=False,
                        help='show information about the characters and exit.')
    args = parser.parse_args()
    if args.dump_characters:
        dump_characters()
        exit(0)
    main()