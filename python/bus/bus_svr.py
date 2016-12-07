import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from bus import *

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        text = 'No Info'
        import re
        m = re.search(r'/([0-9]{5})', str(s.path))
        if m:
            text = str(m.group(1))
            text = TextForCountdown(text, False)
        s.wfile.write( \
r'''<html><head></head>
<body style="font-size: 30pt;">
<pre style="font-size: 20pt;">
{}
</pre>

<script type="text/javascript">
  function goToPage() {{
    var page = document.getElementById('page').value;
    window.location = "/" + page;
  }}
</script>

<form action="javascript:goToPage();">
  <input type="text" id="page"
         style="font-size:25pt;" />
  <input type="submit" value="submit"
         style="font-size:25pt;" />
</form>
</body>
</html>'''.format(text).encode('utf-8'))

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
