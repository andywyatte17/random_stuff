import pprint

MAX_CACHE_SIZE = 256 * 1024

class FileCache:
    def __init__(self):
        self.cache = dict()
        self.incrementer = 0

    def IsInCache(self, path):
        if path in self.cache:
            tup = self.cache[path]
            return ( tup[1], tup[3] )
        return ( None, None )

    def TrimCache(self):
        while True:
            carryOn = False
            byteCount = 0
            for t in self.cache:
               if t[1]: byteCount = byteCount + len(t[1])
            if byteCount < MAX_CACHE_SIZE:
                return
            # remove cached item with lowest incrementer (t[2])
            incrementerMax = 1<<32
            keyToUse = None
            for key,value in self.cache.items():
                if value[1] and value[2] < incrementerMax:
                    incrementerMax = value[2]
                    keyToUse = key
            if keyToUse:
                t = self.cache[keyToUse]
                t = ( t[0], None, t[2], t[3] )
                self.cache[keyTouse] = t

    def CacheIfRelevant(self, path, theBytes, mtime):
        self.incrementer = self.incrementer + 1
        if not path in self.cache:
            self.cache[path] = (1, None, self.incrementer, mtime)
            return
        tup = self.cache[path]
        tup = (tup[0]+1, theBytes, self.incrementer, tup[3])
        self.cache[path] = tup
        self.TrimCache()
