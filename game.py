import pygame as pg
import sys

pg.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height = 700
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width,self.height))
        self.bg_img = pg.transform.scale(pg.image.load("assets/bg.png").convert(),(600,1066))
        
        self.gameloop()

    def gameloop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit
            self.win.blit(self.bg_img,(0,-300))
            pg.display.update()

game = Game()
