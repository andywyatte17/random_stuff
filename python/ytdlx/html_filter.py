#!\bin\python

def filter(htm):
  import bs4
  from bs4 import Comment
  def dc(tag): return isinstance(tag, Comment)
  soup = bs4.BeautifulSoup(htm, 'html.parser')
  for f in ('script', 'link', 'img', dc):
    for x in soup.find_all(f, recursive=True):
      x.decompose()
  return str(soup)

if __name__=='__main__':
  path = 'The_Relics_of_Time_1_2_Demon_Quest_Doctor_Who_-_BBC_Radio_4_Extra.mp4.htm'
  with open(path, 'rb') as f:
    htm = f.read()
    s = len(htm)
    htm = filter(htm)
    print(s, len(htm))
