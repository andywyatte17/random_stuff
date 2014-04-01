import SimpleHTTPServer
import SocketServer
import zipfile
import pprint
from urlparse import urlparse

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def sendAs(self, path, contentType):
        global zf
        global root
        if not path.startswith('/') :
            path = '/' + path
        altPath = root + path
        #print "\n\n" + altPath + "\n\n"
        with zf.open(altPath, 'r') as f:
            self.send_response(200)
            self.send_header('Content-type', contentType)
            self.end_headers()
            self.wfile.write(f.read())

    def do_GET(self):
        print "\ndo_GET:" + self.path + "\n"
        o = urlparse(self.path)
        print "path=", o.path

        if o.path == '/':
            self.send_response(301)
            self.send_header('Location', rootHtml)
            self.end_headers()
            return
        if o.path.endswith(".html"):
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
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

zf = zipfile.ZipFile('cppreference-doc-20120620.zip', 'r')
root = 'cppreference-doc-20120620'
rootHtml = '/cppreference-doc-20120620/reference/en.cppreference.com/w/index.html'
#pprint.pprint(zf.namelist())
theport = 1234
Handler = myHandler
pywebserver = SocketServer.TCPServer(("", theport), Handler)

print "Python based web server. Serving at port", theport
pywebserver.serve_forever()