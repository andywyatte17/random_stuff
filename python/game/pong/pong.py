#!/usr/bin/env python3
# python3 -m pgzero invaders.py

import pygame
from pgzrun import *

WIDTH, HEIGHT = 640, 480

left_bat = Actor('pong_bat')
left_bat.x = 20
right_bat = Actor('pong_bat')
right_bat.x = 620

def draw():
    screen.fill( ( 96, 32, 16) )
    left_bat.draw()
    right_bat.draw()

def corrected_bat_ys(bat_top, bat_bottom):
    if bat_top <= 5:
        correction = 5 - bat_top
        bat_bottom += correction
        bat_top += correction
    if bat_bottom >= HEIGHT - 5:
        correction = HEIGHT - 5 - bat_bottom
        bat_bottom += correction
        bat_top += correction
    return bat_top, bat_bottom

def update():
    if keyboard.W:
        left_bat.y = left_bat.y - 5
        left_bat.top, left_bat.bottom = \
            corrected_bat_ys(left_bat.top, left_bat.bottom)
    if keyboard.S:
        left_bat.y = left_bat.y + 5
        left_bat.top, left_bat.bottom = \
            corrected_bat_ys(left_bat.top, left_bat.bottom)
    if keyboard.K:
        right_bat.y = right_bat.y - 5
        right_bat.top, right_bat.bottom = \
            corrected_bat_ys(right_bat.top, right_bat.bottom)
    if keyboard.M:
        right_bat.y = right_bat.y + 5
        right_bat.top, right_bat.bottom = \
            corrected_bat_ys(right_bat.top, right_bat.bottom)

go() # Start the game!
