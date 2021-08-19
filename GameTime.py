import threading
import random
import pygame
import time
import game2
count=0
point=1

def timer():
    global point
    global count
    count+=1
    point=count*100
    print(count)
    print(point)
    time=threading.Timer(1,timer)
    time.start()
    if count==5:
        time.cancel()

class Time(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timer()
        
            


class Other_Car(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.val=0
        self.time=1
    def run(self):
        game=True
        while game:
            ran=random.randint(1,3)
            self.val=ran
            print(self.val)
            time.sleep(1)
            if self.val==3:
                break



