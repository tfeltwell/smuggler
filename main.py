import pygame, sys
from pygame.locals import *
import daySystem, demander, player, good

if __name__ == "__main__":

	# Pygame variables
	pygame.init()
	WIDTH = 800
	HEIGHT = 600
	DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Sussex Smuggler")
	backgroundColor = 212,203,188
	fontBlk = 45,46,40
	splash = pygame.image.load("splash.jpg")
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
	f = open("goods.txt",'r')
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

	# Generate initial characters

	#TODO: Load everything from text files to create characters


	# for i in range(5):
	# 	goodsList.append(good.good(str(i),10))
	# # print names for debugging


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
			DISPLAYSURF.blit(title,((WIDTH//2)-title.get_width()//2,0))
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
			pygame.display.update()
			calendar.update()
			player.update()

			frameCount = 0
		else:
			frameCount += 1
		clock.tick(60)