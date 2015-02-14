# Demands - This generates the items which are demanded and at what price
import random

class demander:
	def __init__(self,calendar):
		print 'Demander initialised'
		self.calSystem = calendar # Handle on the calendar object

		# Currently does nothing...

		# Demand system vars
		self.maxDemand = 100

	def update(self):
		# Roll for a chance to increase demand
		modDemand = random.randint(0,100)
		if modDemand > 75:
			product = random.randint(0,5)
			self.increaseDemand(product)
			self.updatePrice(product)

	def increaseDemand(self,product):
		if self.demands[product] is not self.maxDemand:
			self.demands[product] += 1
			print "Demand for",self.goods[product],"increased"

	def updatePrice(self, product):
		self.price[product] = float(self.basePrice[product]*((float(self.demands[product])/100)+1))
		print self.goods[product],"changed price to",str(self.price[product])

	def printDemands(self):
		print "\nToday's demands are as follows:"
		for i in range(len(self.goods)):
			print str(self.goods[i]) + ": " + str(self.demands[i])

