
class settlement:
	def __init__(self,name,x,y):
		self.name = name
		self.x = int(x)
		self.y = int(y)

	def update(self):
		print 'Updating'

	def getDetails(self):
		return self.name, self.x, self.y

	def getName(self):
		return self.name

	def getX(self):
		return int(self.x)

	def getY(self):
		return int(self.y)