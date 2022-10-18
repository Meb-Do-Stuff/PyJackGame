import sys
import pygame
from pygame.locals import *


class Cartes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        pass


class Display:
    def __init__(self):
        pygame.init()
        self.pg_events = []
        self.screen = pygame.display.set_mode((960, 810))
        self.clock = pygame.time.Clock()
        self.h, self.w = self.screen.get_size()
        pygame.display.set_caption("PyJack")

    def board(self):
        self.screen.fill((0, 120, 0), (0, 0, self.h, self.w))

    def update(self):
        self.clock.tick(30)

        pygame.display.flip()

        self.pg_events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):  # Quit
                sys.exit()
