import threading
import pygame
import game1

class Score(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.score=0
        self.player=game1
        
    def run(self):
        self.player.Get_Score()

