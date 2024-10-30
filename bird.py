import pygame as pg
import sys , time

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.img_list = [pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                           pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center = (100,100))
        self.y_velocity = 0
        self.gravity = 10

    def update(self,dt):
        self.y_velocity += self.gravity
    