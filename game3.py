#/usr/bin/env python
import time
import string
import random
import math

# PyGame Constants
import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import box
import manager
import gameobject

import math

class Player(box.Box):
        def __init__(self):
                box.Box.__init__(self)
                self.speed = 7
                self.name = "Player"
        def update(self):
                keys = pygame.key.get_pressed()
                if keys[K_n]:
                        for i in range(10):
                                Target(pos=(random.random()*400,random.random()*400))
                if keys[K_UP]:
                        self.y -= self.speed
                if keys[K_DOWN]:
                        self.y += self.speed
                if keys[K_LEFT]:
                        self.x -= self.speed
                if keys[K_RIGHT]:
                        self.x += self.speed
                if keys[K_SPACE]:
                        if True:#Bullet.numOf < 2:
                                Bullet(pos=(self.x+self.width,self.y+self.height/2),angle=random.random()*360)

class Bullet(box.Box):
        numOf = 0
        def __init__(self,size=(5,5),pos=(20,20),angle=0):
                box.Box.__init__(self,size=size,pos=pos)
                self.name = "Bullet"
                Bullet.numOf += 1
                self.speed = 5
                self.angle = angle
        def update(self):
                self.x += self.speed * math.cos(self.angle * (math.pi / 180))
                self.y += self.speed * math.sin(self.angle * (math.pi / 180))
        def collision(self,obj):
                if obj.name == "Target":
                        self.status = 0
        def destroy(self):
                Bullet.numOf -= 1
class Target(box.Box):
        def __init__(self,pos=(100,100)):
                box.Box.__init__(self,pos=pos)
                self.name = "Target"
        def collision(self,obj):
                if obj.name == "Bullet":
                        self.status = 0
def main():
        world = manager.World()
        Player()
        Target()
        world.run()
        
if __name__=="__main__":
	main()


