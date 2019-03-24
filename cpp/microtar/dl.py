import urllib.request

c = urllib.request.urlopen("https://raw.githubusercontent.com/rxi/microtar/master/src/microtar.c").read()
h = urllib.request.urlopen("https://raw.githubusercontent.com/rxi/microtar/master/src/microtar.h").read()
open("microtar.c", "wb").write(c)
open("microtar.h", "wb").write(h)
