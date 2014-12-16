import daySystem, demander

if __name__ == "__main__":
	calendar = daySystem.daySystem()
	demand = demander.demander(calendar)
	print 'Started'

	while calendar.year != 1650:
			calendar.update()
			demand.update()
			raw_input() # This is just to manually step through the day
			print "-----"