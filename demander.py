# Demands - This generates the items which are demanded and at what price
import random

class demander:
	def __init__(self,calendar):
		print 'Demander initialised'
		self.calSystem = calendar # Handle on the calendar object

		# Items and their demand
		self.cheese = 0
		self.brandy = 0
		self.gin = 0
		self.tobacco = 0
		self.tea = 0
		self.wool = 0

	def update(self):
		product = random.randint(0,6)
		print "product",product
		self.calSystem.printDate()
		# increaseDemand(product)

	def increaseDemand(self,product):
		if product == 0:
			print "Demand for cheese increased"
		elif product == 1:
			print "Demand for brandy increased"
		elif product == 2:
			print "Demand for gin increased"
		elif product == 3:
			print "Demand for tobacco increased"
		elif product == 4:
			print "Demand for tea increased"
		elif product == 5:
			print "Demand for wool increased"

