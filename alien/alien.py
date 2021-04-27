# coding=UTF-8
import  pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):

        #初始化外星人并设置位置
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('images/alien.bmp')

        #将图片缩小
        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #将外星人放在屏幕
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #在外星人的属性center中存储小数值
        self.x = float(self.rect.x)

        #外星人设置
        self.ai_settings.alien_speed_factor = ai_settings.alien_speed_factor


    def blitme(self):
        #在指定位置放置飞船
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        if self.ai_settings.fleet_direction == 1 :
            self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
            self.rect.x = self.x