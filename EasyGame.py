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
easymode=True
class Enemy_Car:
    def __init__(self):
        self.p1=Thread.Other_Car()
        
    
    def runGame(self):
    
        global pos_x
        global easymode
        self.st=Thread.Other_Car()
        car_img=pygame.image.load('bomb.png').convert_alpha()
        car_img=pygame.transform.scale(car_img,(75,75))
        cars=[]
        new_car=[]
        self.st.start()
        score=0

        
        rect=pygame.Rect(car_img.get_rect())
        asdf=self.st.real
        
        rect.left=asdf
        rect.top=-100
        dy=3
        cars.append({'rect':rect,'dy':dy})
           
        
        while easymode:
                clock.tick(60)
                screen.fill((255,255,255))
                pygame.draw.line(screen,black,(266,0),(266,800))
                pygame.draw.line(screen,black,(532,0),(532,800))
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
                    pos_x=50
                if key_event[pygame.K_2]:
                    pos_x=380
                if key_event[pygame.K_3] :
                    pos_x=700
                    
                if key_event[pygame.K_RIGHT]:
                    if pos_x==50:
                        pos_x=380

               
                cars.append({'rect':rect,'dy':dy})
                for car in cars:
                    car['rect'].top+=car['dy']
                character=pygame.draw.rect(screen,black,[pos_x,650,50,50])   
                for car in cars:
                    if car['rect'].colliderect(character):
                        score+=100
                        print(score)
                    screen.blit(car_img,car['rect'])
                
                pygame.display.update()
          
            
       
    



            
        

