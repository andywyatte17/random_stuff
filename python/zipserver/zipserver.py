import SimpleHTTPServer
import SocketServer
import zipfile
import pprint
from urlparse import urlparse
import json
import sys
from random import shuffle

'''
{
  "zipFiles":["cppreference-doc-20120620.zip"],
  "root":"cppreference-doc-20120620",
  "rootHtml":"/cppreference-doc-20120620/reference/en.cppreference.com/w/index.html"
}
'''

zipFiles = []
root = ''
rootHtml = ''

def ProbableRoot(nl):
    indexHtmlLoc = []
    for x in nl:
        if x.endswith('index.htm') or x.endswith('index.html'):
            indexHtmlLoc.append(x)
    if len(indexHtmlLoc)<1 :
        return '?'
    return min(indexHtmlLoc, key=lambda x: len(x))
        
def ParseConfig():
    global root
    global zipFiles
    global rootHtml
    jsonPath = sys.argv[2]
    with open(jsonPath, 'r') as f:
        js = json.load(f)
        for zf in js['zipFiles']:
            zipFiles.append( (zf, zipfile.ZipFile(zf, 'r') ) )
        root = js['root']
        rootHtml = js['rootHtml']
    pprint.pprint(zipFiles)
    print "root", root
    print "rootHtml", rootHtml

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def sendAs(self, path, contentType):
        print("sendAs", path, contentType)
        global zipFiles
        global root
        if not path.startswith('/') :
            path = '/' + path
        altPath = root + path
        altPath = altPath.encode('utf8')
        print "\naltPath",altPath,"\n"
        for zfp,zf in zipFiles :
            try:
                with zf.open(altPath, 'r') as f:
                    self.send_response(200)
                    self.send_header('Content-type', contentType)
                    self.end_headers()
                    self.wfile.write(f.read())
            except:
                pass
        self.send_error(404)

    def do_GET(self):
        print "\ndo_GET:" + self.path + "\n"
        o = urlparse(self.path)
        # print "path=", o.path

        if o.path == '/':
            self.send_response(301)
            self.send_header('Location', rootHtml)
            self.end_headers()
            return
        if o.path.endswith(".html") or o.path.endswith(".htm"):
            self.sendAs(o.path, 'text/html')
            return
        if o.path.endswith(".css"):
            self.sendAs(o.path, 'text/css')
            return
        if o.path.endswith(".js"):
            self.sendAs(o.path, 'application/javascript')
            return
        if o.path.endswith(".png"): 
            self.sendAs(o.path, 'image/png')
            return
        if o.path.endswith(".jpg") or o.path.endswith(".jpeg"): 
            self.sendAs(o.path, 'image/jpeg')
            return
        self.sendAs(o.path, 'application/octet-stream')
        return

ParseConfig()
for zfp,zf in zipFiles:
    print "Zipfile:", zfp, len(zf.namelist())
    nl = list(zf.namelist())
    for i in range(0,10):
       print "  {0}".format(nl[(i * len(nl)-1) / 9] )
    print "Probably root:", ProbableRoot(nl)
    print "\n"

theport = int(sys.argv[1])
Handler = MyHandler
pywebserver = SocketServer.TCPServer(("", theport), Handler)

print "Python based web server. Serving at port", theport
pywebserver.serve_forever()