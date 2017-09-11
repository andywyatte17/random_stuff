import glob, os
import sys

def CleanupTmp():
    for f in glob.glob("tmp\\*"): os.remove(f)
    os.rmdir("tmp")

try: CleanupTmp()
except: pass

for x in glob.glob("*.zip"):
    try: os.mkdir("tmp")
    except: pass
    os.system('7z e -otmp "{}"'.format(x))
    # sys.exit(0)
    os.system('7z a -y "{}".7z tmp\\*'.format(x))
    CleanupTmp()
    # sys.exit(0)