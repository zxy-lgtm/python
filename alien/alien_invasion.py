# coding=UTF-8
import sys
import pygame
import settings
from ship import Ship
from alien import Alien
import game_functions as gf 
from pygame.sprite import Group
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #子弹
    bullets = Group()

    #外星人
    #alien = Alien(ai_settings,screen)
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # game loop
    while True:
        # supervise keyboard and mouse item
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        #print(len(bullets))
        gf.update_aliens(ai_settings,aliens)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()