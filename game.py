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

def main():
	WINSIZE = 640,480
	pygame.init()
	screen = pygame.display.set_mode(WINSIZE,0,8)
	pygame.display.set_caption('Game!')

	screen.fill(THECOLORS["black"])
	
	manage = manager.ObjectManager()
	manage.add(box.Box(screen))
	
	clock = pygame.time.Clock()
	# The Main Event Loop
	done = False
	while not done:
		# Update Objects
		manage.update()
		
		# Drawing:
		manage.draw()
		
		# Drawing finished this iteration?  Update the screen
		pygame.display.update()

		# Event Handling:
		events = pygame.event.get( )
		for e in events:
			if( e.type == QUIT ):
				done = True
				break
			elif (e.type == KEYDOWN):
				if( e.key == K_ESCAPE ):
					done = True
					break
				if( e.key == K_f ):
					pygame.display.toggle_fullscreen()
			clock.tick(30)

	print "Exiting!"

	return
if __name__=="__main__":
	main()

