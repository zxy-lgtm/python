# coding=UTF-8

import sys

import pygame


def check_keydown_events(event,ship):
    #响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):

    # supervise keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship):

    # fill color
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # visualiaze the window
    pygame.display.flip()