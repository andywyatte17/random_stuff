# data_routes.py

def Zeroized(timings):
  '''
    Turn a series of hh:mm timings into minutes with the first value at 0, ie:
    ["0527","0530","0610"...] -> [0,3,40,...].
  '''
  first = -1
  results = []
  for x in timings:
    hh, mm = int(x[0:2]), int(x[2:4])
    mm = hh*60 + mm
    if first<0:
      results.append(0)
      first = mm
    else:
      results.append( mm - first )
  return tuple( results )

routes = {
  "bakerloo":{
     "stations":('Elephant & Castle', 'Lambeth North', 'Waterloo', 'Embankment', 'Charing Cross', 'Piccadilly Circus', 'Oxford Circus', "Regent's Park", 'Baker Street', 'Marylebone', 'Edgware Road (Bakerloo)', 'Paddington', 'Warwick Avenue', 'Maida Vale', 'Kilburn Park', "Queen's Park", 'Kensal Green', 'Willesden Junction', 'Harlesden', 'Stonebridge Park', 'Wembley Central', 'North Wembley', 'South Kenton', 'Kenton', 'Harrow & Wealdstone'),
     "timings":Zeroized( ('0537','0539','0541','0542','0543','0545','0547','0549','0551','0552','0553','0555','0557','0559','0601','0605','0608','0611','0613','0615','0618','0620','0622','0624','0627') )
  },
  # ...
  "central_white_city_ealing_broadway":{
    "stations":('White City', 'East Acton', 'North Acton', 'West Acton', 'Ealing Broadway'),
    "timings":Zeroized( ('0557','0559','0601','0604','0608') )
  },
  # ...
  "central_west_ruislip":{
    "stations":('Epping', 'Theydon Bois', 'Debden', 'Loughton', 'Buckhurst Hill', 'Woodford', 'South Woodford', 'Snaresbrook', 'Leytonstone', 'Leyton', 'Stratford', 'Mile End', 'Bethnal Green', 'Liverpool Street', 'Bank', "St. Paul's", 'Chancery Lane', 'Holborn', 'Tottenham Court Road', 'Oxford Circus', 'Bond Street', 'Marble Arch', 'Lancaster Gate', 'Queensway', 'Notting Hill Gate', 'Holland Park', "Shepherd's Bush (Central)", 'White City', 'East Acton', 'North Acton', 'Hanger Lane', 'Perivale', 'Greenford', 'Northolt', 'South Ruislip', 'Ruislip Gardens', 'West Ruislip'),
    "timings":Zeroized( ('0510','0513','0516','0519','0522','0524','0527','0529','0532','0534','0537','0540','0543','0546','0548','0550','0552','0553','0555','0556','0558','0559','0601','0603','0605','0606','0608','0612','0614','0616','0620','0622','0624','0627','0629','0631','0634') )
  },
  # ...
  "central_hainault":{
    "stations":('Hainault', 'Fairlop', 'Barkingside', 'Newbury Park', 'Gants Hill', 'Redbridge', 'Wanstead', 'Leytonstone'),
    "timings":Zeroized( ('0514','0516','0518','0520','0523','0525','0527','0530') )
  },
  "central_roding_valley":{
    "stations":('Hainault', 'Grange Hill', 'Chigwell', 'Roding Valley', 'Woodford'),
    "timings":Zeroized( ( '0604', '0606', '0608', '0611', '0614' ) )
  },
  # ...
  "circle_hammersmith_north_circle":{
    "stations":( 'Hammersmith (H&C Line)', 'Goldhawk Road', "Shepherd's Bush Market", "Wood Lane", 'Latimer Road', 'Ladbroke Grove', 'Westbourne Park', 'Royal Oak', 'Paddington (H&C Line)-Underground', 'Edgware Road (Circle Line)', 'Baker Street', 'Great Portland Street', 'Euston Square', "King's Cross St. Pancras", 'Farringdon', 'Barbican', 'Moorgate', 'Liverpool Street', 'Aldgate'),
    "timings":Zeroized( ('0438','0439','0441','0442','0444','0445','0447','0448','0450','0453','0456','0458','0500','0502','0505','0507','0509','0510','0513') )
  },
  # ...
  "circle_liverpool_street_south_circle":{
    "stations":( 'Liverpool Street', 'Aldgate', 'Tower Hill', 'Monument', 'Cannon Street', 'Mansion House', 'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St. James's Park", 'Victoria', 'Sloane Square', 'South Kensington', 'Gloucester Road', 'High Street Kensington', 'Notting Hill Gate', 'Bayswater', 'Paddington', 'Edgware Road (Circle Line)'),
    "timings":Zeroized( ('0524', '0527','0529','0531','0532','0533','0535','0537','0539','0540','0542','0544','0546','0548','0552','0554','0556','0558','0600','0603') )
  },
  # ...
  "district_upminster_richmond":{
    "stations":('Upminster', 'Upminster Bridge', 'Hornchurch', 'Elm Park', 'Dagenham East', 'Dagenham Heathway', 'Becontree', 'Upney', 'Barking', 'East Ham', 'Upton Park', 'Plaistow', 'West Ham', 'Bromley-by-Bow', 'Bow Road', 'Mile End', 'Stepney Green', 'Whitechapel', 'Aldgate East', 'Tower Hill', 'Monument', 'Cannon Street', 'Mansion House', 'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St. James's Park", 'Victoria', 'Sloane Square', 'South Kensington', 'Gloucester Road', "Earl's Court", 'West Kensington', 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Ravenscourt Park', 'Stamford Brook', 'Turnham Green', 'Gunnersbury', 'Kew Gardens', 'Richmond'),
    "timings":Zeroized( ('0453', '0455', '0457', '0459', '0502', '0504', '0507', '0509', '0512', '0516', '0518', '0520', '0522', '0524', '0526', '0528', '0530', '0533', '0535', '0537', '0539', '0540', '0541', '0543', '0545', '0547', '0548', '0550', '0552', '0554', '0556', '0558', '0602', '0604', '0606', '0608', '0610', '0611', '0613', '0616', '0618', '0622') )
  },
  # ...
  "district_earls_court_ealing_broadway":{
    "stations":("Earl's Court", 'West Kensington', 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Ravenscourt Park', 'Stamford Brook', 'Turnham Green', 'Chiswick Park', 'Acton Town', 'Ealing Common', 'Ealing Broadway'),
    "timings":Zeroized(('0609', '0611', '0613', '0615', '0617', '0618', '0620', '0622', '0625', '0627', '0633'))
  },
  # ...
  "district_earls_court_wimbledon":{
    "stations":('High Street Kensington', "Earl's Court", 'West Brompton', 'Fulham Broadway', 'Parsons Green', 'Putney Bridge', 'East Putney', 'Southfields', 'Wimbledon Park', 'Wimbledon'),
    "timings":Zeroized( ('0603', '0607', '0608', '0610', '0612', '0615', '0617', '0619', '0621', '0625' ) )
  },
  # ...
  "district_high_st_kensington_olympia":{
    "stations":('High Street Kensington', "Earl's Court", 'Kensington (Olympia)'),
    "timings": Zeroized(('0656', '0700', '0703'))
  },
  # ...
  "hammersmith":{
    "stations":('Barking', 'East Ham', 'Upton Park', 'Plaistow', 'West Ham', 'Bromley-by-Bow', 'Bow Road', 'Mile End', 'Stepney Green', 'Whitechapel', 'Aldgate East', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Edgware Road (Circle Line)', 'Paddington (H&C Line)-Underground', 'Royal Oak', 'Westbourne Park', 'Ladbroke Grove', 'Latimer Road', 'Wood Lane', "Shepherd's Bush Market", 'Goldhawk Road', 'Hammersmith (H&C Line)'),
    "timings": Zeroized(('0501', '0504', '0506', '0509', '0510', '0512', '0515', '0516', '0518', '0521', '0523', '0526', '0528', '0529', '0531', '0534', '0536', '0538', '0540', '0543', '0545', '0546', '0548', '0550', '0551', '0553', '0554', '0556', '0559'))
  },
  # ...
  "jubilee":{
    "stations":('Stanmore', 'Canons Park', 'Queensbury', 'Kingsbury', 'Wembley Park', 'Neasden', 'Dollis Hill', 'Willesden Green', 'Kilburn', 'West Hampstead', 'Finchley Road', 'Swiss Cottage', "St. John's Wood", 'Baker Street', 'Bond Street', 'Green Park', 'Westminster', 'Waterloo', 'Southwark', 'London Bridge', 'Bermondsey', 'Canada Water', 'Canary Wharf', 'North Greenwich', 'Canning Town', 'West Ham', 'Stratford'),
    "timings": Zeroized(('0709', '0712', '0714', '0716', '0718', '0721', '0723', '0725', '0727', '0728', '0730', '0732', '0734', '0736', '0739', '0740', '0742', '0743', '0745', '0747', '0749', '0752', '0755', '0759', '0801', '0803', '0806'))
  },
  # ...
  "metropolitan_watford":{
    "stations":('Moor Park', 'Croxley', 'Watford'),
    "timings": Zeroized(('0730', '0734', '0738'))
  },
  # ...
  "metropolitan_amersham":{
    "stations":('Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park', 'Harrow-on-the-Hill', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Amersham'),
    "timings": Zeroized(('1925', '1931', '1938', '1940', '1942', '1943', '1946', '1948', '1950', '1953', '1956', '2001', '2004', '2008', '2013'))
  },
  # ...
  "metropolitan_chesham":{
    "stations":('Harrow-on-the-Hill', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Chesham'),
    "timings": Zeroized(('2310', '2313', '2315', '2317', '2320', '2323', '2328', '2331', '2336', '2345'))
  },
  # ...
  "metropolitan_uxbridge":{
    "stations":('Harrow-on-the-Hill', 'West Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge'),
    "timings": Zeroized(('0543', '0545', '0547', '0549', '0551', '0553', '0555', '0557', '0601'))
  },
  # ...
  "northern_bank":{
    "stations":('Morden', 'South Wimbledon', 'Colliers Wood', 'Tooting Broadway', 'Tooting Bec', 'Balham', 'Clapham South', 'Clapham Common', 'Clapham North', 'Stockwell', 'Oval', 'Kennington', 'Elephant & Castle', 'Borough', 'London Bridge', 'Bank', 'Moorgate', 'Old Street', 'Angel', "King's Cross St. Pancras", 'Euston', 'Camden Town', 'Kentish Town', 'Tufnell Park', 'Archway', 'Highgate', 'East Finchley', 'Finchley Central', 'West Finchley', 'Woodside Park', 'Totteridge & Whetstone', 'High Barnet'),
    "timings": Zeroized(('0005', '0007', '0009', '0011', '0013', '0015', '0017', '0019', '0020', '0022', '0024', '0027', '0029', '0031', '0032', '0034', '0036', '0037', '0040', '0043', '0044', '0051', '0053', '0054', '0056', '0059', '0101', '0105', '0107', '0109', '0111', '0115'))
  },
  # ...
  "northern_charing_cross":{
    "stations":('Kennington', 'Waterloo', 'Embankment', 'Charing Cross', 'Leicester Square', 'Tottenham Court Road', 'Goodge Street', 'Warren Street', 'Euston', 'Mornington Crescent', 'Camden Town', 'Chalk Farm', 'Belsize Park', 'Hampstead', 'Golders Green', 'Brent Cross', 'Hendon Central', 'Colindale', 'Burnt Oak', 'Edgware'),
    "timings": Zeroized(('0033', '0035', '0037', '0038', '0039', '0041', '0042', '0043', '0045', '0047', '0051', '0052', '0054', '0056', '0101', '0103', '0105', '0108', '0110', '0113'))
  },
  # ...
  "northern_mill_hill":{
    "stations":('Mill Hill East', 'Finchley Central'),
    "timings": Zeroized(('0106', '0109'))
  },
  # ...
  'piccadilly_uxbridge': {
    "stations": ('Uxbridge', 'Hillingdon', 'Ickenham', 'Ruislip', 'Ruislip Manor', 'Eastcote', 'Rayners Lane', 'South Harrow', 'Sudbury Hill', 'Sudbury Town', 'Alperton', 'Park Royal', 'North Ealing', 'Ealing Common', 'Acton Town', 'Hammersmith (Dist&Picc Line)', 'Barons Court', "Earl's Court", 'Gloucester Road', 'Knightsbridge', 'Hyde Park Corner', 'Green Park', 'Piccadilly Circus', 'Leicester Square', 'Covent Garden', 'Holborn', 'Russell Square', "King's Cross St. Pancras", 'Caledonian Road', 'Holloway Road', 'Arsenal', 'Finsbury Park', 'Manor House', 'Turnpike Lane', 'Wood Green', 'Bounds Green', 'Arnos Grove', 'Southgate', 'Oakwood', 'Cockfosters'),
    'timings': Zeroized(('0625', '0627', '0630', '0631', '0633', '0637', '0641', '0643', '0646', '0649', '0652', '0655', '0657', '0700', '0706', '0708', '0711', '0713', '0718', '0719', '0722', '0723', '0725', '0726', '0728', '0730', '0732', '0735', '0737', '0738', '0740', '0742', '0745', '0747', '0750', '0754', '0757', '0800', '0804'))
  },
  # ...
  "piccadilly_heathrow_5":{
    "stations":('Cockfosters', 'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane', 'Manor House', 'Finsbury Park', 'Arsenal', 'Holloway Road', 'Caledonian Road', "King's Cross St. Pancras", 'Russell Square', 'Holborn', 'Covent Garden', 'Leicester Square', 'Piccadilly Circus', 'Green Park', 'Hyde Park Corner', 'Knightsbridge', 'South Kensington', 'Gloucester Road', "Earl's Court", 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Turnham Green', 'Acton Town', 'South Ealing', 'Northfields', 'Boston Manor', 'Osterley', 'Hounslow East', 'Hounslow Central', 'Hounslow West', 'Hatton Cross', 'Heathrow Terminals 1-2-3', 'Heathrow Terminal 5'),
    "timings": Zeroized(('2202', '2204', '2207', '2212', '2214', '2216', '2218', '2221', '2224', '2225', '2227', '2228', '2232', '2234', '2235', '2237', '2238', '2240', '2241', '2243', '2245', '2247', '2249', '2251', '2254', '2256', '2300', '2305', '2308', '2311', '2313', '2316', '2318', '2319', '2322', '2328', '2332', '2336'))
  },
  "piccadilly_heathrow_4":{
    "stations":('Hatton Cross', 'Heathrow Terminal 4'),
    "timings": Zeroized(('0749', '0752'))
  },
  # ...
  "victoria":{
    "stations":('Walthamstow Central', 'Blackhorse Road', 'Tottenham Hale', 'Seven Sisters', 'Finsbury Park', 'Highbury & Islington', "King's Cross St. Pancras", 'Euston', 'Warren Street', 'Oxford Circus', 'Green Park', 'Victoria', 'Pimlico', 'Vauxhall', 'Stockwell', 'Brixton'),
    "timings": Zeroized(('0525', '0527', '0529', '0531', '0535', '0537', '0540', '0541', '0543', '0545', '0546', '0549', '0550', '0552', '0554', '0557'))
  },
  # ...
}

if __name__=='__main__':
  import sys, os
  if len(sys.argv)==2 and sys.argv[1]=='-test':
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
    from data.data_js import stations

    def HasStation(test):
      for x in stations.keys():
        if stations[x]==test: return True
      return False

    for route in routes.keys():
      for station in routes[route]["stations"]:
        if not HasStation(station):
          print("Error : route {}, station {}".format(route, station))

    for route in routes.keys():
      if "stations" in routes[route] and "timings" in routes[route]:
        if len(routes[route]["stations"]) != len(routes[route]["timings"]):
          print("Stations / timings mismatch in {}".format(route))
