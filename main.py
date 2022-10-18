import pygame
from pygame.locals import *
from blackjack import BlackJackGame

game_running = True
game = BlackJackGame(2)

while game_running:
    game.next_round()
