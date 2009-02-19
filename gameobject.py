class GameObject():
	def __init__(self, x=0, y=0, width=1, height=1, name='GameObject'):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.status = 1
		self.name = name
	def draw(self):
		pass
	def update(self):
		#GameObject.manager.destroy(self)
		pass
