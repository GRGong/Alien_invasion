#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Gong@2019-03-30

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #build a bullet at (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet.width, ai_settings.bullet.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #float position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet.color
        self.speed_factor = ai_settings.bullet.speed_factor

