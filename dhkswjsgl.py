import pygame
import Game_Button

black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
startimg=pygame.image.load("starticon.png")
startactimg=pygame.image.load("clickedStartIcon.png")
class Main:
    def __init__(self):
        pass
    def Title(self):
        self.screen = pygame.display.set_mode((800,800))
        self.screen.fill((255,255,255))
        self.font=pygame.font.SysFont(None,80)
        self.img=self.font.render('AVOID CAR GAME!',True,blue)
        self.screen.blit(self.img,(150,300))
        self.mouse=pygame.mouse.get_pos()
        print(self.mouse)
        