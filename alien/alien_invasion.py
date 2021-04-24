# coding=UTF-8
import sys
import pygame
import settings
from ship import Ship
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船
    ship = Ship(screen)



    # game loop
    while True:
        # supervise keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # fill color
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # visualiaze the window
        pygame.display.flip()
run_game()