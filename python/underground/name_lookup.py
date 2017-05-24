NAME_LOOKUP = {
  "King's Cross St Pancras":"King's Cross St.Pancras",
  "South Wimbledon (Merton)":"South Wimbledon",
  "Totteridge and Whetstone":"Totteridge & Whetstone",
  "Euston Underground Station":"Euston",
  "St Paul's":"St.Paul's"
}

OFFICIAL_NAMES = set(("King's Cross St.Pancras",))

def convert(n):
  if n in NAME_LOOKUP:
    return NAME_LOOKUP[n]
  return n
