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
	def __init__(self,pos=(20,20)):
		box.Box.__init__(self,size=(20,80),pos=pos)
		self.speed = 10
		self.name = "Player"
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[K_DOWN]:
			self.y += self.speed
		if keys[K_UP]:
			self.y -= self.speed
		
class Ball(box.Box):
	def __init__(self):
		box.Box.__init__(self,boxcolor=THECOLORS['red'],size=(10,10),pos=(self.manager.WINSIZE[0]/2,self.manager.WINSIZE[1]/2))
		self.speed = 10
		self.angle = 180
		self.rev = 1
	def update(self):
		self.x += self.speed * math.cos(self.angle * (math.pi / 180))
		self.y += self.speed * math.sin(self.angle * (math.pi / 180)) * self.rev
	def collision(self,obj):
		if obj.name == "Player":
			# right player
			if self.x < obj.x:
				self.x = obj.x-self.width-1
				self.angle = 180+self.y-(obj.y + obj.height/2)*1.2
				print self.angle
			# left player
			if self.x > obj.x:
				self.x = obj.x+obj.width+1
				self.angle = self.y-(obj.y + obj.height/2)*1.2
		if obj.name == "Border":
			if obj.dir == "Bottom" or obj.dir == "Top":
				self.rev *= -1
	
def main():
	world = manager.World()
	Player()
	Player(pos=(world.WINSIZE[0]-40,20))
	Ball()
	world.run()
        
if __name__=="__main__":
	main()