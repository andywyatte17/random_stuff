URL = 'http://ondemand.premier.org.uk/unbelievable/AudioFeed.aspx'
LOCAL_NAME = 'Unbelievable.xml'

import httplib, urllib2, os

def downloadIfNecessary():
  httplib.HTTPConnection.debuglevel = 1
  
  request = urllib2.Request(URL)
  request.add_header('Accept-encoding', 'gzip')
  opener = urllib2.build_opener()
  f = opener.open(request)
  content_length = int(f.headers['Content-Length'])
  
  def OldLength():
    try:  
      return os.path.getsize(LOCAL_NAME)
    except:
      return -1
  
  if OldLength() != content_length:
    print 'Downloading - content is updated'
    data = f.read()
    with open(LOCAL_NAME, 'wb') as fOut:
      fOut.write(data)
    return
  
  print 'No need to download - content is unchanged'
  return

try:
  downloadIfNecessary()
except urllib2.HTTPError as e:
  print str(e)
