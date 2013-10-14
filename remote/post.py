import SimpleHTTPServer
import SocketServer
import logging
import cgi
import datetime
from pprint import pprint


PORT = 8000

SendKeyIsWin32 = False
try:
    import win32com.client
    SendKeyIsWin32 = True
except: 
    pass

def SendKey(keys):
    if SendKeyIsWin32:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(keys, 0)
    return

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST_op(self, path):
        if( path=='/right' ):
            SendKey("{RIGHT}")
        if( path=='/left' ):
            SendKey("{LEFT}")

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.do_POST_op( self.path )

        length = int( self.headers['Content-Length'] )
        post_data = self.rfile.read(length).decode('utf-8')
        print post_data

        self.send_response(200)
        self.send_header('Content-type','text')
        self.end_headers()
        self.wfile.write( self.path )

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()