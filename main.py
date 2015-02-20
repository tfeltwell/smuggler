import pygame, sys, random
from pygame.locals import *
import daySystem, demander, player, good, character, settlement

if __name__ == "__main__":

	# Pygame variables
	pygame.init()
	WIDTH = 800
	HEIGHT = 600
	DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Sussex Smuggler")
	backgroundColor = 212,203,188
	fontBlk = 45,46,40
	splash = pygame.image.load("assets/splash.jpg")
	splashrect = splash.get_rect()
	DISPLAYSURF.blit(splash,splashrect)
	background = pygame.image.load("assets/map.png")
	backgroundrect = splash.get_rect()
	pygame.display.update()

	# Game system variables
	calendar = daySystem.daySystem()
	# demand = demander.demander(calendar)
	player = player.player()
	frameCount = 0
	clock = pygame.time.Clock()
	# Generate goods
	goodSpriteLocation = 'assets/goods/'
	goodsList = []
	characterList = []

	#Generate places
	print 'places'
	f = open("assets/proc/places.txt")
	settlementList = []
	for i in f:
		parts = i.strip('\n').split(',')
		if len(parts) is 3:
			settlementList.append(settlement.settlement(parts[0],parts[1],parts[2]))
			print settlementList[-1].getDetails() 

	f = open("assets/proc/goods.txt",'r')
	for i in f:
		parsed = i.strip('\n').split(',')
		if len(parsed) is 3:
			goodsList.append(good.good(parsed[0],parsed[1],parsed[2]))
		else:
			print 'Invalid input',i
	print 'Goods:'
	for i in goodsList:
		i.setSprite(pygame.image.load(goodSpriteLocation+i.name+'.png'))
		print i.name,'at',i.basePrice
	f.close()

	# Generate initial characters
	f = open("assets/proc/firstnames.txt",'r')
	firstNames = []
	for i in f:
		firstNames.append(i.strip('\n'))
	f.close()
	f = open("assets/proc/lastnames.txt",'r')
	lastNames = []
	for i in f:
		lastNames.append(i.strip('\n'))
	f.close()
	f = open("assets/proc/profession.txt",'r')
	professionList = []
	for i in f:
		professionList.append(i.strip('\n'))
	f.close()

	for i in range(10): #Create 10 characters
		first = firstNames[random.randint(0,len(firstNames)-1)]
		last = lastNames[random.randint(0,len(lastNames)-1)]
		profession = professionList[random.randint(0,len(professionList)-1)]
		home = settlementList[random.randint(0,len(settlementList)-1)].getName()
		characterList.append(character.character(first,last,profession,home))
		characterList[-1].setSprite(pygame.image.load("assets/character.png"))
		print characterList[-1].getDetails()

	titleFont = pygame.font.SysFont(None, 72)
	textFont = pygame.font.SysFont(None,30)
	title = titleFont.render("Sussex Smuggler", True, (45, 46, 40))

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		if frameCount >= 100: #Integrate this with the pygame clock
			# Rendering
			# Background stuff
			DISPLAYSURF.fill(backgroundColor)
			DISPLAYSURF.blit(background,(0,0))
			# DISPLAYSURF.blit(title,((WIDTH//2)-title.get_width()//2,0))
			# Text overlays
			demandsStr = ""
			# for i in range(len(demand.goods)):
			# 	demandsStr += str(demand.goods[i])+": "+str(demand.price[i])+" | "
			demands = textFont.render(demandsStr, True, (fontBlk))
			dateUI = textFont.render(calendar.getDate(), True, (fontBlk))
			capital = textFont.render(("Capital: "+str(player.capital)), True, (fontBlk))
			DISPLAYSURF.blit(demands,(0+20,HEIGHT//2))
			DISPLAYSURF.blit(dateUI,(0,(HEIGHT-dateUI.get_height())))
			DISPLAYSURF.blit(capital,((WIDTH-capital.get_width()-20),(HEIGHT-capital.get_height())))
			# DISPLAYSURF.blit(dateUI,(((WIDTH//2)-dateUI.get_width()//2,((HEIGHT/)-dateUI.get_height()//2))
			# Objects
			for count, i in enumerate(goodsList):
				DISPLAYSURF.blit(i.sprite,(((70*count)+100),490))

			# This needs sorting as it's quite inefficient
			for count, i in enumerate(characterList):
				for j in settlementList:
					if j.getName() is characterList[count].getCurrentLocation():
						print j.getX(), j.getY()
						DISPLAYSURF.blit(i.sprite,(j.getX(),j.getY()))
			pygame.display.update()
			calendar.update()
			player.update()

			frameCount = 0
		else:
			frameCount += 1
		clock.tick(60)