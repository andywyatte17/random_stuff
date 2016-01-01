import BaseHTTPServer
import subprocess
from SimpleHTTPServer import SimpleHTTPRequestHandler
import threading

# ...

def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    while 1:
        httpd.handle_request()

# ...

def start_abcde():
    subprocess.call(["abcde", "-N", "-o mp3"], stdout=open('abcde.txt', 'w'))

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, a, b, c):
        SimpleHTTPRequestHandler.__init__(self, a, b, c)
        self.this_thread = None

    def do_GET(self):
        if self.path.endswith('abcde'):
            t = threading.Thread(target=start_abcde)
            t.start()
            self.this_thread = t
            DUMMY_RESPONSE = "<html><head></head><body>CD Ripping Started.</body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(DUMMY_RESPONSE))
            self.end_headers()
            self.wfile.write(DUMMY_RESPONSE)
            return
        return SimpleHTTPRequestHandler.do_GET(self)

# ...
            
run_while_true(handler_class = MyHandler)
