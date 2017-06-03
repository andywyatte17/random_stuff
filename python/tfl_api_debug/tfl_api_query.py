import pickle

def grab_nocache(url):
    import urllib2
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    #print(response.info())
    the_page = response.read()
    return the_page

def unpickle_d():
    try:
        return pickle.load( open( "save.p", "rb" ) )
    except:
        return dict()

def pickle_d(the_dict):
    pickle.dump(the_dict, open( "save.p", "wb" ) )

_pd = None

def grab(url, cache = True):
    global _pd
    if not _pd: _pd = unpickle_d()
    if cache and url in _pd:
        return _pd[url]
    s = grab_nocache(url)
    _pd[url] = s
    pickle_d(_pd)
    return s

