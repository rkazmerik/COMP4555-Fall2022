import pygame
import random

pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Space Invaders")

# Background
background = pygame.image.load("./media/stars.png")

# Player
playerImg = pygame.image.load("./media/spaceship.png")
playerX = 370 
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("./media/ufo.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load("./media/bullet.png") #load and image for the bullet
bulletX = 0 #set the bullet start position and motion
bulletY = 480 #place the bullet behind the spaceship to start
bulletX_change = 0 #set the speed for horizontal movement
bulletY_change = 10 #set the speed for vertical movement
bullet_state = "ready" #create a state for the bullet

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
	global bullet_state

	bullet_state = "fire"
	screen.blit(bulletImg, (x+16, y+10)) #draw the bullet on the center of the spaceship

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
			
			if event.key == pygame.K_SPACE:
				if bullet_state is "ready": #fire only one bullet at a time
					bulletX = playerX
					fire_bullet(bulletX, bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0 

	# Screen Attributes
	screen.fill((0, 0, 0))
	screen.blit(background, (0, 0))

	playerX += playerX_change
	
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	enemyX += enemyX_change
	
	if enemyX <= 0:
		enemyX_change = 2
		enemyY += enemyY_change
	elif enemyX >= 736:
		enemyX_change = -2
		enemyY += enemyY_change

	#Bullet Animation
	if bulletY <= 0: #detect if the bullet is off the screen
		bulletY = 480 #reposition the bullet
		bullet_state = "ready" #set the state to ready to fire

	if bullet_state is "fire": #fire a bullet on change
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change #move the bullet on the screen

	player(playerX, playerY)
	enemy(enemyX, enemyY)

	pygame.display.update()