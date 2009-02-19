class ObjectManager:
	def __init__(self):
		self.objs = []
	def add(self, obj):
		self.objs += [obj]
	def update(self):
		for i in self.objs:
			try:
				i.update()
			except AttributeError:
				pass
	def draw(self):
		for i in self.objs:
			try:
				i.draw()
			except AttributeError:
				pass
