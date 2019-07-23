import cog, glob, os
from collections import OrderedDict

def make_source_map():
  m = {}
  sn = OrderedDict()
  for x in glob.glob('**/*.cpp', recursive=True):
    dn = os.path.dirname(x)
    if dn not in m:
      sn[dn] = 'SOURCE_' + dn
      m[dn] = 'set(' + sn[dn] + ' '
    m[dn] = m[dn] + '"' + x + '" '
  return m, sn

def gen_sources():
  m, sn = make_source_map()
  cog.outl()
  for k in m:
    m[k] += ")"
    cog.outl(m[k])
  cog.outl()

def gen_source_list(library_name):
  m, sn = make_source_map()
  cog.outl()
  cog.out("add_library(" + library_name + ' ')
  for k in sn:
    cog.out('${' + sn[k] + '} ')
  cog.outl(')')
  cog.outl('')
