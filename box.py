import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import gameobject

class Box(gameobject.GameObject):
	def __init__(self, size=(50,50), pos=(20,20), background=THECOLORS['black'], boxcolor=THECOLORS['white']):
		gameobject.GameObject.__init__(self,name='Box')
		screensize = self.screen.get_size()
		self.screenwidth = screensize[0]
		self.screenheight = screensize[1]
		# Position of Box on the Screen
		self.x = pos[0]
		self.y = pos[1]
		self.width = size[0]
		self.height = size[1]
		self.bgcolor = background
		self.boxcolor = boxcolor
		self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

	def draw(self):
		# Clear the old box
		# pygame.draw.rect(self.screen, self.bgcolor, self.rect)
		# Draw the new box
		self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect( self.screen, self.boxcolor, self.rect )
		
	def setBackgroundColor(self, color):
		self.bgcolor=color
		
	def setBoxColor(self, color):
		self.boxcolor=color

