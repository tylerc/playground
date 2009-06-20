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
		self.screen = pygame.display.set_mode(self.WINSIZE,HWSURFACE | DOUBLEBUF)
		pygame.display.set_caption('Game!')

		self.screen.fill(THECOLORS["black"])
		self.clock = pygame.time.Clock()
		gameobject.GameObject.manager = self
		gameobject.GameObject.screen = self.screen

		self.font = pygame.font.Font(None, 72)

		self.FPS = 30
		self.displace = 0
		self.top = Border("Top")
		self.bottom = Border("Bottom")
		self.right = Border("Right")
		self.left = Border("Left")
		self.note = []
	def add(self,obj):
		self.objs2 += [obj]
	def update(self):
		for i in self.objs2:
				self.objs += [i]
		self.objs2 = []
		for i in self.objs:
				if i.status <= 0:
						self.destroy(i)
		iters = 0
		for i in self.objs:
			iters += 1
			# update objects
			i.update()
			# check collsions with borders
			if i.x < 0:
				i.collision(self.left)
			if i.y < 0:
				i.collision(self.top)
			if i.x > self.WINSIZE[0]:
				i.collision(self.right)
			if i.y > self.WINSIZE[1]:
				i.collision(self.bottom)
			
			# check for colllsions with other objects
			for j in self.objs[iters:]:
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

				i.collision(j)
				j.collision(i)
		for i in self.objs:
			i.x += self.displace
		# update displacements (for side-scrolling)
		self.displace = 0
	def draw(self):
		self.screen.fill(THECOLORS['black'])
		for i in self.objs:
			i.draw()
	def destroy(self, obj):
		obj.destroy()
		self.kill(obj)
	def kill(self, obj):
		self.objs.remove(obj)
	def add_noter(self,obj):
		self.note += [obj]
	def run(self):
		done = False
		while not done:
			# Update Objects
			self.update()
						
			# Drawing:
			self.draw()
			
			# Drawing finished this iteration?  Update the screen
			pygame.display.flip()
			
			# Event Handling:
			events = pygame.event.get( )
			for e in events:
				# mouse up event
				if e.type == 6:
					for i in self.objs:
						i.mouse_up(e.pos)
				if( e.type == QUIT ):
					done = True
					break
				elif (e.type == KEYDOWN):
					for i in self.note:
						i.notify(e.key,"down")
					if( e.key == K_ESCAPE ):
						done = True
						break
					if( e.key == K_f ):
						print str(self.objs)
				elif (e.type == KEYUP):
					for i in self.note:
						i.notify(e.key,"up")
			self.clock.tick(self.FPS)

		print "Exiting!"

class MyFont(gameobject.GameObject):
	def __init__(self,string="test",pos=None, status=10, size=72):
		self.font = pygame.font.Font(None, size)
		gameobject.GameObject.__init__(self)
		self.text = self.font.render(string, 1, THECOLORS['blue'], THECOLORS['black'])
		if pos == None:
				self.textpos = self.text.get_rect(centerx=self.screen.get_width()/2)
		else:
				self.textpos = pos
		self.status = status
		self.string = string
	def draw(self):
		self.manager.screen.blit(self.text,self.textpos)
	def update(self):
		self.text = self.manager.font.render(self.string, 1, THECOLORS['blue'], THECOLORS['white'])
			
class Border(gameobject.GameObject):
	def __init__(self,dir):
		gameobject.GameObject.__init__(self)
		self.dir = dir
		self.name = "Border"
	
