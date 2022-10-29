import os
from pygame_button import Button
import pygame
import pygame_textinput
import sys
from math import *
from pygame.locals import *

import blackjack
from blackjack import BlackJackGame
from interface import Display, Cartes

game_running = True
pygame.font.init()
display = Display()
cartes = Cartes()

text_input = pygame_textinput.TextInputVisualizer(font_object=display.default_font,
                                                  font_color=(255, 255, 255), cursor_color=(255, 255, 255))

pygame.key.set_repeat(200, 25)


def setup():
    setup_nbr_manager = pygame_textinput.TextInputManager(
        validator=lambda inp: len(inp) < 2 and inp.isnumeric() and int(inp) > 1)
    setup_nbr_input = pygame_textinput.TextInputVisualizer(manager=setup_nbr_manager, font_object=display.default_font,
                                                           font_color=(255, 255, 255), cursor_color=(255, 255, 255))
    players_pos = []
    while True:
        display.board()

        name_text = display.huge_font.render("PyJackGame", False, (255, 255, 255))
        display.screen.blit(name_text, (name_text.get_rect(center=(display.h / 2, 0))[0], name_text.get_rect().centery))

        setup_nbr_input.update(display.pg_events)
        display.screen.blit(setup_nbr_input.surface, (display.screen.get_rect().centerx, display.w / 2))

        text = display.small_font.render("Entrez le nombre de joueurs (vous y compris): ", False, (255, 255, 255))
        display.screen.blit(text, (
            display.h / 2 - text.get_rect().centerx, display.w / 2 - display.default_font.get_height()))

        confirm_text = display.ultra_small_font.render("Appuyez sur Entrer pour confirmer", False, (210, 210, 210))
        display.screen.blit(confirm_text, (confirm_text.get_rect(center=(display.h / 2, display.w / 1.75))))

        display.update()
        for event in display.pg_events:
            if event.type == KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    setup_nbr_input.value = ""
                if event.key in [pygame.K_KP_ENTER, pygame.K_RETURN]:
                    if setup_nbr_input.value != "":

                        display.reset_error()

                        rad_jrs = 2 / int(setup_nbr_input.value)
                        for jrs in range(int(setup_nbr_input.value)):
                            players_pos.append(
                                cartes.trigo_calc(rad_jrs * (jrs * 3.1), 310, (display.h / 2.5, display.w / 2.5)))

                        return int(setup_nbr_input.value), players_pos

                    else:
                        display.error = "Erreur: Mettez un chiffre."


def as_func(joueur):
    if joueur == 0:
        button_1 = Button((display.w / 3, display.h / 2, 50, 60), (150, 150, 150), lambda a: a)
        button_1.process_kwargs({"text": display.small_font.render("1", False, (255, 255, 255)),
                                 "hover_color": (200, 200, 200)})
        button_11 = Button((display.w / 1.5, display.h / 2, 50, 60), (150, 150, 150), lambda a: a)
        button_11.process_kwargs({"text": display.small_font.render("11", False, (255, 255, 255)),
                                  "hover_color": (200, 200, 200)})
        while True:
            display.board()

            for nbr, card in enumerate(game.j_perm_cards[0]):
                display.screen.blit(cartes.cards[list(card.keys())[0]][list(card.values())[0]],
                                    (display.w / 3 + nbr * 20, display.w / 1.3))

            pygame.draw.rect(display.screen, (100, 100, 100),
                             (display.w / 3.6, display.h / 4.1, display.w / 1.935, display.h / 2.9))
            pygame.draw.rect(display.screen, (150, 150, 150),
                             (display.w / 3.5, display.h / 4, display.w / 2, display.h / 3))
            display.screen.blit(display.small_font.render("Vous avez récupéré un AS.", False,
                                                          (255, 255, 255)), (display.w / 3.2, display.h / 3.5))
            display.screen.blit(display.ultra_small_font.render("Voulez vous l'utiliser comme 1 ou 11?", False,
                                                                (255, 255, 255)), (display.w / 3.1, display.h / 3))
            button_1.update(display.screen)
            button_11.update(display.screen)

            display.update()

            for event in display.pg_events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_1.rect.collidepoint(event.pos):
                        return 1
                    if button_11.rect.collidepoint(event.pos):
                        return 11

    else:
        if game.players_result[joueur] >= 10:
            return 11
        else:
            return 1


def retire_func(joueur):
    if joueur == 0:
        button_oui = Button((display.w / 3, display.h / 2, 75, 60), (150, 150, 150), lambda a: a)
        button_oui.process_kwargs({"text": display.small_font.render("Oui", False, (255, 255, 255)),
                                   "hover_color": (200, 200, 200)})
        button_non = Button((display.w / 1.5, display.h / 2, 75, 60), (150, 150, 150), lambda a: a)
        button_non.process_kwargs({"text": display.small_font.render("Non", False, (255, 255, 255)),
                                   "hover_color": (200, 200, 200)})
        while True:
            display.board()

            for nbr, card in enumerate(game.j_perm_cards[0]):
                display.screen.blit(cartes.cards[list(card.keys())[0]][list(card.values())[0]],
                                    (display.w / 3 + nbr * 20, display.w / 1.3))

            pygame.draw.rect(display.screen, (100, 100, 100),
                             (display.w / 3.6, display.h / 4.1, display.w / 1.935, display.h / 2.9))
            pygame.draw.rect(display.screen, (150, 150, 150),
                             (display.w / 3.5, display.h / 4, display.w / 2, display.h / 3))
            display.screen.blit(display.small_font.render("Vous avez plus de 16.", False,
                                                          (255, 255, 255)), (display.w / 3.2, display.h / 3.5))
            display.screen.blit(display.ultra_small_font.render("Voulez-vous vous arrêter?", False,
                                                                (255, 255, 255)), (display.w / 3.1, display.h / 3))
            button_oui.update(display.screen)
            button_non.update(display.screen)

            display.update()

            for event in display.pg_events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_oui.rect.collidepoint(event.pos):
                        return True
                    if button_non.rect.collidepoint(event.pos):
                        return False
    else:
        if game.players_result[joueur] > 17:
            return False
        else:
            return True


if "__main__" == __name__:
    nbr_jrs, players_pos = setup()
    game = blackjack.BlackJackGame(nbr_jrs)
    reveal = False

    ok = True

    button_ok = Button((display.w / 2.4, display.h / 2, 190, 60), (150, 150, 150), lambda a: a)
    button_ok.process_kwargs({"text": display.small_font.render("Tour suivant", False, (255, 255, 255)),
                              "hover_color": (200, 200, 200)})

    while True:
        display.board()

        for ply_cards in game.j_perm_cards:
            for nbr, card in enumerate(game.j_perm_cards[ply_cards]):
                if ply_cards == 0 or reveal:
                    display.screen.blit(cartes.cards[list(card.keys())[0]][list(card.values())[0]],
                                        (players_pos[ply_cards][0] + nbr * 20, players_pos[ply_cards][1]))
                else:
                    display.screen.blit(cartes.cards["Reversed"][0],
                                        (players_pos[ply_cards][0] + nbr * 20, players_pos[ply_cards][1]))
        for x in range(game.cards_remaining):
            display.screen.blit(cartes.cards["Reversed"][1],
                                (display.w / 3 - cartes.cards["Reversed"][1].get_rect()[0] / 2.3 + x * 3,
                                 display.h / 2.7 - cartes.cards["Reversed"][1].get_rect()[1] / 2))
        display.screen.blit(display.small_font.render("Vous:", False, (255, 255, 255)),
                            (players_pos[0][0], players_pos[0][1] - 35))

        if game.cards_remaining == 0 or game.j_cards == {}:
            reveal = True
            pygame.draw.rect(display.screen, (100, 100, 100),
                             (display.w / 3.6, display.h / 4.1, display.w / 1.935, display.h / 2.9))
            pygame.draw.rect(display.screen, (150, 150, 150),
                             (display.w / 3.5, display.h / 4, display.w / 2, display.h / 3))
            display.screen.blit(display.default_font.render("Terminé!", True, (255, 255, 255)),
                                (display.w / 2, display.h / 4))
        else:
            button_ok.update(display.screen)
            if ok:
                game.next_round(as_func, retire_func)
                ok = False

        display.update()

        for event in display.pg_events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_ok.rect.collidepoint(event.pos):
                    ok = True
