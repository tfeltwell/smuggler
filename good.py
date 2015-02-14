
class good:
	def __init__(self, name, basePrice,scarcity):
		self.name = name
		self.basePrice = basePrice
		self.currentPrice = basePrice
		self.scarcity = scarcity # How rare/valuable a commodity is

	def setSprite(self, loadedImage):
		self.sprite = loadedImage
		self.spriteRect = self.sprite.get_rect()

	def update(self):
		# update current price here
		print 'Running update'

	def getName(self):
		return self.name

	def getBasePrice(self):
		return self.basePrice

	def getCurrentPrice(self):
		return self.currentPrice
