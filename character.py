
class character:
	def __init__(self, firstName, lastName, profession, home):
		self.firstName = firstName
		self.lastName = lastName
		self.profession = profession
		self.home = home
		self.currentLocation = self.home

	def setSprite(self, loadedImage):
		self.sprite = loadedImage
		self.spriteRect = self.sprite.get_rect()

	def update():
		print "Updating character"

	def getFullName(self):
		return self.firstName, self.lastName

	def getProfession(self):
		return self.profession

	def getHome(self):
		return self.home

	def getCurrentLocation(self):
		return self.currentLocation

	def getDetails(self):
		return (self.firstName, self.lastName, self.profession, self.home)