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
	def __init__(self, up=K_UP, down=K_DOWN, pos=(20,20)):
		box.Box.__init__(self,size=(20,80),pos=pos)
		self.up = up
		self.down = down
		self.speed = 10
		self.name = "Player"
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[self.up]:
			self.y -= self.speed
		if keys[self.down]:
			self.y += self.speed

class Ball(box.Box):
	def __init__(self):
		box.Box.__init__(self,size=(10,10),pos=(self.manager.WINSIZE[0]/2,self.manager.WINSIZE[1]/2))
		self.xvel = 10
		self.yvel = 0
		self.speed = 10
		self.name = "Ball"
		self.lscore = 0
		self.rscore = 0
	def update(self):
		self.x += self.xvel
		self.y += self.yvel
		manager.MyFont(string=str(self.lscore),status=100,pos = (100,100))
		manager.MyFont(string=str(self.rscore),status=100,pos = (400,100))
	def collision(self,obj):
		if obj.name == "Player":
			self.xvel *= -1 ; self.yvel *= -1
			if self.x < 100:
				self.x = obj.x+obj.width+1
			if self.x > 100:
				self.x = obj.x-self.width-1
			if self.xvel < self.speed:
				self.xvel += 5
		if obj.name == "Border":
			if obj.dir == "Left" or obj.dir == "Right":
				if obj.dir == "Left":
					self.rscore += 1
				if obj.dir == "Right":
					self.lscore += 1
				self.x = self.manager.WINSIZE[0]/2
				self.y = self.manager.WINSIZE[1]/2
				self.xvel = random.random() * 20 - 10; self.yvel = random.random() * 20 - 10
			if obj.dir == "Top" or obj.dir == "Bottom":
				self.yvel *= -1
def main():
	world = manager.World()
	Player()
	Player(up=K_w, down=K_s, pos=(world.WINSIZE[0]-40,20))
	Ball()
	world.run()
        
if __name__=="__main__":
	main()