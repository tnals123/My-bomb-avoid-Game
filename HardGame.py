import Thread
import pygame
import time
import random

black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
pos_x=380
pox_y=650
score=0
easymode=True

def draw_score():
    global score
    smallfont=pygame.font.SysFont(None,30)
    realscore=smallfont.render('SCORE:'+str(score),True,(0,0,255))
    screen.blit(realscore,(650,0))
def game_over():
    global score
    smallfont2=pygame.font.SysFont(None,100)
    gameover=smallfont2.render('GAME OVER',True,(255,0,0))
    screen.blit(gameover,(200,380))
    
class Enemy_Car:
    def __init__(self):
        self.p1=Thread.Other_Car()
        
    
    def runGame(self):
        global score
        global pos_x
        global easymode
        self.st=Thread.Other_Car_Hard()
        car_img=pygame.image.load('bomb.png').convert_alpha()
        car_img=pygame.transform.scale(car_img,(75,75))
        cars=[]
        new_car=[]
        self.st.start()
        

        
        rect=pygame.Rect(car_img.get_rect())
        asdf=self.st.real
        
        rect.left=asdf
        rect.top=-100
        dy=3
        cars.append({'rect':rect,'dy':dy})
           
        
        while easymode:
                clock.tick(60)
                screen.fill((255,255,255))
                pygame.draw.line(screen,black,(100,0),(100,800))
                pygame.draw.line(screen,black,(200,0),(200,800))
                pygame.draw.line(screen,black,(300,0),(300,800))
                pygame.draw.line(screen,black,(400,0),(400,800))
                pygame.draw.line(screen,black,(500,0),(500,800))
                pygame.draw.line(screen,black,(600,0),(600,800))
                pygame.draw.line(screen,black,(700,0),(700,800))
                pygame.draw.line(screen,black,(800,0),(800,800))
                rect=pygame.Rect(car_img.get_rect())
                asdf=self.st.real

                rect.left=asdf
                rect.top=-100
                dy=3
                cars.append({'rect':rect,'dy':dy})

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        easymode=False
                key_event=pygame.key.get_pressed()
                if key_event[pygame.K_1]:
                    pos_x=30
                if key_event[pygame.K_2]:
                    pos_x=130
                if key_event[pygame.K_3] :
                    pos_x=230
                if key_event[pygame.K_4] :
                    pos_x=320
                if key_event[pygame.K_5] :
                    pos_x=430
                if key_event[pygame.K_6] :
                    pos_x=520
                if key_event[pygame.K_7] :
                    pos_x=620
                if key_event[pygame.K_8] :
                    pos_x=720
                    
                if key_event[pygame.K_RIGHT]:
                    if pos_x==50:
                        pos_x=380

               
                cars.append({'rect':rect,'dy':dy})
                for car in cars:
                    car['rect'].top+=car['dy']
                character=pygame.draw.rect(screen,black,[pos_x,650,50,50]) 
                draw_score()
                
                for car in cars:
                    if car['rect'].colliderect(character):
                        game_over()
                        easymode=False
                        
                        
                        
                    screen.blit(car_img,car['rect'])
                score+=2
                
                pygame.display.update()
          
            
       
    



            
        

