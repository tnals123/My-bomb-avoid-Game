import pygame
import Main_Manu_01
import time
import sys
import EasyGame
import NormalGame
import HardGame
clock=pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
pygame.init()
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)

startimg=pygame.image.load("starticon.png")
startactimg=pygame.image.load("clickedStartIcon.png")
quitimg=pygame.image.load("quiticon.png")
quitactimg=pygame.image.load("clickedQuitIcon.png")
smallfont=pygame.font.SysFont(None,50)
title=smallfont.render('AVOID BOMB GAME!',True,(0,0,255))
selctdifficulty=smallfont.render('Select Game Mode',True,(0,0,255))
texteasy=smallfont.render('easy',True,(0,0,0))
texteasy2=smallfont.render('easy',True,(100,100,100))
textnormal=smallfont.render('normal',True,(0,0,0))
textnormal2=smallfont.render('normal',True,(100,100,100))
texthard=smallfont.render('hard',True,(0,0,0))
texthard2=smallfont.render('hard',True,(100,100,100))

b1=Main_Manu_01.Main()

class Button:
    def __init__(self,img,x,y,width,height,img_act,x_act,y_act,action=None):
        global screen
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+width>mouse[0]>x and y+height>mouse[1]:
            screen.blit(img_act,(x_act,y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img,(x,y))


class Button2:
    def __init__(self,text,x,y,width,height,text_act,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+width>mouse[0]>x and y+height>mouse[1]:
            screen.blit(text_act,(x,y))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(text,(x,y))   

def Easy_Mode():
    global screen
    player1=EasyGame.Enemy_Car()
    player1.runGame()
def Normal_Mode():
    player2=NormalGame.Enemy_Car()
    player2.runGame()
def Hard_Mode():
    player3=HardGame.Enemy_Car()
    player3.runGame()
            
            
    

def quitgame():
    pygame.quit()
    sys.exit()

def selecscreen():
    global screen
    select=True
    while select:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    select=False

            screen.fill((255,255,255))
            screen.blit(selctdifficulty,(200,200))
            easymode=Button2(texteasy,80,540,60,30,texteasy2,Easy_Mode)
            normalmode=Button2(textnormal,350,540,60,30,textnormal2,Normal_Mode)
            hardmode=Button2(texthard,650,540,60,30,texthard2,Hard_Mode)          
            pygame.display.update()

def Main_Manu():
    global screen
    mainmanu=True
    while mainmanu:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainmanu=False

            screen.fill((255,255,255))
            screen.blit(title,(150,300))
            startbutton=Button(startimg,280,517,60,20,startactimg,277,514,selecscreen)
            quitbutton=Button(quitimg,480,517,60,20,quitactimg,477,514,quitgame)
            pygame.display.update()

        


    
