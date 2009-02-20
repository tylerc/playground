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
                self.name = 'Player'	#def draw(self)
	def update(self):
                if pygame.key.get_pressed()[K_UP]: self.y -= self.speed
		if pygame.key.get_pressed()[K_DOWN]: self.y += self.speed
		if pygame.key.get_pressed()[K_LEFT]: self.x -= self.speed
		if pygame.key.get_pressed()[K_RIGHT]: self.x += self.speed
		if pygame.key.get_pressed()[K_SPACE]: 
			if Bullet.numOf < 1:
				Bullet(pos=(self.x+self.width,self.y+self.height/2))

class Target(box.Box):
        def __init__(self):
                box.Box.__init__(self,pos=(100,100),boxcolor=THECOLORS['red'])
        def collision(self,obj):
                if obj.name == 'Player':
                        self.manager.destroy(self)

class Bullet(box.Box):
	numOf = 0
	def __init__(self,pos=(50,50),velocity=(5,0),color=THECOLORS['blue']):
		box.Box.__init__(self,pos=pos,size=(5,5),boxcolor=color)
		self.speed = 10
		self.name = 'Bullet'
		self.velocity = velocity
		Bullet.numOf += 1
		
	def update(self):
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		
	def destroy(self):
		Bullet.numOf -= 1
		
	def collision(self,obj):
		if obj.name == 'Border':
			self.manager.destroy(self)

def main():
        world = manager.World()
        Player()
        Target()
        world.run()
        
if __name__=="__main__":
	main()


