import pygame
from pygame.locals import *

class Box:
	def __init__(self, screen, size, pos, background, boxcolor):
		self.screen = screen
		screensize = self.screen.get_size()
		self.screenwidth = screensize[0]
		self.screenheight = screensize[1]
		# Position of Box on the Screen
		# Box will start roughly in the middle of the screen.
		self.x = pos[0]
		self.y = pos[1]
		self.width = size[0]
		self.height = size[1]
		self.bgcolor = background
		self.boxcolor = boxcolor
		self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

	def draw(self):
		# Draw the new box
		self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect( self.screen, self.boxcolor, self.rect )
		
	def setBackgroundColor(self, color):
		self.bgcolor=color
		
	def setBoxColor(self, color):
		self.boxcolor=color
