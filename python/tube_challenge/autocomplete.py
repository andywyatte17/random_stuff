import os, sys

def get_key():
    import os
    if os.name == 'nt':
        import msvcrt
        while True:
            c = msvcrt.getch()
            if c==b'\r': return '\n'
            if c==b'\x03': quit()
            if c!=None:
                return c.decode('ascii')
    import termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return c

def get_autocomplete_string(autocomplete_fn):
  from sys import stdout
  total = ""
  tabText = None
  tab = -1
  while(True):
    c = get_key()
    # print(ord(c))
    if c=="\n":
      stdout.write("\n")
      stdout.flush()
      break
    elif ord(c)==127 or c=='\b':  # backspace
      tabText = None
      if total != "": total = total[0:-1]
      stdout.write("\b \b")
      stdout.flush()
    elif c=="\t":
      complete_list = autocomplete_fn(total)
      if not complete_list : continue
      tab += 1
      if tab >= len(complete_list) : tab = 0
      nTotal = len(total)
      white = 40 - len(complete_list[tab])
      stdout.write("\r" + complete_list[tab] + " "*white + "\r" + total)
      stdout.flush()
      tabText = complete_list[tab]
    else:
      tabText = None
      tab = -1
      total += c
      white = 40 - len(total)
      stdout.write("\r" + total + " "*white + "\b"*white)
      stdout.flush()
  return tabText if tabText else total 

if __name__=="__main__":
  from sys import stdout
  print("Type in the underground station (tab to autocomplete): ")
  def complete_fn(s):
    if len(s)>=3 and s.lower().startswith("edg"):
      return ["edgware", "edgware road 1", "edgware road 2"]
    if len(s)>=3 and s.lower().startswith("hea"):
      return ["heathrow 1-2-3", "heathrow 4", "heathrow 5"]
    return None
  
  result = get_autocomplete_string(complete_fn)
  print("Result = {}".format(result))