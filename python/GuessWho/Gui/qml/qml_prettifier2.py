from qml_prettifier import Prettify
import StringIO, sys

if __name__=='__main__':
    buf = None
    with open(sys.argv[1], 'rb') as f:
        buf = f.read()
    if buf:
        sIO = StringIO.StringIO(buf)
        Prettify(sIO, open(sys.argv[1], 'wb'))
