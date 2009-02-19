class ObjectManager:
	def __init__(self):
		self.objs = []
	def add(self, obj):
		self.objs += [obj]
	def update(self):
		for i in self.objs:
			i.update()
	def draw(self):
		for i in self.objs:
			i.draw()
