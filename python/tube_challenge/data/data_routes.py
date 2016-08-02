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
  "central_ealing_broadway":{
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
  "circle":{ "stations":('Aldgate', 'Tower Hill', 'Monument', 'Cannon Street', 'Mansion House', 'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St. James's Park", 'Victoria', 'Sloane Square', 'South Kensington', 'Gloucester Road', 'High Street Kensington', 'Notting Hill Gate', 'Bayswater', 'Paddington', 'Edgware Road (Circle Line)', 'Baker Street', 'Great Portland Street', 'Euston Square', "King's Cross St. Pancras", 'Farringdon', 'Barbican', 'Moorgate', 'Liverpool Street')  },
  # ...
  "district_upminster_richmond":{ "stations":('Upminster', 'Upminster Bridge', 'Hornchurch', 'Elm Park', 'Dagenham East', 'Dagenham Heathway', 'Becontree', 'Upney', 'Barking', 'East Ham', 'Upton Park', 'Plaistow', 'West Ham', 'Bromley-by-Bow', 'Bow Road', 'Mile End', 'Stepney Green', 'Whitechapel', 'Aldgate East', 'Tower Hill', 'Monument', 'Cannon Street', 'Mansion House', 'Blackfriars', 'Temple', 'Embankment', 'Westminster', "St. James's Park", 'Victoria', 'Sloane Square', 'South Kensington', 'Gloucester Road', "Earl's Court", 'West Kensington', 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Ravenscourt Park', 'Stamford Brook', 'Turnham Green', 'Gunnersbury', 'Kew Gardens', 'Richmond')  },
  # ...
  "district_earls_court_ealing_broadway":{ "stations":("Earl's Court", 'West Kensington', 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Ravenscourt Park', 'Stamford Brook', 'Turnham Green', 'Chiswick Park', 'Acton Town', 'Ealing Common', 'Ealing Broadway')  },
  # ...
  "district_earls_court_wimbledon":{ "stations":("Earl's Court", 'West Brompton', 'Fulham Broadway', 'Parsons Green', 'Putney Bridge', 'East Putney', 'Southfields', 'Wimbledon Park', 'Wimbledon')  },
  # ...
  "district_edgware_road_kensington_olympia":{ "stations":('Edgware Road (Circle Line)', 'Paddington', 'Bayswater', 'Notting Hill Gate', 'High Street Kensington', "Earl's Court", 'Kensington (Olympia)')  },
  # ...
  "hammersmith":{ "stations":('Barking', 'East Ham', 'Upton Park', 'West Ham', 'Bromley-by-Bow', 'Bow Road', 'Mile End', 'Stepney Green', 'Whitechapel', 'Aldgate East', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Edgware Road (Circle Line)', 'Paddington (H&C Line)-Underground', 'Royal Oak', 'Westbourne Park', 'Ladbroke Grove', 'Latimer Road', 'Wood Lane', "Shepherd's Bush Market", 'Goldhawk Road', 'Hammersmith (H&C Line)')  },
  # ...
  "jubilee":{ "stations":('Stanmore', 'Canons Park', 'Queensbury', 'Kingsbury', 'Wembley Park', 'Neasden', 'Dollis Hill', 'Willesden Green', 'Kilburn', 'West Hampstead', 'Finchley Road', 'Swiss Cottage', "St. John's Wood", 'Baker Street', 'Bond Street', 'Green Park', 'Westminster', 'Waterloo', 'Southwark', 'London Bridge', 'Bermondsey', 'Canada Water', 'Canary Wharf', 'North Greenwich', 'Canning Town', 'West Ham', 'Stratford')  },
  # ...
  "metropolitan_1":{ "stations":('Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park', 'Harrow-on-the-Hill', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Croxley', 'Watford')  },
  # ...
  "metropolitan_2":{ "stations":('Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park', 'Harrow-on-the-Hill', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Amersham')  },
  # ...
  "metropolitan_3":{ "stations":('Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park', 'Harrow-on-the-Hill', 'North Harrow', 'Pinner', 'Northwood Hills', 'Northwood', 'Moor Park', 'Rickmansworth', 'Chorleywood', 'Chalfont & Latimer', 'Chesham')  },
  # ...
  "metropolitan_4":{ "stations":('Aldgate', 'Liverpool Street', 'Moorgate', 'Barbican', 'Farringdon', "King's Cross St. Pancras", 'Euston Square', 'Great Portland Street', 'Baker Street', 'Finchley Road', 'Wembley Park', 'Preston Road', 'Northwick Park', 'Harrow-on-the-Hill', 'West Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge')  },
  # ...
  "northern_bank":{ "stations":('Morden', 'South Wimbledon', 'Colliers Wood', 'Tooting Broadway', 'Tooting Bec', 'Balham', 'Clapham South', 'Clapham Common', 'Clapham North', 'Stockwell', 'Oval', 'Kennington', 'Elephant & Castle', 'Borough', 'London Bridge', 'Bank', 'Moorgate', 'Old Street', 'Angel', "King's Cross St. Pancras", 'Euston', 'Camden Town', 'Kentish Town', 'Tufnell Park', 'Archway', 'Highgate', 'East Finchley', 'Finchley Central', 'West Finchley', 'Woodside Park', 'Totteridge & Whetstone', 'High Barnet')  },
  # ...
  "northern_charing_cross":{ "stations":('Morden', 'South Wimbledon', 'Colliers Wood', 'Tooting Broadway', 'Tooting Bec', 'Balham', 'Clapham South', 'Clapham Common', 'Clapham North', 'Stockwell', 'Oval', 'Kennington', 'Waterloo', 'Embankment', 'Charing Cross', 'Leicester Square', 'Tottenham Court Road', 'Goodge Street', 'Warren Street', 'Euston', 'Mornington Crescent', 'Camden Town', 'Chalk Farm', 'Belsize Park', 'Hampstead', 'Golders Green', 'Brent Cross', 'Hendon Central', 'Colindale', 'Burnt Oak', 'Edgware')  },
  # ...
  "northern_mill_hill":{ "stations":('Mill Hill East', 'Finchley Central')  },
  # ...
  "piccadilly_1":{ "stations":('Cockfosters', 'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane', 'Manor House', 'Finsbury Park', 'Arsenal', 'Holloway Road', 'Caledonian Road', "King's Cross St. Pancras", 'Russell Square', 'Holborn', 'Covent Garden', 'Leicester Square', 'Piccadilly Circus', 'Green Park', 'Hyde Park Corner', 'Knightsbridge', 'South Kensington', 'Gloucester Road', "Earl's Court", 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Turnham Green', 'Acton Town', 'Ealing Common', 'North Ealing', 'Park Royal', 'Alperton', 'Sudbury Town', 'Sudbury Hill', 'South Harrow', 'Rayners Lane', 'Eastcote', 'Ruislip Manor', 'Ruislip', 'Ickenham', 'Hillingdon', 'Uxbridge')  },
  # ...
  "piccadilly_2":{ "stations":('Cockfosters', 'Oakwood', 'Southgate', 'Arnos Grove', 'Bounds Green', 'Wood Green', 'Turnpike Lane', 'Manor House', 'Finsbury Park', 'Arsenal', 'Holloway Road', 'Caledonian Road', "King's Cross St. Pancras", 'Russell Square', 'Holborn', 'Covent Garden', 'Leicester Square', 'Piccadilly Circus', 'Green Park', 'Hyde Park Corner', 'Knightsbridge', 'South Kensington', 'Gloucester Road', "Earl's Court", 'Barons Court', 'Hammersmith (Dist&Picc Line)', 'Turnham Green', 'Acton Town', 'South Ealing', 'Northfields', 'Boston Manor', 'Osterley', 'Hounslow East', 'Hounslow Central', 'Hounslow West', 'Hatton Cross', 'Heathrow Terminal 4', 'Heathrow Terminals 1-2-3')  },
  # ...
  "piccadilly_3":{ "stations":('Acton Town', 'South Ealing', 'Northfields', 'Boston Manor', 'Osterley', 'Hounslow East', 'Hounslow Central', 'Hounslow West', 'Hatton Cross', 'Heathrow Terminals 1-2-3', 'Heathrow Terminal 5')  },
  # ...
  "victoria":{ "stations":('Walthamstow Central', 'Blackhorse Road', 'Tottenham Hale', 'Seven Sisters', 'Finsbury Park', 'Highbury & Islington', "King's Cross St. Pancras", 'Euston', 'Warren Street', 'Oxford Circus', 'Green Park', 'Victoria', 'Pimlico', 'Vauxhall', 'Stockwell', 'Brixton')  },
  # ...
}
