import pygame
screen = pygame.display.set_mode((600,800))
class Line:
    def __init__(self):
        self.name=0
    def BackGround(self):
        pygame.draw.rect(screen,(0,0,0),[40,40,50,20],2)