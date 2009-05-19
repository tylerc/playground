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

class MyBoxes(gameobject.GameObject):
	def __init__(self):
		gameobject.GameObject.__init__(self)
		self.manager.add_noter(self)
		self.connect = False
		
	def find_dir(self,x,pos):
		pass
	
	def mouse_up(self,pos):
		x = box.Box(size=(20,20),pos=pos)
		for j in self.manager.objs:
			if pos[1] < j.y:
				continue
			if pos[1] > j.y + j.height:
				continue
			if pos[0] < j.x:
				continue
			if pos[0] > j.x + j.width:
				continue
			x.status = 0
				
	def notify(self,key):
		if key == K_RETURN:
			if self.connect == True:
				self.connect = False
			else:
				self.connect = True
			print self.connect
		

def main():
	world = manager.World()
	MyBoxes()
	world.run()

if __name__=="__main__":
	main()