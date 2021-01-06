import pygame as pg
from random import randint

from hero import Hero
# from field import Field


class StarFall:
    def __init__(self, hero: Hero, field, surface: pg.Surface):
        self.hero = hero
        self.field = field
        self.screen = surface
        self.running = False

    def start(self):
        self.running = True

    def loop(self):
        callback = None
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    callback = 'closeEvent'
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        callback = 'gameOver'
                        self.running = False
                self.screen.fill('black')
                pg.display.flip()
        return callback