objs = []
def add(obj):
	objs += obj
def update():
	for i in objs.iterate():
		try:
			objs.update()
		except AttributeError:
			pass
def draw():
	for i in objs.iterate():
		try:
			objs.draw()
		except AttributeError:
			pass
