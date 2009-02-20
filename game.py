#/usr/bin/env python
import time
import string
import random

# PyGame Constants
import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import box
import manager
import gameobject

class Player(box.Box):
        def __init__(self):
                box.Box.__init__(self)
                self.speed = 5
                self.name = 'Player'
         #def draw(self)
        def update(self):
                if pygame.key.get_pressed()[K_UP]: self.y -= self.speed
		if pygame.key.get_pressed()[K_DOWN]: self.y += self.speed
		if pygame.key.get_pressed()[K_LEFT]: self.x -= self.speed
		if pygame.key.get_pressed()[K_RIGHT]: self.x += self.speed

class Target(box.Box):
        def __init__(self):
                box.Box.__init__(self,pos=(100,100),boxcolor=THECOLORS['red'])
        def collision(self,obj):
                if obj.name == 'Player':
                        print 'collide'
                        self.manager.destroy(self)
def main():
        world = manager.World()
        Player()
        Target()
        world.run()
        
if __name__=="__main__":
	main()


