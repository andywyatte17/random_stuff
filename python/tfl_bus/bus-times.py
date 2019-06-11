#!/usr/bin/env python3

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests                     # pip install requests
from bs4 import BeautifulSoup       # pip install bs4

def GetFromStop():
    r = requests.request(url='https://tfl.gov.uk/bus/stop/490014169E/wolsey-avenue', method='GET')
    html = r.text
    soup = BeautifulSoup(html, features='html.parser')
    x = ""
    for script in soup.findAll("div", {"class": "live-board initial-board-container bus"}):
        x += str(script)
    return x

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("""<html>
<head>
<script>
function mySubmit()
{
}
</script>
</head>
<body>
<input type="text" name="fname">
<input type="submit" value="Submit" onclick="mySubmit()">
{the-stops}
</body>
</html>""".replace("{the-stops}", GetFromStop()).encode('utf-8'))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()