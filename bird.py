import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.image_list = [pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                           pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect(centre = (100,100))