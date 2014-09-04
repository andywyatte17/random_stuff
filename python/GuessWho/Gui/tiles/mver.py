import os
for i in range(5,24):
  src = "GuessWho_{:03d}.jpg".format(i)
  print src
  dst = raw_input()
  cmd = "git mv {} {}.jpg".format(src, dst)
  print "\t{}".format(cmd)
  os.system(cmd)

