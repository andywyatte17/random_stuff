import characters,  StringIO,  re

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
