import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import gameobject

class Border:
	name = 'Border'

class World:
	def __init__(self):
		self.objs = []
		self.WINSIZE = 640,480
                pygame.init()
                self.screen = pygame.display.set_mode(self.WINSIZE,0,8)
                pygame.display.set_caption('Game!')

                self.screen.fill(THECOLORS["black"])
                self.clock = pygame.time.Clock()
                gameobject.GameObject.manager = self
                gameobject.GameObject.screen = self.screen
	def add(self,obj):
		self.objs += [obj]
	def update(self):
                for i in self.objs:
                        if i.status == 0:
                                self.destroy(i)

                # Update Objects
		for i in self.objs:
			i.update()

		for i in self.objs:
                        if i.x < 0 or i.x > self.WINSIZE[0] or i.y < 0 or i.y > self.WINSIZE[1]:
                                i.status = 0

	def draw(self):
		self.screen.fill(THECOLORS['black'])
		for i in self.objs:
			i.draw()
	def destroy(self, obj):
		obj.destroy()
		self.kill(obj)
	def kill(self, obj):
		self.objs.remove(obj)
	def run(self):
            done = False
            while not done:
                # Update Objects
                self.update()
                            
                # Drawing:
                self.draw()
                            
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
                self.clock.tick(30)

            print "Exiting!"
