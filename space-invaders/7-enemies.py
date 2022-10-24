import pygame
import math
import random
import psutil


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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6 #define how many enemies

for i in range(num_enemies): #loop to create 6 enemies
	enemyImg.append(pygame.image.load("./media/ufo.png"))
	enemyX.append(random.randint(0, 735))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(2)
	enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load("./media/bullet.png") 
bulletX = 0 
bulletY = 480 
bulletX_change = 0 
bulletY_change = 10 
bullet_state = "ready" 

score = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, i): #modify for list of enemies
	screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
	global bullet_state

	bullet_state = "fire"
	screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):

	distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))

	if distance < 27:
		return True
	else:
		return False

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
				if bullet_state is "ready":
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

	# Enemy Movement
	for i in range(num_enemies): #move every enemy in the list
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyX_change[i] = 2
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] = -2
			enemyY[i] += enemyY_change[i]

		#detect a collision with each enemy
		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY) 
		if collision:
			bulletY = 480
			bullet_state = "ready"
			score += 1
			enemyX[i] = random.randint(0, 800) 
			enemyY[i] = random.randint(50, 150) 

			print(f"{score}")
			print('RAM memory % used:', psutil.virtual_memory()[2])
			print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
		
		enemy(enemyX[i], enemyY[i], i) #animate each enemy

	#Bullet Animation
	if bulletY <= 0:
		bulletY = 480 
		bullet_state = "ready"
		
	if bullet_state is "fire": 
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change 
		
	player(playerX, playerY)

	pygame.display.update()