import unittest
from station_data import StationData
import json
import data.data_js as data_js
import data.data_routes as data_routes


class TestStationData(unittest.TestCase):

    def test_go_routes_central_line(self):
        sd = StationData()
        routes = sd.GoRoutes("Epping", "West Ruislip")
        self.assertEqual(['central_west_ruislip'], routes)

    def test_calculate_remains_fails_when_run_twice(self):
        sd = StationData()
        stationList = ( ("Epping", None, None), ("Woodford", 0, "central_west_ruislip") )
        result = sd.CalculateRemainsByLine([("Epping", None, None)])
        count = sum([len(result[key]) for key in result.keys()])
        self.assertEqual(385, count)

        result = sd.CalculateRemainsByLine(stationList)
        count = sum([len(result[key]) for key in result.keys()])
        self.assertEqual(380, count)

        result = sd.CalculateRemainsByLine(stationList)
        count = sum([len(result[key]) for key in result.keys()])
        self.assertEqual(380, count)


class TestDataJs(unittest.TestCase):

    def test_district_line(self):
        district = ['Acton Town', 'Aldgate East', 'Barking', 'Barons Court', 'Bayswater', 'Becontree', 'Blackfriars', 'Bow Road', 'Bromley-by-Bow', 'Cannon Street', 'Chiswick Park', 'Dagenham East', 'Dagenham Heathway', 'Ealing Broadway', 'Ealing Common', "Earl's Court", 'East Ham', 'East Putney', 'Edgware Road (Circle Line)', 'Elm Park', 'Embankment', 'Fulham Broadway', 'Gloucester Road', 'Gunnersbury', 'Hammersmith (Dist&Picc Line)', 'High Street Kensington', 'Hornchurch', 'Kensington (Olympia)', 'Kew Gardens', 'Ladbroke Grove', 'Latimer Road', 'Mansion House', 'Mile End', 'Monument', 'Notting Hill Gate', 'Paddington', 'Parsons Green', 'Plaistow', 'Putney Bridge', 'Ravenscourt Park', 'Richmond', 'Sloane Square', 'South Kensington', 'Southfields', "St. James's Park", 'Stamford Brook', 'Stepney Green', 'Temple', 'Tower Hill', 'Turnham Green', 'Upminster', 'Upminster Bridge', 'Upney', 'Upton Park', 'Victoria', 'West Brompton', 'West Ham', 'West Kensington', 'Westminster', 'Whitechapel', 'Wimbledon', 'Wimbledon Park']
        district2 = set(data_js.stationsR[x] for x in district)
        #stations = sorted(data_js.stations[x] for x in data_js.stationsOnLines['district'])
        stations2 = set(x for x in data_js.stationsOnLines['district'])
        #print(repr(stations2))
        self.assertEqual(district2, stations2)


if __name__ == '__main__':
    unittest.main()