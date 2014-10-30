#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import webapp2, urllib2
from google.appengine.api import memcache
from StringIO import StringIO
import ub
import xml.sax
        
class MainPage(webapp2.RequestHandler):
    def cachedGet(self, url):
        return ub.data
        data = memcache.get(url)
        if data is not None:
            logging.info("Using cache...")
            return data
        else:
            logging.info("Downloading...")
            req = urllib2.Request(R'http://ondemand.premier.org.uk/unbelievable/AudioFeed.aspx')
            f = urllib2.urlopen(req)
            data = f.read()
            MAX = 128 * 1024
            if len(data)>MAX: data = data[:MAX]
            memcache.add(url, data)
            return data

    def get(self):
        self.response.headers['Content-Type'] = 'text/xml'
        #self.response.write('Hello, World!')
        
        url = R'http://ondemand.premier.org.uk/unbelievable/AudioFeed.aspx'
        sI = StringIO( self.cachedGet(url) )
        print MyHandler().parse(sI)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
