x = ["Alex","Alfred","Anita","Anne","Bernard","Bill","Charles",
        "Claire","David","Eric","Frans","George","Herman","Joe","Maria",
        "Max","Paul","Peter","Philip","Richard","Robert","Sam","Susan","Tom"]

print R"""ListModel {
  id: fruitModel"""

for i in x:
  print '  ListElement {{ name: "{}" }}'.format(i)

print "}"