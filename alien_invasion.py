#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Gong@2019-03-29

import sys
import pygame
import settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    while True:
        gf.check_events(ship)
        ship.update_self()
        gf.update_screen(ai_settings, screen, ship)


run_game()
