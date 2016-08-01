import json
import sys

js = json.loads(open(sys.argv[1], "r").read())

pks = set()

def recurse(parent_keys, js, s):
  if not ( parent_keys in pks ) :
    print(parent_keys)
    pks.add(parent_keys)
  if isinstance(js, dict):
    for k in js.keys():
      recurse( parent_keys + (k,), js[k], s + "  ")
  if isinstance(js, list):
    for v in js:
      try:
        recurse( parent_keys + ("<list>",), v, s + "  ")
      except: pass

recurse( tuple(), js, "  ")
