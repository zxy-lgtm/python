# coding=UTF-8
import pygame

class Ship():
    def __init__(self,ai_settings,screen):

        #初始化飞船并设置位置
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')

        #将图片缩小
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

        #飞船设置
        self.ai_settings.ship_speed_factor = 1.5

    
    def update(self):
        #根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        #在指定位置放置飞船
        self.screen.blit(self.image,self.rect)
    