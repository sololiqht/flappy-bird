import pygame as pg
import sys , time
from bird import Bird
from pipes import Pipe


pg.init()

class Game:
    def __init__(self):
        #setting window config
        self.width = 600
        self.height = 700
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width,self.height))
        self.clock = pg.time.Clock()
        self.move_speed = 100
        self.bird = Bird(self.scale_factor)
        self.is_enter_pressed = False
        self.pipe_generate_counter = 301
        self.start_monitoring = False
        self.score = 0
        self.font = pg.font.Font("assets/font.ttf",24)
        self.score_text = self.font.render("Score: 0 ",True,(255,255,255))
        self.score_rect = self.score_text.get_rect(center = (100,30))
        self.restart_text = self.font.render("Restart",True,(255,255,255))
        self.restart_rect = self.restart_text.get_rect(center = (300,300))
        self.pipes = []
        self.is_game_started = True

        self.imagesetup()
        self.gameloop()
        


    def gameloop(self):
        last_time = time.time()
        while True:
            # calculate delta time
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit
                if event.type==pg.KEYDOWN and self.is_game_started:
                    if event.key==pg.K_RETURN:
                        self.bird.update_on = True
                        self.is_enter_pressed=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.restart_rect.collidepoint(pg.mouse.get_pos()):
                        self.restartgame()

            self.update(dt)
            self.render()
            self.checkCollisions()
            self.checkscore()
            pg.display.update()
            self.clock.tick(60)

    def restartgame(self):
        self.score=0
        self.is_enter_pressed=False
        self.is_game_started=True
        self.bird.resetposition()
        self.pipes.clear()
        self.pipe_generate_counter = 301
        self.bird.update_on = False

    def checkscore(self):
        if len(self.pipes)>0:
            if (self.bird.rect.left>self.pipes[0].rect_down.left and 
            self.bird.rect.right < self.pipes[0].rect_down.right and not self.start_monitoring):
                self.start_monitoring = True
            if self.bird.rect.left > self.pipes[0].rect_down.right and self.start_monitoring:
                self.start_monitoring = False
                self.score+=1
                self.score_text = self.font.render(f"Score: {self.score}" ,True,(255,255,255))
                

    def checkCollisions(self):
        if len(self.pipes):
            if self.bird.rect.bottom>568:
                self.bird.update_on=False
                self.is_enter_pressed=False
                self.is_game_started = False
            if (self.bird.rect.colliderect(self.pipes[0].rect_down) or
            self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.is_enter_pressed=False
                self.is_game_started = False

    def update(self,dt):
        if self.is_enter_pressed:
            # grounds
            self.ground1_rect.x -= self.move_speed*dt
            self.ground2_rect.x -= self.move_speed*dt

            if self.ground1_rect.right<0:
                self.ground1_rect.x = self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x = self.ground1_rect.right
            #generating pipes
            if self.pipe_generate_counter>300:
                self.pipes.append(Pipe(self.scale_factor,self.move_speed))
                self.pipe_generate_counter=0
                
            self.pipe_generate_counter+=1

            for pipe in self.pipes:
                    pipe.update(dt)
            
            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)

            # bird
        self.bird.update(dt)

    def render(self):
        self.win.blit(self.bg_img,(0,-300))
        for pipe in self.pipes:
            pipe.drawpipe(self.win)
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)
        self.win.blit(self.score_text,self.score_rect)
        if not self.is_game_started:
            self.win.blit(self.restart_text,self.restart_rect)
        

    def imagesetup(self):
        #loading images for bg and ground
        self.bg_img = pg.transform.scale_by(pg.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1_img= pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2_img= pg.transform.scale_by(pg.image.load("assets/ground.png").convert(),self.scale_factor)

        self.ground1_rect= self.ground1_img.get_rect()
        self.ground2_rect= self.ground2_img.get_rect()

        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568


game = Game()
