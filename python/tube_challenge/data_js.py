import Levenshtein # python -m pip install --user python-Levenshtein

# Originally from https://gist.githubusercontent.com/i-like-robots/a4608cbdf21d979d9452/raw/2e5ef08a303f774d5e870138bdcb0fe5528c8606/data.js

class Printable:
  def __repr__(self):
    from pprint import pformat
    return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=2, width=1)

class _Exports(Printable):
  pass

_exports = _Exports()

_exports.lines = {
  "bakerloo": "Bakerloo",
  "central": "Central",
  "circle": "Circle",
  "district": "District",
  "hammersmith-city": "Hammersmith & City",
  "jubilee": "Jubilee",
  "metropolitan": "Metropolitan",
  "northern": "Northern",
  "piccadilly": "Piccadilly",
  "victoria": "Victoria",
  "waterloo-city": "Waterloo & City"
}

_exports.stations = {
  "940GZZLUBST": "Baker Street",
  "940GZZLUCHX": "Charing Cross",
  "940GZZLUEAC": "Elephant & Castle",
  "940GZZLUEMB": "Embankment",
  "940GZZLUERB": "Edgware Road (Bakerloo)",
  "940GZZLUHAW": "Harrow & Wealdstone",
  "940GZZLUHSN": "Harlesden",
  "940GZZLUKEN": "Kenton",
  "940GZZLUKPK": "Kilburn Park",
  "940GZZLUKSL": "Kensal Green",
  "940GZZLULBN": "Lambeth North",
  "940GZZLUMVL": "Maida Vale",
  "940GZZLUMYB": "Marylebone",
  "940GZZLUNWY": "North Wembley",
  "940GZZLUOXC": "Oxford Circus",
  "940GZZLUPAC": "Paddington",
  "940GZZLUPCC": "Piccadilly Circus",
  "940GZZLUQPS": "Queen's Park",
  "940GZZLURGP": "Regent's Park",
  "940GZZLUSGP": "Stonebridge Park",
  "940GZZLUSKT": "South Kenton",
  "940GZZLUWJN": "Willesden Junction",
  "940GZZLUWKA": "Warwick Avenue",
  "940GZZLUWLO": "Waterloo",
  "940GZZLUWYC": "Wembley Central",
  "940GZZLUADE": "Aldgate East",
  "940GZZLUBBB": "Bromley-by-Bow",
  "940GZZLUBBN": "Barbican",
  "940GZZLUBKG": "Barking",
  "940GZZLUBWR": "Bow Road",
  "940GZZLUEHM": "East Ham",
  "940GZZLUERC": "Edgware Road (Circle Line)",
  "940GZZLUESQ": "Euston Square",
  "940GZZLUFCN": "Farringdon",
  "940GZZLUGHK": "Goldhawk Road",
  "940GZZLUGPS": "Great Portland Street",
  "940GZZLUHSC": "Hammersmith (H&C Line)",
  "940GZZLUKSX": "King's Cross St. Pancras",
  "940GZZLULAD": "Ladbroke Grove",
  "940GZZLULRD": "Latimer Road",
  "940GZZLULVT": "Liverpool Street",
  "940GZZLUMED": "Mile End",
  "940GZZLUMGT": "Moorgate",
  "940GZZLUPAH": "Paddington (H&C Line)-Underground",
  "940GZZLUPLW": "Plaistow",
  "940GZZLURYO": "Royal Oak",
  "940GZZLUSBM": "Shepherd's Bush Market",
  "940GZZLUSGN": "Stepney Green",
  "940GZZLUUPK": "Upton Park",
  "940GZZLUWHM": "West Ham",
  "940GZZLUWLA": "Wood Lane",
  "940GZZLUWPL": "Whitechapel",
  "940GZZLUWSP": "Westbourne Park",
  "940GZZLUBMY": "Bermondsey",
  "940GZZLUBND": "Bond Street",
  "940GZZLUCGT": "Canning Town",
  "940GZZLUCPK": "Canons Park",
  "940GZZLUCWR": "Canada Water",
  "940GZZLUCYF": "Canary Wharf",
  "940GZZLUDOH": "Dollis Hill",
  "940GZZLUFYR": "Finchley Road",
  "940GZZLUGPK": "Green Park",
  "940GZZLUKBN": "Kilburn",
  "940GZZLUKBY": "Kingsbury",
  "940GZZLULNB": "London Bridge",
  "940GZZLUNDN": "Neasden",
  "940GZZLUNGW": "North Greenwich",
  "940GZZLUQBY": "Queensbury",
  "940GZZLUSJW": "St. John's Wood",
  "940GZZLUSTD": "Stratford",
  "940GZZLUSTM": "Stanmore",
  "940GZZLUSWC": "Swiss Cottage",
  "940GZZLUSWK": "Southwark",
  "940GZZLUWHP": "West Hampstead",
  "940GZZLUWIG": "Willesden Green",
  "940GZZLUWSM": "Westminster",
  "940GZZLUWYP": "Wembley Park",
  "940GZZLUBKE": "Barkingside",
  "940GZZLUBKH": "Buckhurst Hill",
  "940GZZLUBLG": "Bethnal Green",
  "940GZZLUBNK": "Bank",
  "940GZZLUCHL": "Chancery Lane",
  "940GZZLUCWL": "Chigwell",
  "940GZZLUDBN": "Debden",
  "940GZZLUEAN": "East Acton",
  "940GZZLUEBY": "Ealing Broadway",
  "940GZZLUEPG": "Epping",
  "940GZZLUFLP": "Fairlop",
  "940GZZLUGFD": "Greenford",
  "940GZZLUGGH": "Grange Hill",
  "940GZZLUGTH": "Gants Hill",
  "940GZZLUHBN": "Holborn",
  "940GZZLUHGR": "Hanger Lane",
  "940GZZLUHLT": "Hainault",
  "940GZZLUHPK": "Holland Park",
  "940GZZLULGN": "Loughton",
  "940GZZLULGT": "Lancaster Gate",
  "940GZZLULYN": "Leyton",
  "940GZZLULYS": "Leytonstone",
  "940GZZLUMBA": "Marble Arch",
  "940GZZLUNAN": "North Acton",
  "940GZZLUNBP": "Newbury Park",
  "940GZZLUNHG": "Notting Hill Gate",
  "940GZZLUNHT": "Northolt",
  "940GZZLUPVL": "Perivale",
  "940GZZLUQWY": "Queensway",
  "940GZZLURBG": "Redbridge",
  "940GZZLURSG": "Ruislip Gardens",
  "940GZZLURVY": "Roding Valley",
  "940GZZLUSBC": "Shepherd's Bush (Central)",
  "940GZZLUSNB": "Snaresbrook",
  "940GZZLUSPU": "St. Paul's",
  "940GZZLUSRP": "South Ruislip",
  "940GZZLUSWF": "South Woodford",
  "940GZZLUTCR": "Tottenham Court Road",
  "940GZZLUTHB": "Theydon Bois",
  "940GZZLUWCY": "White City",
  "940GZZLUWOF": "Woodford",
  "940GZZLUWRP": "West Ruislip",
  "940GZZLUWSD": "Wanstead",
  "940GZZLUWTA": "West Acton",
  "940GZZLUALD": "Aldgate",
  "940GZZLUBKF": "Blackfriars",
  "940GZZLUBWT": "Bayswater",
  "940GZZLUCST": "Cannon Street",
  "940GZZLUECT": "Earl's Court",
  "940GZZLUGTR": "Gloucester Road",
  "940GZZLUHSK": "High Street Kensington",
  "940GZZLUMMT": "Monument",
  "940GZZLUMSH": "Mansion House",
  "940GZZLUSJP": "St. James's Park",
  "940GZZLUSKS": "South Kensington",
  "940GZZLUSSQ": "Sloane Square",
  "940GZZLUTMP": "Temple",
  "940GZZLUTWH": "Tower Hill",
  "940GZZLUVIC": "Victoria",
  "940GZZLUACT": "Acton Town",
  "940GZZLUBEC": "Becontree",
  "940GZZLUBSC": "Barons Court",
  "940GZZLUCWP": "Chiswick Park",
  "940GZZLUDGE": "Dagenham East",
  "940GZZLUDGY": "Dagenham Heathway",
  "940GZZLUECM": "Ealing Common",
  "940GZZLUEPK": "Elm Park",
  "940GZZLUEPY": "East Putney",
  "940GZZLUFBY": "Fulham Broadway",
  "940GZZLUGBY": "Gunnersbury",
  "940GZZLUHCH": "Hornchurch",
  "940GZZLUHSD": "Hammersmith (Dist&Picc Line)",
  "940GZZLUKOY": "Kensington (Olympia)",
  "940GZZLUKWG": "Kew Gardens",
  "940GZZLUPSG": "Parsons Green",
  "940GZZLUPYB": "Putney Bridge",
  "940GZZLURMD": "Richmond",
  "940GZZLURVP": "Ravenscourt Park",
  "940GZZLUSFB": "Stamford Brook",
  "940GZZLUSFS": "Southfields",
  "940GZZLUTNG": "Turnham Green",
  "940GZZLUUPB": "Upminster Bridge",
  "940GZZLUUPM": "Upminster",
  "940GZZLUUPY": "Upney",
  "940GZZLUWBN": "West Brompton",
  "940GZZLUWIM": "Wimbledon",
  "940GZZLUWIP": "Wimbledon Park",
  "940GZZLUWKN": "West Kensington",
  "940GZZLUAMS": "Amersham",
  "940GZZLUCAL": "Chalfont & Latimer",
  "940GZZLUCSM": "Chesham",
  "940GZZLUCXY": "Croxley",
  "940GZZLUCYD": "Chorleywood",
  "940GZZLUEAE": "Eastcote",
  "940GZZLUHGD": "Hillingdon",
  "940GZZLUHOH": "Harrow-on-the-Hill",
  "940GZZLUICK": "Ickenham",
  "940GZZLUMPK": "Moor Park",
  "940GZZLUNHA": "North Harrow",
  "940GZZLUNKP": "Northwick Park",
  "940GZZLUNOW": "Northwood",
  "940GZZLUNWH": "Northwood Hills",
  "940GZZLUPNR": "Pinner",
  "940GZZLUPRD": "Preston Road",
  "940GZZLURKW": "Rickmansworth",
  "940GZZLURSM": "Ruislip Manor",
  "940GZZLURSP": "Ruislip",
  "940GZZLURYL": "Rayners Lane",
  "940GZZLUUXB": "Uxbridge",
  "940GZZLUWAF": "Watford",
  "940GZZLUWHW": "West Harrow",
  "940GZZLUBLR": "Blackhorse Road",
  "940GZZLUBXN": "Brixton",
  "940GZZLUEUS": "Euston",
  "940GZZLUFPK": "Finsbury Park",
  "940GZZLUHAI": "Highbury & Islington",
  "940GZZLUPCO": "Pimlico",
  "940GZZLUSKW": "Stockwell",
  "940GZZLUSVS": "Seven Sisters",
  "940GZZLUTMH": "Tottenham Hale",
  "940GZZLUVXL": "Vauxhall",
  "940GZZLUWRR": "Warren Street",
  "940GZZLUWWL": "Walthamstow Central",
  "940GZZLUACY": "Archway",
  "940GZZLUAGL": "Angel",
  "940GZZLUBLM": "Balham",
  "940GZZLUBOR": "Borough",
  "940GZZLUBTK": "Burnt Oak",
  "940GZZLUBTX": "Brent Cross",
  "940GZZLUBZP": "Belsize Park",
  "940GZZLUCFM": "Chalk Farm",
  "940GZZLUCND": "Colindale",
  "940GZZLUCPC": "Clapham Common",
  "940GZZLUCPN": "Clapham North",
  "940GZZLUCPS": "Clapham South",
  "940GZZLUCSD": "Colliers Wood",
  "940GZZLUCTN": "Camden Town",
  "940GZZLUEFY": "East Finchley",
  "940GZZLUEGW": "Edgware",
  "940GZZLUFYC": "Finchley Central",
  "940GZZLUGDG": "Goodge Street",
  "940GZZLUGGN": "Golders Green",
  "940GZZLUHBT": "High Barnet",
  "940GZZLUHCL": "Hendon Central",
  "940GZZLUHGT": "Highgate",
  "940GZZLUHTD": "Hampstead",
  "940GZZLUKNG": "Kennington",
  "940GZZLUKSH": "Kentish Town",
  "940GZZLULSQ": "Leicester Square",
  "940GZZLUMDN": "Morden",
  "940GZZLUMHL": "Mill Hill East",
  "940GZZLUMTC": "Mornington Crescent",
  "940GZZLUODS": "Old Street",
  "940GZZLUOVL": "Oval",
  "940GZZLUSWN": "South Wimbledon",
  "940GZZLUTAW": "Totteridge & Whetstone",
  "940GZZLUTBC": "Tooting Bec",
  "940GZZLUTBY": "Tooting Broadway",
  "940GZZLUTFP": "Tufnell Park",
  "940GZZLUWFN": "West Finchley",
  "940GZZLUWOP": "Woodside Park",
  "910GENFCOAK": "Oakwood Station",
  "940GZZLUALP": "Alperton",
  "940GZZLUASG": "Arnos Grove",
  "940GZZLUASL": "Arsenal",
  "940GZZLUBDS": "Bounds Green",
  "940GZZLUBOS": "Boston Manor",
  "940GZZLUCAR": "Caledonian Road",
  "940GZZLUCGN": "Covent Garden",
  "940GZZLUCKS": "Cockfosters",
  "940GZZLUHNX": "Hatton Cross",
  "940GZZLUHPC": "Hyde Park Corner",
  "940GZZLUHR4": "Heathrow Terminal 4",
  "940GZZLUHR5": "Heathrow Terminal 5",
  "940GZZLUHRC": "Heathrow Terminals 1-2-3",
  "940GZZLUHWC": "Hounslow Central",
  "940GZZLUHWE": "Hounslow East",
  "940GZZLUHWT": "Hounslow West",
  "940GZZLUHWY": "Holloway Road",
  "940GZZLUKNB": "Knightsbridge",
  "940GZZLUMRH": "Manor House",
  "940GZZLUNEN": "North Ealing",
  "940GZZLUNFD": "Northfields",
  "940GZZLUOAK": "Oakwood",
  "940GZZLUOSY": "Osterley",
  "940GZZLUPKR": "Park Royal",
  "940GZZLURSQ": "Russell Square",
  "940GZZLUSEA": "South Ealing",
  "940GZZLUSGT": "Southgate",
  "940GZZLUSHH": "South Harrow",
  "940GZZLUSUH": "Sudbury Hill",
  "940GZZLUSUT": "Sudbury Town",
  "940GZZLUTPN": "Turnpike Lane",
  "940GZZLUWOG": "Wood Green"
}

_exports.stationsOnLines = {
  "bakerloo": [
    "940GZZLUBST",
    "940GZZLUCHX",
    "940GZZLUEAC",
    "940GZZLUEMB",
    "940GZZLUERB",
    "940GZZLUHAW",
    "940GZZLUHSN",
    "940GZZLUKEN",
    "940GZZLUKPK",
    "940GZZLUKSL",
    "940GZZLULBN",
    "940GZZLUMVL",
    "940GZZLUMYB",
    "940GZZLUNWY",
    "940GZZLUOXC",
    "940GZZLUPAC",
    "940GZZLUPCC",
    "940GZZLUQPS",
    "940GZZLURGP",
    "940GZZLUSGP",
    "940GZZLUSKT",
    "940GZZLUWJN",
    "940GZZLUWKA",
    "940GZZLUWLO",
    "940GZZLUWYC"
  ],
  "central": [
    "940GZZLUBKE",
    "940GZZLUBKH",
    "940GZZLUBLG",
    "940GZZLUBND",
    "940GZZLUBNK",
    "940GZZLUCHL",
    "940GZZLUCWL",
    "940GZZLUDBN",
    "940GZZLUEAN",
    "940GZZLUEBY",
    "940GZZLUEPG",
    "940GZZLUFLP",
    "940GZZLUGFD",
    "940GZZLUGGH",
    "940GZZLUGTH",
    "940GZZLUHBN",
    "940GZZLUHGR",
    "940GZZLUHLT",
    "940GZZLUHPK",
    "940GZZLULGN",
    "940GZZLULGT",
    "940GZZLULVT",
    "940GZZLULYN",
    "940GZZLULYS",
    "940GZZLUMBA",
    "940GZZLUMED",
    "940GZZLUNAN",
    "940GZZLUNBP",
    "940GZZLUNHG",
    "940GZZLUNHT",
    "940GZZLUOXC",
    "940GZZLUPVL",
    "940GZZLUQWY",
    "940GZZLURBG",
    "940GZZLURSG",
    "940GZZLURVY",
    "940GZZLUSBC",
    "940GZZLUSNB",
    "940GZZLUSPU",
    "940GZZLUSRP",
    "940GZZLUSTD",
    "940GZZLUSWF",
    "940GZZLUTCR",
    "940GZZLUTHB",
    "940GZZLUWCY",
    "940GZZLUWOF",
    "940GZZLUWRP",
    "940GZZLUWSD",
    "940GZZLUWTA"
  ],
  "circle": [
    "940GZZLUALD",
    "940GZZLUBBN",
    "940GZZLUBKF",
    "940GZZLUBST",
    "940GZZLUBWT",
    "940GZZLUCST",
    "940GZZLUEMB",
    "940GZZLUERC",
    "940GZZLUESQ",
    "940GZZLUFCN",
    "940GZZLUGHK",
    "940GZZLUGPS",
    "940GZZLUGTR",
    "940GZZLUHSC",
    "940GZZLUHSK",
    "940GZZLUKSX",
    "940GZZLULAD",
    "940GZZLULRD",
    "940GZZLULVT",
    "940GZZLUMGT",
    "940GZZLUMMT",
    "940GZZLUMSH",
    "940GZZLUNHG",
    "940GZZLUPAC",
    "940GZZLUPAH",
    "940GZZLURYO",
    "940GZZLUSBM",
    "940GZZLUSJP",
    "940GZZLUSKS",
    "940GZZLUSSQ",
    "940GZZLUTMP",
    "940GZZLUTWH",
    "940GZZLUVIC",
    "940GZZLUWLA",
    "940GZZLUWSM",
    "940GZZLUWSP"
  ],
  "district": [
    "940GZZLUACT",
    "940GZZLUADE",
    "940GZZLUBBB",
    "940GZZLUBEC",
    "940GZZLUBKF",
    "940GZZLUBKG",
    "940GZZLUBSC",
    "940GZZLUBWR",
    "940GZZLUBWT",
    "940GZZLUCST",
    "940GZZLUCWP",
    "940GZZLUDGE",
    "940GZZLUDGY",
    "940GZZLUEBY",
    "940GZZLUECM",
    "940GZZLUECT",
    "940GZZLUEHM",
    "940GZZLUEMB",
    "940GZZLUEPK",
    "940GZZLUEPY",
    "940GZZLUERC",
    "940GZZLUFBY",
    "940GZZLUGBY",
    "940GZZLUGHK",
    "940GZZLUGTR",
    "940GZZLUHCH",
    "940GZZLUHSC",
    "940GZZLUHSD",
    "940GZZLUHSK",
    "940GZZLUKOY",
    "940GZZLUKWG",
    "940GZZLULAD",
    "940GZZLULRD",
    "940GZZLUMED",
    "940GZZLUMMT",
    "940GZZLUMSH",
    "940GZZLUNHG",
    "940GZZLUPAC",
    "940GZZLUPAH",
    "940GZZLUPLW",
    "940GZZLUPSG",
    "940GZZLUPYB",
    "940GZZLURMD",
    "940GZZLURVP",
    "940GZZLURYO",
    "940GZZLUSBM",
    "940GZZLUSFB",
    "940GZZLUSFS",
    "940GZZLUSGN",
    "940GZZLUSJP",
    "940GZZLUSKS",
    "940GZZLUSSQ",
    "940GZZLUTMP",
    "940GZZLUTNG",
    "940GZZLUTWH",
    "940GZZLUUPB",
    "940GZZLUUPK",
    "940GZZLUUPM",
    "940GZZLUUPY",
    "940GZZLUVIC",
    "940GZZLUWBN",
    "940GZZLUWHM",
    "940GZZLUWIM",
    "940GZZLUWIP",
    "940GZZLUWKN",
    "940GZZLUWLA",
    "940GZZLUWPL",
    "940GZZLUWSM",
    "940GZZLUWSP"
  ],
  "hammersmith-city": [
    "940GZZLUADE",
    "940GZZLUBBB",
    "940GZZLUBBN",
    "940GZZLUBKG",
    "940GZZLUBST",
    "940GZZLUBWR",
    "940GZZLUEHM",
    "940GZZLUERC",
    "940GZZLUESQ",
    "940GZZLUFCN",
    "940GZZLUGHK",
    "940GZZLUGPS",
    "940GZZLUHSC",
    "940GZZLUKSX",
    "940GZZLULAD",
    "940GZZLULRD",
    "940GZZLULVT",
    "940GZZLUMED",
    "940GZZLUMGT",
    "940GZZLUPAH",
    "940GZZLUPLW",
    "940GZZLURYO",
    "940GZZLUSBM",
    "940GZZLUSGN",
    "940GZZLUUPK",
    "940GZZLUWHM",
    "940GZZLUWLA",
    "940GZZLUWPL",
    "940GZZLUWSP"
  ],
  "jubilee": [
    "940GZZLUBMY",
    "940GZZLUBND",
    "940GZZLUBST",
    "940GZZLUCGT",
    "940GZZLUCPK",
    "940GZZLUCWR",
    "940GZZLUCYF",
    "940GZZLUDOH",
    "940GZZLUFYR",
    "940GZZLUGPK",
    "940GZZLUKBN",
    "940GZZLUKBY",
    "940GZZLULNB",
    "940GZZLUNDN",
    "940GZZLUNGW",
    "940GZZLUQBY",
    "940GZZLUSJW",
    "940GZZLUSTD",
    "940GZZLUSTM",
    "940GZZLUSWC",
    "940GZZLUSWK",
    "940GZZLUWHM",
    "940GZZLUWHP",
    "940GZZLUWIG",
    "940GZZLUWLO",
    "940GZZLUWSM",
    "940GZZLUWYP"
  ],
  "metropolitan": [
    "940GZZLUALD",
    "940GZZLUAMS",
    "940GZZLUBBN",
    "940GZZLUBST",
    "940GZZLUCAL",
    "940GZZLUCSM",
    "940GZZLUCXY",
    "940GZZLUCYD",
    "940GZZLUEAE",
    "940GZZLUESQ",
    "940GZZLUFCN",
    "940GZZLUFYR",
    "940GZZLUGPS",
    "940GZZLUHGD",
    "940GZZLUHOH",
    "940GZZLUICK",
    "940GZZLUKSX",
    "940GZZLULVT",
    "940GZZLUMGT",
    "940GZZLUMPK",
    "940GZZLUNHA",
    "940GZZLUNKP",
    "940GZZLUNOW",
    "940GZZLUNWH",
    "940GZZLUPNR",
    "940GZZLUPRD",
    "940GZZLURKW",
    "940GZZLURSM",
    "940GZZLURSP",
    "940GZZLURYL",
    "940GZZLUUXB",
    "940GZZLUWAF",
    "940GZZLUWHW",
    "940GZZLUWYP"
  ],
  "northern": [
    "940GZZLUACY",
    "940GZZLUAGL",
    "940GZZLUBLM",
    "940GZZLUBNK",
    "940GZZLUBOR",
    "940GZZLUBTK",
    "940GZZLUBTX",
    "940GZZLUBZP",
    "940GZZLUCFM",
    "940GZZLUCHX",
    "940GZZLUCND",
    "940GZZLUCPC",
    "940GZZLUCPN",
    "940GZZLUCPS",
    "940GZZLUCSD",
    "940GZZLUCTN",
    "940GZZLUEAC",
    "940GZZLUEFY",
    "940GZZLUEGW",
    "940GZZLUEMB",
    "940GZZLUEUS",
    "940GZZLUFYC",
    "940GZZLUGDG",
    "940GZZLUGGN",
    "940GZZLUHBT",
    "940GZZLUHCL",
    "940GZZLUHGT",
    "940GZZLUHTD",
    "940GZZLUKNG",
    "940GZZLUKSH",
    "940GZZLUKSX",
    "940GZZLULNB",
    "940GZZLULSQ",
    "940GZZLUMDN",
    "940GZZLUMGT",
    "940GZZLUMHL",
    "940GZZLUMTC",
    "940GZZLUODS",
    "940GZZLUOVL",
    "940GZZLUSKW",
    "940GZZLUSWN",
    "940GZZLUTAW",
    "940GZZLUTBC",
    "940GZZLUTBY",
    "940GZZLUTCR",
    "940GZZLUTFP",
    "940GZZLUWFN",
    "940GZZLUWLO",
    "940GZZLUWOP",
    "940GZZLUWRR"
  ],
  "piccadilly": [
    "910GENFCOAK",
    "940GZZLUACT",
    "940GZZLUALP",
    "940GZZLUASG",
    "940GZZLUASL",
    "940GZZLUBDS",
    "940GZZLUBOS",
    "940GZZLUBSC",
    "940GZZLUCAR",
    "940GZZLUCGN",
    "940GZZLUCKS",
    "940GZZLUEAE",
    "940GZZLUECM",
    "940GZZLUECT",
    "940GZZLUFPK",
    "940GZZLUGPK",
    "940GZZLUGTR",
    "940GZZLUHBN",
    "940GZZLUHGD",
    "940GZZLUHNX",
    "940GZZLUHPC",
    "940GZZLUHR4",
    "940GZZLUHR5",
    "940GZZLUHRC",
    "940GZZLUHSD",
    "940GZZLUHWC",
    "940GZZLUHWE",
    "940GZZLUHWT",
    "940GZZLUHWY",
    "940GZZLUICK",
    "940GZZLUKNB",
    "940GZZLUKSX",
    "940GZZLULSQ",
    "940GZZLUMRH",
    "940GZZLUNEN",
    "940GZZLUNFD",
    "940GZZLUOAK",
    "940GZZLUOSY",
    "940GZZLUPCC",
    "940GZZLUPKR",
    "940GZZLURSM",
    "940GZZLURSP",
    "940GZZLURSQ",
    "940GZZLURVP",
    "940GZZLURYL",
    "940GZZLUSEA",
    "940GZZLUSFB",
    "940GZZLUSGT",
    "940GZZLUSHH",
    "940GZZLUSKS",
    "940GZZLUSUH",
    "940GZZLUSUT",
    "940GZZLUTNG",
    "940GZZLUTPN",
    "940GZZLUUXB",
    "940GZZLUWOG"
  ],
  "victoria": [
    "940GZZLUBLR",
    "940GZZLUBXN",
    "940GZZLUEUS",
    "940GZZLUFPK",
    "940GZZLUGPK",
    "940GZZLUHAI",
    "940GZZLUKSX",
    "940GZZLUOXC",
    "940GZZLUPCO",
    "940GZZLUSKW",
    "940GZZLUSVS",
    "940GZZLUTMH",
    "940GZZLUVIC",
    "940GZZLUVXL",
    "940GZZLUWRR",
    "940GZZLUWWL"
  ],
  "waterloo-city": [
    "940GZZLUBNK",
    "940GZZLUWLO"
  ]
}

_exports.sharedPlatforms = {
   "940GZZLUEMB": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUADE": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUBBB": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUBBN": [
      [
         "circle",
         "hammersmith-city",
         "metropolitan"
      ]
   ],
   "940GZZLUBWR": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUEHM": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUERC": [
      [
         "circle",
         "hammersmith-city"
      ],
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUESQ": [
      [
         "circle",
         "hammersmith-city",
         "metropolitan"
      ]
   ],
   "940GZZLUGHK": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUGPS": [
      [
         "circle",
         "hammersmith-city",
         "metropolitan"
      ]
   ],
   "940GZZLULAD": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLULRD": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUPLW": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUMED": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLURYO": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUSBM": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUWLA": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUSGN": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUUPK": [
      [
         "district",
         "hammersmith-city"
      ]
   ],
   "940GZZLUWSP": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUEAE": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLUHGD": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLUICK": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLURSM": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLURYL": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLURSP": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLUBST": [
      [
         "circle",
         "hammersmith-city"
      ]
   ],
   "940GZZLUUXB": [
      [
         "metropolitan",
         "piccadilly"
      ]
   ],
   "940GZZLUBWT": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUGTR": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUHSK": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUMMT": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUSJP": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUMSH": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUNHG": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUSKS": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUTMP": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUSSQ": [
      [
         "circle",
         "district"
      ]
   ],
   "940GZZLUECM": [
      [
         "district",
         "piccadilly"
      ]
   ],
   "940GZZLUTNG": [
      [
         "district",
         "piccadilly"
      ]
   ]
}

_exports.routes = {
  "bakerloo":{
    "stations":"""Elephant & Castle
Lambeth North
Waterloo
Embankment
Charing Cross
Piccadilly Circus
Oxford Circus
Regent's Park
Baker Street
Marylebone
Edgware Road (Bakerloo)
Paddington
Warwick Avenue
Maida Vale
Kilburn Park
Queen's Park
Kensal Green
Willesden Junction
Harlesden
Stonebridge Park
Wembley Central
North Wembley
South Kenton
Kenton
Harrow & Wealdstone"""
  },
  # ...
  "piccadilly_1":{
    "stations":"Cockfosters;Oakwood;Southgate;Arnos Grove;Bounds Green;Wood Green;Turnpike Lane;Manor House;Finsbury Park;Arsenal;Holloway Road;Caledonian Road;King's Cross St. Pancras;Russell Square;Holborn;Covent Garden;Leicester Square;Piccadilly Circus;Green Park;Hyde Park Corner;Knightsbridge;South Kensington;Gloucester Road;Earl's Court;Barons Court;Hammersmith (Dist&Picc Line);Turnham Green;Acton Town;Ealing Common;North Ealing;Park Royal;Alperton;Sudbury Town;Sudbury Hill;South Harrow;Rayners Lane;Eastcote;Ruislip Manor;Ruislip;Ickenham;Hillingdon;Uxbridge"
  },
  "piccadilly_2":{
    "stations":"Cockfosters;Oakwood;Southgate;Arnos Grove;Bounds Green;Wood Green;Turnpike Lane;Manor House;Finsbury Park;Arsenal;Holloway Road;Caledonian Road;King's Cross St. Pancras;Russell Square;Holborn;Covent Garden;Leicester Square;Piccadilly Circus;Green Park;Hyde Park Corner;Knightsbridge;South Kensington;Gloucester Road;Earl's Court;Barons Court;Hammersmith (Dist&Picc Line);Turnham Green;Acton Town;South Ealing;Northfields;Boston Manor;Osterley;Hounslow East;Hounslow Central;Hounslow West;Hatton Cross;Heathrow Terminals 1-2-3;Heathrow Terminal 4"
  },
  # ...
  "metropolitan_1":{
    "stations":"Aldgate;Liverpool Street;Moorgate;Barbican;Farringdon;King's Cross St. Pancras;Euston Square;Great Portland Street;Baker Street;Finchley Road;Wembley Park;Preston Road;Northwick Park;Harrow-on-the-Hill;North Harrow;Pinner;Northwood Hills;Northwood;Moor Park;Croxley;Watford"
  },
  "metropolitan_2":{
    "stations":"Aldgate;Liverpool Street;Moorgate;Barbican;Farringdon;King's Cross St. Pancras;Euston Square;Great Portland Street;Baker Street;Finchley Road;Wembley Park;Preston Road;Northwick Park;Harrow-on-the-Hill;North Harrow;Pinner;Northwood Hills;Northwood;Moor Park;Rickmansworth;Chorleywood;Chalfont & Latimer;Amersham"
  },
  "metropolitan_3":{
    "stations":"Aldgate;Liverpool Street;Moorgate;Barbican;Farringdon;King's Cross St. Pancras;Euston Square;Great Portland Street;Baker Street;Finchley Road;Wembley Park;Preston Road;Northwick Park;Harrow-on-the-Hill;North Harrow;Pinner;Northwood Hills;Northwood;Moor Park;Rickmansworth;Chorleywood;Chalfont & Latimer;Chesham"
  },
  "metropolitan_4":{
    "stations":"Aldgate;Liverpool Street;Moorgate;Barbican;Farringdon;King's Cross St. Pancras;Euston Square;Great Portland Street;Baker Street;Finchley Road;Wembley Park;Preston Road;Northwick Park;Harrow-on-the-Hill;West Harrow;Rayners Lane;Eastcote;Ruislip Manor;Ruislip;Ickenham;Hillingdon;Uxbridge"
  },
  # ...
  "hammersmith":{
    "stations":"Barking;East Ham;Upton Park;West Ham;Bromley-by-Bow;Bow Road;Mile End;Stepney Green;Whitechapel;Aldgate East;Liverpool Street;Moorgate;Barbican;Farringdon;King's Cross St. Pancras;Euston Square;Great Portland Street;Baker Street;Edgware Road (Circle Line);Paddington;Royal Oak;Westbourne Park;Ladbroke Grove;Latimer Road;Wood Lane;Shepherd's Bush Market;Goldhawk Road;Hammersmith (H&C Line)"
  },
  # ...
  "circle":{
    "stations":"Aldgate;Tower Hill;Monument;Cannon Street;Mansion House;Blackfriars;Temple;Embankment;Westminster;St. James's Park;Victoria;Sloane Square;South Kensington;Gloucester Road;High Street Kensington;Notting Hill Gate;Bayswater;Paddington;Edgware Road (Circle Line);Baker Street;Great Portland Street;Euston Square;King's Cross St. Pancras;Farringdon;Barbican;Moorgate;Liverpool Street"
  },
  # ...
  "district_1":{
    "stations":"""Upminster
Upminster Bridge
Hornchurch
Elm Park
Dagenham East
Dagenham Heathway
Becontree
Upney
Barking
East Ham
Upton Park
Plaistow
West Ham
Bromley-by-Bow
Bow Road
Mile End
Stepney Green
Whitechapel
Aldgate East
Tower Hill
Monument
Cannon Street
Mansion House
Blackfriars
Temple
Embankment
Westminster
St. James's Park
Victoria
Sloane Square
South Kensington
Gloucester Road
Earl's Court
West Kensington
Barons Court
Hammersmith (Dist&Picc Line)
Ravenscourt Park
Stamford Brook
Turnham Green
Gunnersbury
Kew Gardens
Richmond"""
  },
  "district_2":{
    "stations":"""Upminster
Upminster Bridge
Hornchurch
Elm Park
Dagenham East
Dagenham Heathway
Becontree
Upney
Barking
East Ham
Upton Park
Plaistow
West Ham
Bromley-by-Bow
Bow Road
Mile End
Stepney Green
Whitechapel
Aldgate East
Tower Hill
Monument
Cannon Street
Mansion House
Blackfriars
Temple
Embankment
Westminster
St. James's Park
Victoria
Sloane Square
South Kensington
Gloucester Road
Earl's Court
West Kensington
Barons Court
Hammersmith (Dist&Picc Line)
Ravenscourt Park
Stamford Brook
Turnham Green
Chiswick Park
Acton Town
Ealing Common
Ealing Broadway"""
  },
  "district_3":{
    "stations":"""Upminster
Upminster Bridge
Hornchurch
Elm Park
Dagenham East
Dagenham Heathway
Becontree
Upney
Barking
East Ham
Upton Park
Plaistow
West Ham
Bromley-by-Bow
Bow Road
Mile End
Stepney Green
Whitechapel
Aldgate East
Tower Hill
Monument
Cannon Street
Mansion House
Blackfriars
Temple
Embankment
Westminster
St. James's Park
Victoria
Sloane Square
South Kensington
Gloucester Road
Earl's Court
West Brompton
Fulham Broadway
Parsons Green
Putney Bridge
East Putney
Southfields
Wimbledon Park
Wimbledon"""
  },
  "district_4":{
    "stations":"""Edgware Road (Circle Line)
Paddington
Bayswater
Notting Hill Gate
High Street Kensington
Earl's Court
Kensington (Olympia)"""
  },
  # ...
  "northern_charing_cross":{
    "stations":"""Morden
South Wimbledon
Colliers Wood
Tooting Broadway
Tooting Bec
Balham
Clapham South
Clapham Common
Clapham North
Stockwell
Oval
Kennington
Waterloo
Embankment
Charing Cross
Leicester Square
Tottenham Court Road
Goodge Street
Warren Street
Euston
Mornington Crescent
Camden Town
Chalk Farm
Belsize Park
Hampstead
Golders Green
Brent Cross
Hendon Central
Colindale
Burnt Oak
Edgware"""
  },
  "northern_mill_hill":{
    "stations":"Mill Hill East;Finchley Central"
  },
  "northern_bank":{
    "stations":"""Morden
South Wimbledon
Colliers Wood
Tooting Broadway
Tooting Bec
Balham
Clapham South
Clapham Common
Clapham North
Stockwell
Oval
Kennington
Elephant & Castle
Borough
London Bridge
Bank
Moorgate
Old Street
Angel
King's Cross St. Pancras
Euston
Camden Town
Kentish Town
Tufnell Park
Archway
Highgate
East Finchley
Finchley Central
West Finchley
Woodside Park
Totteridge & Whetstone
High Barnet"""
  },
  # ...
  "jubilee":{
    "stations":"""Stanmore
Canons Park
Queensbury
Kingsbury
Wembley Park
Neasden
Dollis Hill
Willesden Green
Kilburn
West Hampstead
Finchley Road
Swiss Cottage
St. John's Wood
Baker Street
Bond Street
Green Park
Westminster
Waterloo
Southwark
London Bridge
Bermondsey
Canada Water
Canary Wharf
North Greenwich
Canning Town
West Ham
Stratford"""
  },
  # ...
  "victoria":{
    "stations":"""Walthamstow Central
Blackhorse Road
Tottenham Hale
Seven Sisters
Finsbury Park
Highbury & Islington
King's Cross St. Pancras
Euston
Warren Street
Oxford Circus
Green Park
Victoria
Pimlico
Vauxhall
Stockwell
Brixton"""
  }
}
