# coding=UTF-8
import sys
import pygame
import settings
from ship import Ship
import game_functions as gf
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船
    ship = Ship(ai_settings,screen)



    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()