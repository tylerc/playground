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
			self.x = 300
			self.y = 480-self.height
			self.width = 10
			self.height = 40
			self.vel = 0
			self.up = False
			self.jumpstart = self.y
	def update(self):
		keys = pygame.key.get_pressed()

		if keys[K_n]:
			for i in range(10):
				Target(pos=(random.random()*600,random.random()*400))
		if keys[K_LEFT]:
			self.manager.displace += self.speed
		if keys[K_RIGHT]:
			self.manager.displace -= self.speed
		if keys[K_UP]:
			if self.up == False:
				self.up = True
				self.vel = 20
		if keys[K_t]:
			for i in self.manager.objs:
				if i.name == "Platform":
					i.status = 0
					break
		
		self.y -= self.vel
		self.vel -= 1
		if self.y > 480-self.height and self.vel < 0:
			self.vel = 0
			self.y = 480-self.height
			self.up = False
		self.x -= self.manager.displace
	def destroy(self):
		manager.MyFont(string="PWNED",status=100)
	def collision(self,obj):
		if obj.name == "Platform":
			if self.vel < 0 and obj.y >= self.y+self.height+self.vel:
				self.y = obj.y-self.height
				self.vel = 0
				obj.status -= 10
				self.up = False
			if self.vel > 0 and obj.y+obj.height >= self.y:
				self.y = obj.y+obj.height
				obj.status -= 50
				self.vel = 0
		if obj.name == "Border":
			if obj.dir == "Right":
				self.status = 0
		if obj.name == "Flag":
			manager.MyFont("Sorry Mario",(50,50),status= 10000)
			manager.MyFont("The Princess Is In", (50,100), status = 10000)
			manager.MyFont("Another Castle", (50, 150), status = 10000)
			self.manager.objs = []
class Platform(box.Box):
	def __init__(self,pos=(100,100),size=(30,30)):
		box.Box.__init__(self,pos=pos,boxcolor=(255,0,0),size=size)
		self.name = "Platform"
		self.status = 10
	def collision(self,obj):
		if obj.name == "Bullet":
				self.status = 0
	def update(self):
		self.boxcolor=(255-self.status,self.status,self.status)
	def destroy(self):
		#for x in range(5):
			for i in range(6):
				for j in range(6):
					Bit(pos=(self.x+5*j,self.y+5*i),vel=[i+5,j+3])

class Bit(box.Box):
	numOf = 0
	def __init__(self,pos=(5,5),vel=[1,1]):
		box.Box.__init__(self,size=(5,5),pos=pos)
		self.vel = vel
		Bit.numOf += 1
	def update(self):
		self.y += self.vel[0]
		self.x += self.vel[1]
		self.vel[0] -= random.random() * 2.0 - 1
		self.vel[1] -= 0.1
	def collision(self,obj):
		if obj.name == "Border":
			self.status = 0
	def destroy(self):
		Bit.numOf -= 1
		if Bit.numOf == 0:
			for i in range(20):
				for j in range(15):
					Bit(pos=(500+5*j,300+5*i),vel=[-j,-i])
		
class Flag(box.Box):
	def __init__(self):
		box.Box.__init__(self,pos=(400,400))
		self.name = "Flag"
def main():
	world = manager.World()
	#for i in [[50,400],[80,400],[110,400],[140,400]]:
	for i in range(200):
		Platform(pos=(2,400),size=(2,2))
	#Platform(pos = (50,400))
	#for i in range(15):
	#	for j in range(15):
	#		Bit(pos=(500+5*j,300+5*i),vel=[-i,-j])
		
	Player()
	#Flag()
	world.FPS = 30
	world.run()
        
if __name__=="__main__":
	main()


