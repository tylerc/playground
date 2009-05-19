#/usr/bin/env python

# PyGame Constants
import pygame
from pygame.locals import *

import manager
import gameobject

class Pic(gameobject.GameObject):
	def __init__(self,image,pos=(0,0)):
		gameobject.GameObject.__init__(self,name="Pic")
		self.x = pos[0]
		self.y = pos[1]
		self.image = pygame.image.load(image)
	def draw(self):
		self.screen.blit(self.image, (self.x, self.y))

# Example Usage:
if __name__ == "__main__":
	world = manager.World()
	Pic("coolness.png")
	world.run()
