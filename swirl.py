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
		self.angle = 0
		self.tl, self.tm, self.tr, self.ml, self.mm, self.mr, self.bl, self.bm, self.br = True, True, True, True, True, True, True, True, True
		self.text = manager.MyFont(str(Bullet.startStat))
	def update(self):
		self.text.string = str(Bullet.startStat)
		# top left
		if self.tl:
			Bullet(angle=self.angle,pos=(100,100),color=THECOLORS['cyan'])
		# top middle
		if self.tm:
			Bullet(angle=self.angle,pos=(320,100),color=THECOLORS['pink'])
		# top right
		if self.tr:
			Bullet(angle=self.angle,pos=(540,100),color=THECOLORS['purple'])
		# middle left
		if self.ml:
			Bullet(angle=self.angle,pos=(100,240),color=THECOLORS['red'])
		# middle middle
		if self.mm:
			Bullet(angle=self.angle,pos=(320,240),color=THECOLORS['blue'])
		# middle right
		if self.mr:
			Bullet(angle=self.angle,pos=(540,240),color=THECOLORS['yellow'])
		# bottom left
		if self.bl:
			Bullet(angle=self.angle,pos=(100,380),color=THECOLORS['brown'])
		# bottom middle
		if self.bm:
			Bullet(angle=self.angle,pos=(320,380),color=THECOLORS['green'])
		# bottom right
		if self.br:
			Bullet(angle=self.angle,pos=(540,380),color=THECOLORS['white'])
		self.angle += 10
		if self.angle > 360:
			self.angle = 0
		keys = pygame.key.get_pressed()
		if keys[K_n]:
			for i in range(10):
				Target(pos=(random.random()*600,random.random()*400))
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
		if keys[K_r]:
			for i in self.manager.objs:
			    if i.name == "Bullet":
				i.status = 0
		if keys[K_w]:
			Bullet.startStat += 1
		if keys[K_s]:
			Bullet.startStat -= 1
		if keys[K_1]:
			self.tl = False
		if keys[K_2]:
			self.tm = False
		if keys[K_3]:
			self.tr = False
		if keys[K_4]:
			self.ml = False
		if keys[K_5]:
			self.mm = False
		if keys[K_6]:
			self.mr = False
		if keys[K_7]:
			self.bl = False
		if keys[K_8]:
			self.bm = False
		if keys[K_9]:
			self.br = False
		#-------------------------------
		if keys[K_LSHIFT] and keys[K_1]:
			self.tl = True
		if keys[K_LSHIFT] and keys[K_2]:
			self.tm = True
		if keys[K_LSHIFT] and keys[K_3]:
			self.tr = True
		if keys[K_LSHIFT] and keys[K_4]:
			self.ml = True
		if keys[K_LSHIFT] and keys[K_5]:
			self.mm = True
		if keys[K_LSHIFT] and keys[K_6]:
			self.mr = True
		if keys[K_LSHIFT] and keys[K_7]:
			self.bl = True
		if keys[K_LSHIFT] and keys[K_8]:
			self.bm = True
		if keys[K_LSHIFT] and keys[K_9]:
			self.br = True
		for i in self.manager.objs:
		    if i.name == "Bullet":
		        i.status -= 1

class Bullet(box.Box):
        numOf = 0
        startStat = 10
        def __init__(self,size=(5,5),pos=(20,20),angle=0,color=THECOLORS['white']):
                box.Box.__init__(self,size=size,pos=pos,boxcolor=color)
                self.name = "Bullet"
                Bullet.numOf += 1
                self.speed = 5
                self.angle = angle
                self.status = Bullet.startStat
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
                box.Box.__init__(self,pos=pos,boxcolor=THECOLORS['red'])
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


