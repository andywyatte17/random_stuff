import csv, os, sys
import turtle
import line_list
from name_lookup import convert as nlconv

def from_csv(filename):
    stations = []
    with open(filename, 'r') as f:
        r = csv.reader(f)
        for row in r:
            stations.append(row[0])
    return stations

vic = from_csv('victoria_line.csv')
nor_bank = from_csv('northern_bank.csv')
nor_charing_x = from_csv('northern_charing_x.csv')
central = from_csv('central_line.csv')
central_hainault = from_csv('central_hainault.csv')
metro_amersham = from_csv('metro_amersham.csv')
metro_watford = from_csv('metro_watford.csv')

gps = dict()
r = csv.reader(open('gps.csv', 'r'))
for row in r:
    gps[row[0]] = (float(row[1]), float(row[2]))

lat_min = min(gps.values(), key = lambda x: x[0])[0]
lat_max = max(gps.values(), key = lambda x: x[0])[0]
long_min = min(gps.values(), key = lambda x: x[1])[1]
long_max = max(gps.values(), key = lambda x: x[1])[1]

W,H=450,350
turtle.color(0.9, 0.9, 0.9)
turtle.penup()
for x,y in ((-1,-1),(1,-1),(1,1),(-1,1),(-1,-1)):
  turtle.setposition(x*W*0.5,y*H*0.5)
  turtle.pendown()

turtle.speed(1)
for line, col in ( (vic, (0,0.5,1.0)),
                   (nor_bank, (0,0,0)),
                   (nor_charing_x, (0,0,0)),
                   (central, (1,0,0)),
                   (central_hainault, (1,0,0)),
                   (metro_watford, (1,0,1)),
                   (metro_amersham, (1,0,1))
                 ):
    turtle.penup()
    turtle.width(1.5)
    turtle.color(col)
    for st in line:
        st = nlconv(st)
        if st in gps:
            latt, longt = gps[st]
            x = (longt - long_min)/(long_max-long_min)
            y = (latt - lat_min)/(lat_max-lat_min)
            x -= 0.5
            y -= 0.5
            x = x*W
            y = y*H
            turtle.setposition(x, y)
            turtle.pendown()
        else:
            print(st)
