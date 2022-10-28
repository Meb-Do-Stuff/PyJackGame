import pygame
import pygame_textinput
import sys
from pygame.locals import *
from blackjack import BlackJackGame
from interface import Display, Cartes

game_running = True
pygame.font.init()
display = Display()
default_font = pygame.font.SysFont("Arial Bold", 55)
text_input = pygame_textinput.TextInputVisualizer(font_object=default_font,
                                                  font_color=(255, 255, 255), cursor_color=(255, 255, 255))

pygame.key.set_repeat(200, 25)


def setup():
    is_setup = True
    setup_nbr_manager = pygame_textinput.TextInputManager(validator=lambda inp: len(inp) < 2 and inp.isnumeric())
    setup_nbr_input = pygame_textinput.TextInputVisualizer(manager=setup_nbr_manager, font_object=default_font,
                                                           font_color=(255, 255, 255), cursor_color=(255, 255, 255))
    while is_setup:
        display.board()

        setup_nbr_input.update(display.pg_events)
        display.screen.blit(setup_nbr_input.surface, (display.screen.get_rect().centerx, display.w/2))

        text = default_font.render("Test", False, (255, 255, 255))
        display.screen.blit(text, (10, 10, 10, 10))

        display.update()
        for event in display.pg_events:
            if event.type == KEYDOWN and event.key == pygame.K_BACKSPACE:
                setup_nbr_input.value = ""


if "__main__" == __name__:
    setup()

    while game_running:
        display.board()

        display.update()
        # game.next_round()
