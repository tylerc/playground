class GameObject():
	def __init__(self, x=0, y=0, width=1, height=1, name='GameObject', status=1):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.status = status
		self.name = name
		self.manager.add(self)
	def draw(self):
		pass
	def update(self):
		#GameObject.manager.destroy(self)
		pass
	def destroy(self):
		pass
	def collision(self,obj):
		pass
	def notify(self,key,what):
		pass
	def mouse_up(self,pos):
		pass
