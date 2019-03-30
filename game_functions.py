#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Gong@2019-03-30
import pygame
import sys


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # get other keys
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def update_screen(ai_settings, screen, ship):
    '''update screen'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #show new screen
    pygame.display.flip()
