import SimpleHTTPServer
import SocketServer
import logging
import cgi
import datetime
from pprint import pprint

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST_op(self, path):
        if( path=='/right' ):
            print 'Do right!'
        if( path=='/left' ):
            print 'Do left!'

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.do_POST_op( self.path )
        self.send_response(200)
        self.send_header('Content-type','text')
        self.end_headers()
        self.wfile.write( self.path )

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()