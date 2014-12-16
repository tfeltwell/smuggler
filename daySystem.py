# Day calculator

class daySystem:
	def __init__(self):
		print "Day system init"
		self.day = 0
		self.month = 0
		self.year = 1600

		self.monthLength = 30

	def update(self):
		self.dayUp()
		self.printDate()

	def dayUp(self):
		if self.day > self.monthLength:
			self.monthUp()
		else:
			self.day += 1

	def monthUp(self):
		self.day = 1
		if self.month >= 12:
			self.yearUp()
		else:
			self.month += 1

	def yearUp(self):
		self.day = 1
		self.month = 1
		self.year += 1

	def printDate(self):
		print "Day:",self.day,"Month:",self.month,"Year",self.year 