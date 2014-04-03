import SimpleHTTPServer
import SocketServer
import zipfile
import pprint
from urlparse import urlparse
import json
import sys
from random import shuffle
import argparse
import os, time, stat
from filecache import FileCache

'''
{
  "zipFiles":["cppreference-doc-20120620.zip"],
  "root":"cppreference-doc-20120620",
  "rootHtml":"/cppreference-doc-20120620/reference/en.cppreference.com/w/index.html"
}
'''

cache = FileCache()
theport = 1234
debugZips = False
zipFiles = []
root = ''
rootHtml = ''
CONTENT_TYPES = { ".htm":'text/html', ".html":'text/html', \
  ".svg":"image/svg+xml", ".png":"image/png", ".css":'text/css',
  ".js":'application/javascript', 
  ".jpg":'image/jpeg', ".jpeg":'image/jpeg'
}

def ParseConfig():
    global debugZips
    global root
    global zipFiles
    global rootHtml
    global theport
    parser = argparse.ArgumentParser(description='Run a web server, serving files from a zip file')
    parser.add_argument('port', metavar='port', type=int, help='a port number on which files will be served.')
    parser.add_argument('json_config_file', metavar='json_config_file', type=str,\
      help='a json-format configuration file giving details about location of zip files and other settings.')
    parser.add_argument('--debugZips', dest='debugZips', action='store_true', default=False, \
      help='Show some debugging information about the zips passed in json_config_file and exit.')
    args = parser.parse_args()
    theport = args.port
    jsonPath = args.json_config_file
    debugZips = args.debugZips
    with open(jsonPath, 'r') as f:
        js = json.load(f)
        for zf in js['zipFiles']:
            zipFiles.append( (zf, zipfile.ZipFile(zf, 'r'), os.stat(zf)[stat.ST_MTIME] ) )
        root = js['root']
        rootHtml = js['rootHtml']
    # pprint.pprint(zipFiles)
    # print "root", root
    # print "rootHtml", rootHtml

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def SendAs(self, path, contentType):
        global cache
        global zipFiles
        global root
        if not path.startswith('/') :
            path = '/' + path
        altPath = root + path
        altPath = altPath.encode('utf8')
        #print "\naltPath",altPath,"\n"
        someBytes, mtime = cache.IsInCache(altPath)
        if someBytes:
            dbxAltPath = altPath
            if len(dbxAltPath)>30:
                dbxAltPath = "..."+dbxAltPath[-26:]
            print "\nServing cached content - {0}\n".format(dbxAltPath)
            self.send_response(200)
            self.send_header('Content-type', contentType)
            self.send_header('Last-Modified', self.date_time_string(mtime))
            self.end_headers()
            self.wfile.write(someBytes)
            return
        for zfp,zf,zfMTime in zipFiles :
            try:
                with zf.open(altPath, 'r') as f:
                    self.send_response(200)
                    self.send_header('Content-type', contentType)
                    self.send_header('Last-Modified', self.date_time_string(zfMTime))
                    print self.date_time_string(zfMTime)
                    self.end_headers()
                    someBytes = f.read()
                    self.wfile.write(someBytes)
                    cache.CacheIfRelevant(altPath, someBytes, zfMTime)
                    return
            except KeyError as e:
                pass
        self.send_error(404)

    def do_GET(self):
        # print "\ndo_GET:" + self.path + "\n"
        o = urlparse(self.path)
        # print "path=", o.path

        if o.path == '/':
            self.send_response(301)
            self.send_header('Location', rootHtml)
            self.end_headers()
            return
        for key in CONTENT_TYPES.iterkeys():
            if o.path.endswith(key):
                self.SendAs(o.path, CONTENT_TYPES[key])
                return
        self.SendAs(o.path, 'application/octet-stream')
        return

def DebugZips():
    s = "DebugZips"
    print "\n" + s + "\n" + "-" * len(s)
    for zfp,zf,zfMTime in zipFiles:
        print "Zipfile:", zfp, len(zf.namelist()), "\n"
        print "index.htm(l):"
        for x in zf.namelist():
            if x.find('/index.')>=0:
                print "\t{0}".format(x)
        print "\nfolders:"
        folderSet = set()
        for x in zf.namelist():
            head, tail = os.path.split(x)
            folderSet.add(head)
        for x in folderSet:
            print "\t" + x
    print "\n"

def main():
    ParseConfig()
    if debugZips:
        DebugZips()
        exit(0)
        return

    Handler = MyHandler
    pywebserver = SocketServer.TCPServer(("", theport), Handler)
    
    print "Python based web server. Serving at port", theport
    pywebserver.serve_forever()

if __name__ == "__main__":
    main()