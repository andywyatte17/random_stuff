import csv, os
import turtle
import line_list
import name_lookup

def from_csv(filename):
    stations = []
    with open(filename, 'r') as f:
        r = csv.reader(f)
        for row in r:
            stations += row
    return stations

vic = from_csv('victoria_line.csv')
nor_bank = from_csv('northern_bank.csv')
nor_charing_x = from_csv('northern_charing_x.csv')
central = from_csv('central_line.csv')
central_hainault = from_csv('central_hainault.csv')

gps = dict()
r = csv.reader(open('gps.csv', 'r'))
for row in r:
    gps[row[0]] = (float(row[1]), float(row[2]))

lat_min = min(gps.values(), key = lambda x: x[0])[0]
lat_max = max(gps.values(), key = lambda x: x[0])[0]
long_min = min(gps.values(), key = lambda x: x[1])[1]
long_max = max(gps.values(), key = lambda x: x[1])[1]

turtle.speed(1)
for line, col in ( (vic, (0,0.5,1.0)),
                   (nor_bank, (0,0,0)),
                   (nor_charing_x, (0,0,0)),
                   (central, (1,0,0)),
                   (central_hainault, (1,0,0))
                 ):
    turtle.penup()
    turtle.width(1.5)
    turtle.color(col)
    for st in line:
        if st in gps:
            latt, longt = gps[st]
            x = (longt - long_min)/(long_max-long_min)
            y = (latt - lat_min)/(lat_max-lat_min)
            x *= 200
            y *= 200
            turtle.setposition(x, y)
            #print(st)
            turtle.pendown()
        else: print("Missing - " + st)
