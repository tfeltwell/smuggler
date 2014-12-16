import pygame, sys
from pygame.locals import *
import daySystem, demander

if __name__ == "__main__":
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Sussex Smuggler")
	splash = pygame.image.load("splash.jpg")
	splashrect = splash.get_rect()

	calendar = daySystem.daySystem()
	demand = demander.demander(calendar)
	print 'Started'
	frameCount = 0

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if frameCount >= 1000000:
			DISPLAYSURF.blit(splash,splashrect)
			pygame.display.update()
			calendar.update()
			demand.update()
			frameCount = 0
		else:
			frameCount += 1