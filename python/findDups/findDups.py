import md5, os, sys
from collections import defaultdict

def hashfile(file, quickHashSize = 0, hashWithFileSize = False):
    m = md5.new()
    if hashWithFileSize:
        hashSizeStr = "%d" % os.path.getsize(file)
        m.update( hashSizeStr )
    with open(file, 'rb') as f:
        BLOCKSIZE = 16 * 1024
        if quickHashSize>0:
            BLOCKSIZE = quickHashSize
        while True:
            block = f.read(BLOCKSIZE)
            if not block: break
            m.update( block )
            if quickHashSize>0:
                break
    return m.hexdigest()

def findDup(parentFolder, is_in_filter):
    # Dups in format {hash[names]}
    dups = defaultdict(list)
    
    # Work out number of dirs/subdirs
    dirCount = 0
    for dirName, subdirs, fileList in os.walk(parentFolder):
        dirCount += 1

    SMALL_HASH = 4096
    # Find first-level hash quickly using first 'SMALL_HASH' bytes of file
    pctLast = -1
    dirCount2 = 0
    for dirName, subdirs, fileList in os.walk(parentFolder):
        dirCount2 += 1
        pct = (dirCount2 * 100) / dirCount
        if pctLast!=pct:
            pctLast = pct
            print('Scanning (%d%%)' % ( pctLast, ) )
        for filename in fileList:
            if not is_in_filter(filename):
                continue
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path, quickHashSize = SMALL_HASH, hashWithFileSize = True)
            # Add or append the file path
            dups[file_hash].append(path)

    dupsNew = defaultdict(list)
    for key in dups.keys():
        if len(dups[key])>1:
            for file in dups[key]:
                hash = hashfile(file)
                dupsNew[hash].append( file )
    
    dupsOut = defaultdict(list)
    for key in dupsNew.keys():
        values = dupsNew[key]
        if len(values)>1:
            dupsOut[key] = values
            
    return dupsOut

def cppFilter(filename):
    return filename.endswith('.cpp')

if __name__=='__main__':
    from pprint import pprint
    dups = findDup(sys.argv[1], cppFilter)
  
    print "\nNumber of dups groups =", len(dups), "\n"
    #for key in dups.keys():
    #    pprint( (key, dups[key]) )
  
    for key in dups.keys():
        filelist = dups[key]
        for i in range(1, len(filelist)+1):
            print "{:3d} - {:s}".format(i, filelist[i-1])
        print "\nFilesize: {:10.5f} MiB".format( os.path.getsize(filelist[0]) / 1000.0**2 )
        raw_input()
