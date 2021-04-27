# coding=UTF-8
class Settings():

    """储存《外星人入侵》的所有设置类"""

    def __init__(self):
        """屏幕设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,250,250)
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 1
        #1表示右，-1表示左
        self.fleet_direction = 1