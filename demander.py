# Demands - This generates the items which are demanded and at what price
import random

class demander:
	def __init__(self,calendar):
		print 'Demander initialised'
		self.calSystem = calendar # Handle on the calendar object

		# Items and their demand
		self.goods = ["cheese","brandy","gin","tobacco","tea","wool"]
		self.demands = [0,0,0,0,0,0]
		self.basePrice = [1.0,3.0,5.0,8.0,7.0,15.0]
		self.price = [1.0,3.0,5.0,8.0,7.0,15.0]

		# Demand system vars
		self.maxDemand = 100

	def update(self):
		product = random.randint(0,5)
		self.increaseDemand(product)
		self.updatePrice(product)

	def increaseDemand(self,product):
		if self.demands[product] is not self.maxDemand:
			self.demands[product] += 1
			print "Demand for",self.goods[product],"increased"
		self.printDemands()

	def updatePrice(self, product):
		print "Calculated price:",str((float(self.demands[product])/100)+1*self.basePrice[product]),"base price",self.basePrice[product],"demand",self.demands[product]
		# self.price[product] = (float(self.demands[product])/100)+1*self.basePrice[product]

	def printDemands(self):
		print "\nToday's demands are as follows:"
		for i in range(len(self.goods)):
			print str(self.goods[i]) + ": " + str(self.demands[i])

