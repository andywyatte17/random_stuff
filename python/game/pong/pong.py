#!/usr/bin/env python3
# python3 -m pgzero invaders.py

import pygame
from pgzrun import *
import random

WIDTH, HEIGHT = 640, 480

class BasicObject() : pass

player_1_score = 0
player_2_score = 0

left_bat = Actor('pong_bat')
left_bat.x = 20
right_bat = Actor('pong_bat')
right_bat.x = 620
ball_pos = BasicObject()
ball_pos.x = WIDTH/2
ball_pos.y = HEIGHT/2 
ball_radius = 5
ball_direction = BasicObject()
ball_direction.x = 0
ball_direction.y = 0
ball_speed_multiplier = 2.5

started = False

def start_game():
    global started
    if not started:
        started = True
        ball_pos.x = WIDTH/2
        ball_pos.y = random.randint(20, HEIGHT - 20)
        ball_direction.x = 1
        ball_direction.y = 0.2

def ball_left():
    return ball_pos.x - ball_radius

def ball_right():
    return ball_pos.x + ball_radius

def ball_top():
    return ball_pos.y - ball_radius

def ball_bottom():
    return ball_pos.y + ball_radius

def draw():
    screen.fill( (197, 201, 179) ) 
    left_bat.draw()
    right_bat.draw()
    screen.draw.filled_circle((ball_pos.x, ball_pos.y), ball_radius, (5, 80, 20))
    screen.draw.text(str(player_1_score), (10, 25))
    screen.draw.text(str(player_2_score), (WIDTH-10, 25))

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

def end_point(what_happened):
    global player_1_score, player_2_score, started
    if what_happened=="left wins":
        player_1_score += 1
        started = False
    if what_happened=="right wins":
        player_2_score += 1
        started = False

def is_in_range(x, lo, hi):
    return lo<=x and x<=hi

def check_collisions():
    if not started: return

    # Check for right_bat / ball collision
    if is_in_range(ball_right(), right_bat.left, right_bat.left + 3):
        if ball_bottom() < right_bat.top or \
           ball_top() > right_bat.bottom:
           end_point("left wins")
           return
        else:
            # change ball direction
            ball_direction.x = -ball_direction.x
            return

    # Check for left_bat / ball collision
    if is_in_range(ball_left(), left_bat.right - 3, left_bat.right):
        if ball_bottom() < left_bat.top or \
           ball_top() > left_bat.bottom:
           end_point("right wins")
           return
        else:
            # change ball direction
            ball_direction.x = -ball_direction.x
            return

    # Check for top- or bottom- screen collision
    if ball_bottom() > HEIGHT or ball_top() < 0:
        ball_direction.y = -ball_direction.y

def update():
    global ball_speed_multiplier
    ball_pos.x = ball_pos.x + ball_direction.x * ball_speed_multiplier
    ball_pos.y = ball_pos.y + ball_direction.y * ball_speed_multiplier
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
    if keyboard.R:
        start_game()
    if keyboard.KP_PLUS:
        ball_speed_multiplier *= 1.1
        if ball_speed_multiplier > 2.5: ball_speed_multiplier = 2.5
    if keyboard.KP_MINUS:
        ball_speed_multiplier /= 1.1
        if ball_speed_multiplier < 0.2: ball_speed_multiplier = 0.2
    check_collisions()

go() # Start the game!
