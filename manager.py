import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import gameobject

class Border:
	name = 'Border'

class World:
	def __init__(self):
		self.objs = []
		self.objs2 = []
		self.WINSIZE = 640,480
                pygame.init()
                self.screen = pygame.display.set_mode(self.WINSIZE,0,8)
                pygame.display.set_caption('Game!')

                self.screen.fill(THECOLORS["black"])
                self.clock = pygame.time.Clock()
                gameobject.GameObject.manager = self
                gameobject.GameObject.screen = self.screen

                self.font = pygame.font.Font(None, 72)
                self.custom_ev = []
	def add(self,obj):
		self.objs2 += [obj]
	def update(self):
                for i in self.objs2:
                        self.objs += [i]
                self.objs2 = []
                for i in self.objs:
                        if i.status <= 0:
                                self.destroy(i)

                # Update Objects
		for i in self.objs:
			i.update()

		for i in self.objs:
                        if i.x < 0 or i.x > self.WINSIZE[0] or i.y < 0 or i.y > self.WINSIZE[1]:
                                i.status = 0

                # Check for collisions
                for i in self.objs:
                        for j in self.objs:
                                if i.name == j.name:
                                        continue
                                if i.y + i.height < j.y:
                                        continue
                                if i.y > j.y + j.height:
                                        continue
                                if i.x + i.width < j.x:
                                        continue
                                if i.x > j.x + j.width:
                                        continue

                                #print "collision" + i.name + "," + j.name
                                i.collision(j)
                                j.collision(i)

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
                                for i in self.custom_ev:
                                        if e.key == i:
                                                pass
                                if( e.key == K_ESCAPE ):
                                    done = True
                                    break
                                if( e.key == K_f ):
                                    pygame.display.toggle_fullscreen()
                self.clock.tick(30)

            print "Exiting!"

class MyFont(gameobject.GameObject):
        def __init__(self,string="test",pos=None, status=10):
                gameobject.GameObject.__init__(self)
                self.text = self.manager.font.render(string, 1, THECOLORS['blue'], THECOLORS['black'])
                if pos == None:
                        self.textpos = self.text.get_rect(centerx=self.screen.get_width()/2)
                else:
                        self.textpos = pos
                self.status = status
        def draw(self):
                self.manager.screen.blit(self.text,self.textpos)
        def update(self):
                self.status -= 1
	
