import pygame
import random

pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load("./media/spaceship.png")
playerX = 370 
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("./media/ufo.png")
enemyX = random.randint(0, 800) #start the enemy in a new position every time
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

	# Game Events
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT:
				playerX_change = -3 

			if event.key == pygame.K_RIGHT:
				playerX_change = 3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0 

	# Screen Attributes
	screen.fill((0, 0, 0))

	playerX += playerX_change
	
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	enemyX += enemyX_change #handle enemy movement
	
	if enemyX <= 0: #check for enemy boundaries on left side
		enemyX_change = 2
		enemyY += enemyY_change
	elif enemyX >= 736: #check for enemy boundaries on right side
		enemyX_change = -2
		enemyY += enemyY_change

	player(playerX, playerY)
	enemy(enemyX, enemyY) #assign the new enemy position

	pygame.display.update()