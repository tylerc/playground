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

class TextInput(box.Box):
	def __init__(self):
		box.Box.__init__(self,size=(100,50))
		self.manager.add_noter(self)
		self.string = manager.MyFont(string="",status=100000,pos=(self.x,self.y),size=22)
	def notify(self,key):
		if key < 256 and key != K_RETURN: self.string.string += chr(key)
		if key == K_BACKSPACE:
			self.string.string = self.string.string[:-2]

def main():
	world = manager.World()
	TextInput()
	world.run()

if __name__=="__main__":
	main()