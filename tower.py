[Notepad++PortableSettings]
LastDriveLetter=E:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               5
		self.up = False
		self.down = False
		self.left = False
		self.right = False
		self.status = 100
		self.name = "Player"
	def notify(self,key,what):
		if key == pygame.K_UP:
			if what == "down":
				self.up = True
			else:
				self.up = False
		if key == pygame.K_DOWN:
			if what == "down":
				self.down = True
			else:
				self.down = False
		if key == pygame.K_RIGHT:
			if what == "down":
				self.right = True
			else:
				self.right = False
		if key == pygame.K_LEFT:
			if what == "down":
				self.left = True
			else:
				self.left = False
	def update(self):
		if self.up:
			self.y -= self.speed
		if self.down:
			self.y += self.speed
		if self.right:
			self.x += self.speed
		if self.left:
			self.x -= self.speed
	def collision(self,obj):
		pass
class Bar(box.Box):
	def __init__(self,pos=(0,0),size=100,value=100):
		pass#box.Box.__init__(self,pos=pos,size
		if obj.name == "Enemy":
			self.status -= 1
def main():
	world = manager.World()
	Enemy()
	Player()
	world.run()

if __name__=="__main__":
	main()