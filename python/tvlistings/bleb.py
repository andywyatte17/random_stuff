'''
  http://bleb.org/tv/data/rss.php?ch=bbc1&day=1
  http://bleb.org/tv/data/listings/{day}/{ch}.xml  
'''

CHANNELS = '''4music bbc1 bbc2 itv1 itv2 itv3 itv4 ch4 five bbc4  
 cbbc cbeebies challenge citv dave e4 film_four five_us fiver fx 
 ideal_world living_tv more4 watch'''.split(' ')
CHANNELS = [x.replace('\n', '') for x in CHANNELS]
CHANNELS = [x for x in CHANNELS if x!='']
CHANNELS = [x for x in CHANNELS if "sky" not in x]

def url(channel, day_off):
  return R'''http://bleb.org/tv/data/listings/{}/{}.xml'''.format(day_off, channel)

def find(channel, xml, find_type):
  from xml.dom import minidom
  doc = minidom.parseString(xml)
  for type_tag in doc.getElementsByTagName('type'):
    if find_type in type_tag.firstChild.nodeValue:
      import xmltodict
      d = xmltodict.parse(type_tag.parentNode.toxml())
      yield "\t{} - {} - {}".format(channel, d["programme"]["start"], d["programme"]["title"])
