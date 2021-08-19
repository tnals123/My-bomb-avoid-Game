import pygame

import time
import sys

import Game_Button
pygame.init()
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)

clock=pygame.time.Clock()
pygame.display.set_caption('Bomb Moving Game')



if __name__=="__main__":
    player=Game_Button
    player.Main_Manu()

         

pygame.quit()
sys.exit()
