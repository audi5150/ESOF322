import pygame as pg
from pygame.locals import *
import sys
pg.init()

FPS = 60
FramePerSec = pg.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

DISPLAYSURF = pg.display.set_mode((1000,600))
DISPLAYSURF.fill(WHITE)
#_______[ground level shoulkd be around y = 500]__________

vel = 5
x = 50
y =50
is_jumping = False
jump_count =10
class Luigi(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('50luigi.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x=x
        self.y=y
        self.is_jumping = False
        self.jump_count = jump_count
        self.vel = vel
        
    def update(self):
        keys = pg.key.get_pressed()
        if self.rect.left >0 :
            if keys[pg.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH:
            if keys[pg.K_RIGHT]:
                self.rect.move_ip(5,0)
       
        if not(self.is_jumping): 
            if keys[pg.K_UP]:
                self.rect.move_ip(0,-5)

            if keys[pg.K_DOWN]:
                self.rect.move_ip(0,5)

            if keys[pg.K_SPACE]:
                self.is_jumping = True
                if jump_count >= -10:
                    self.y -= (jump_count * abs(jump_count)) * 0.5
                    self.jump_count -= 1
                else: 
                    self.jump_count = 10
                    self.is_jumping = False
                    
          
           
            
    def draw(self,surface):
        surface.blit(self.image, self.rect)

        
p1 = Luigi()


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    
            
    p1.update()
    DISPLAYSURF.fill(WHITE)
    p1.draw(DISPLAYSURF)

    pg.display.update()
    FramePerSec.tick(FPS)
            
