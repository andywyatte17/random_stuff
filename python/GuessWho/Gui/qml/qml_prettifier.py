import sys

INDENT = 2

def Prettify(f, out):
    indent = 0
    for line in f:
        line = line.lstrip(' ')
        if line[0]=='\n' and indent>0:
            continue
        if line[0]=='}':
            line = ' '*((indent-1)*INDENT) + line
        else:
            line = ' '*(indent*INDENT) + line
        openers = line.count('{')
        closers = line.count('}')
        indent += (openers - closers)
        out.write(line)

if __name__=='__main__':
    with open(sys.argv[1], 'r') as f:
        Prettify( f, sys.stdout )