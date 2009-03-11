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

class Player(box.Box):
        def __init__(self):
                box.Box.__init__(self)
                self.speed = 7
                self.name = 'Player'
                self.direc = ''
                self.bulvel = (0,0)
                self.otherpos = (0,0)
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
	#def draw(self)
        def update(self):
                if self.y < self.manager.WINSIZE[1] - self.height:
                        self.y += 5
                if pygame.key.get_pressed()[K_UP]:
                        self.y -= self.speed
                        self.up = 1
		if pygame.key.get_pressed()[K_DOWN] and self.y < self.manager.WINSIZE[1] - self.height:
                        self.y += self.speed
                        self.down = 1
		if pygame.key.get_pressed()[K_LEFT]:
                        self.x -= self.speed
                        self.left = 1
		if pygame.key.get_pressed()[K_RIGHT]:
                        self.x += self.speed
                        self.right = 1
                if pygame.key.get_pressed()[K_SPACE]:
                        for i in range(100):
                                Bullet(velocity=(random.random()*5-2.5,random.random()*5-2.5),pos=(100,100),color=THECOLORS['white'])
		if True:#pygame.key.get_pressed()[K_SPACE]: 
                        for i in range(10):
                                if self.up == 1:
                                        self.otherpos = (self.x+self.width/2,self.y+self.height)
                                        self.bulvel = (random.random()*4-2,random.random()*10+2)
                                        Bullet(velocity=self.bulvel,pos=self.otherpos,color=THECOLORS['white'])
                                if self.left == 1:
                                        self.otherpos = (self.x+self.width,self.y+self.height/2)
                                        self.bulvel = (random.random()*10+2,random.random()*4-2)
                                        Bullet(velocity=self.bulvel,pos=self.otherpos,color=THECOLORS['white'])
                                if self.right == 1:
                                        self.otherpos = (self.x,self.y+self.height/2)
                                        self.bulvel = (random.random()*-10-2,random.random()*-4+2)
                                        Bullet(velocity=self.bulvel,pos=self.otherpos,color=THECOLORS['white'])
                                if self.down == 1:
                                        self.otherpos = (self.x+self.width/2,self.y)
                                        self.bulvel = (random.random()*-4+2,random.random()*-10-2)
                                        Bullet(velocity=self.bulvel,pos=self.otherpos,color=THECOLORS['white'])
                                if False:
                                        Bullet(velocity=self.bulvel,pos=self.otherpos,color=THECOLORS['white'])
                self.up = 0
                self.down = 0
                self.left = 0
                self.right = 0
#class Target(box.Box):
#        def __init__(self):
#                box.Box.__init__(self,pos=(100,100),boxcolor=THECOLORS['red'])
#        def collision(self,obj):
#                if obj.name == 'bullet':
#                        self.manager.destroy(self)
class Bullet(box.Box):
	numOf = 0
	def __init__(self,pos=(50,50),velocity=(5,0),color=THECOLORS['cyan'],home=1,life=75,size=(5,5)):
		box.Box.__init__(self,pos=pos,size=size,boxcolor=color)
		self.speed = 10
		self.name = 'Bullet'
		self.velocity = velocity
		Bullet.numOf += 1
		self.home = home
		self.status = life
	def update(self):
                self.status-=10
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		if self.status <= 0:
                        self.manager.destroy(self)
                if self.home==3 and random.random()*10 >=9:
                        #Bullet(velocity=(random.random()*10+2,random.random()*6-3),pos=(self.x,self.y),color=THECOLORS['gray'],home=4)
                        Bullet(velocity=self.velocity,pos=(self.x,self.y),color=THECOLORS['gray'],home=4)
                if self.home==2 and random.random()*10 >=9:
                        #Bullet(velocity=(random.random()*10+2,random.random()*6-3),pos=(self.x,self.y),color=THECOLORS['blue'],home=3)
                        Bullet(velocity=self.velocity,pos=(self.x,self.y),color=THECOLORS['blue'],home=3)
                if self.home==1 and random.random()*10 >=9:
                        Bullet(velocity=self.velocity,pos=(self.x,self.y),color=THECOLORS['cyan'],home=2)
                        #Bullet(velocity=(random.random()*10+2,random.random()*6-3),pos=(self.x,self.y),color=THECOLORS['cyan'],home=2)
	def destroy(self):
		Bullet.numOf -= 1
	def collision(self,obj):
		if obj.name == 'Border':
			self.manager.destroy(self)
def main():
        world = manager.World()
        Player()
        #Target()
        world.run()
        
if __name__=="__main__":
	main()


