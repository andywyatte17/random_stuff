import ub
import xml.sax

class MyHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        pass

    def parse(self, f):
        xml.sax.parse(f, self)
        return self._result

    def characters(self, data):
        print "\t"+data

    def startElement(self, name, attrs):
        print name

    def endElement(self, name):
        print "~"+name

if __name__=='__main__':
    mh = MyHandler()
    try:
        xml.sax.parseString( ub.data, mh )
    except: pass
    print mh._result
