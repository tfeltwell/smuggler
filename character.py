
class character:
	def __init__(self, firstName, lastName, profession, home):
		self.firstName = firstName
		self.lastName = lastName
		self.profession = profession
		self.home = home

	def update():
		print "Updating character"

	def getFullName(self):
		return self.firstName, self.lastName

	def getProfession(self):
		return self.profession

	def getHome(self):
		return self.home

	def getDetails(self):
		return (self.firstName, self.lastName, self.profession, self.home)