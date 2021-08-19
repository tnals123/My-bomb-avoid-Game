import pygame
import threading

import random
import time

class Other_Car(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.val=0
        self.real=1
    def run(self):
        while True:
            ran=random.randint(1,3)
            self.val=ran
            
            
            if self.val==1:
                self.real=50
            elif self.val==2:
                self.real=380
            elif self.val==3:
                self.real=650
            
            
            time.sleep(0.5)
            pygame.display.update()

class Other_Car_Normal(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.val=0
        self.real=1
    def run(self):
        while True:
            ran=random.randint(1,5)
            self.val=ran
            
            if self.val==1:
                self.real=50
            elif self.val==2:
                self.real=250
            elif self.val==3:
                self.real=400
            elif self.val==4:
                self.real=550
            elif self.val==5:
                self.real=700
            time.sleep(2)
            

class Other_Car_Hard(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.val=0
        self.real=1
    def run(self):
        while True:
            ran=random.randint(1,8)
            self.val=ran
            
            if self.val==1:
                self.real=30
            elif self.val==2:
                self.real=130
            elif self.val==3:
                self.real=230
            elif self.val==4:
                self.real=320
            elif self.val==5:
                self.real=430
            elif self.val==6:
                self.real=520
            elif self.val==7:
                self.real=620
            elif self.val==8:
                self.real=720
            time.sleep(0.15)
            

            


        
        
 
        
        
        
        