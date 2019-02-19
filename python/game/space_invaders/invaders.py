#!/usr/bin/env python3.6
# python3.6 -m pgzero invaders.py

import pygame
import glob
from pgzrun import *
from random import choice

WIDTH, HEIGHT = 320, 240

def CorrectedBounds(actor):
    global WIDTH, HEIGHT
    x = min(actor.x, WIDTH - actor.width / 2)
    x = max(actor.width / 2, x)
    return x, actor.y

def SetupAliens():
    aliens = list()
    the_actor = Actor('alien')
    w, h = the_actor.width, the_actor.height
    for x in range(w, int(WIDTH*0.66), w * 2):
        for y in range(h, 7 * h, h*2):
            alien = Actor('alien')
            alien.x = x
            alien.y = y
            aliens.append(alien)
    return aliens

aliens = SetupAliens()
lasers = list()

ship = Actor('ship')
ship.x, ship.y = 300, HEIGHT - ship.height

def key_down_ship():
    if keyboard.z:
        ship.x -= 10
        ship.x, ship.y = CorrectedBounds(ship)
    if keyboard.x:
        ship.x += 10
        ship.x, ship.y = CorrectedBounds(ship)

def on_key_down():
    if keyboard.space:
        laser = Actor('laser')
        laser.x = ship.x
        laser.y = ship.y
        lasers.append( laser )
        return
    if keyboard.q:
        quit()
        return

def draw():
    screen.fill((32, 16, 16))
    for alien in aliens:
        alien.draw()
    for laser in lasers:
        laser.draw()
    ship.draw()

# print([(a.left,a.top) for a in aliens])

def DeleteAlien(aliens, lasers):
    if len(lasers)>0:
        #print([(a.left, a.top) for a in aliens])
        #print([(a.left, a.top) for a in lasers])
        #quit()
        pass

    for ai in range(len(aliens)):
        alien = aliens[ai]
        def MakeHit(alien):
            a = alien
            return lambda x,y: a.left<=x and x<=a.right and a.top<=y and y<=a.bottom
        hit = MakeHit(alien)
        for li in range(len(lasers)):
            laser = lasers[li]
            if hit(laser.left, laser.top) or hit(laser.right, laser.bottom):
                return ai, li
    return -1, -1

def MoveAlien(alien):
    try: alien.direction
    except: alien.direction = 1
    alien.x += alien.direction * 0.25
    x = alien.x
    alien.x, alien.y = CorrectedBounds(alien)
    if x != alien.x:
        if alien.direction==1:
            alien.x -= alien.width
        else:
            alien.x += alien.width
        alien.direction *= -1
        alien.y += 16

def update():
    key_down_ship()
    for alien in aliens:
        MoveAlien(alien)
    while True:
        ai, li = DeleteAlien(aliens, lasers)
        if ai<0:
            break
        del aliens[ai]
        del lasers[li]
    for laser in lasers:
        laser.y -= 3
        laser.x, laser.y = CorrectedBounds(laser)

go()