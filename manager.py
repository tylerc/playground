import gameobject

class ObjectManager:
	def __init__(self):
		self.objs = []
		gameobject.GameObject.manager = self
	def add(self,obj):
		self.objs += [obj]
	def update(self):
		for i in self.objs:
			i.update()
		for i in self.objs:
			for j in self.objs:
				if i == j:
					break
				if (i.y + i.height) < (j.y):
					break
				if (i.y) > (j.y + j.height):
					break
				if (i.x + i.width) < (j.x):
					break
				if (i.x) > (j.x + j.width):
					break
				print 'Collision between ' + i.name + ' ' + j.name
	def draw(self):
		for i in self.objs:
			i.draw()
	def destroy(self, obj):
		pass
	def kill(self, obj):
		pass
