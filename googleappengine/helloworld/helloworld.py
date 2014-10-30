import webapp2, urllib2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml'
        #self.response.write('Hello, World!')
        
        req = urllib2.Request(R'http://ondemand.premier.org.uk/unbelievable/AudioFeed.aspx')
        f = urllib2.urlopen(req)
        self.response.write(f.read(1024))        

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
