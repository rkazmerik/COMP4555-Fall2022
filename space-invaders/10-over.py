import pygame
import math
import random

pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Background
background = pygame.image.load("./media/stars.png")

# Sound
pygame.mixer.music.load("./media/background.wav")
pygame.mixer.music.play(-1) 

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
num_enemies = 6

for i in range(num_enemies):
	enemyImg.append(pygame.image.load("./media/ufo.png"))
	enemyX.append(random.randint(0, 735))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(4)
	enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("./media/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score Board
score_value = 0
font = pygame.font.Font("./fonts/Square.ttf", 24)
textX = 10
textY = 10

# Game Over Text
game_over_font = pygame.font.Font("./fonts/Square.ttf", 128) #create the font for game over

def show_score(x, y):
	score = font.render("Score: "+str(score_value), True, (255, 255, 255))
	screen.blit(score, (x, y))


def player(x, y):
	screen.blit(playerImg, (x, y))


def enemy(x, y, i):
	screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
	global bullet_state

	bullet_state = "fire"
	screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):

	distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
											 math.pow(enemyY-bulletY, 2))

	if distance < 27:
		return True
	else:
		return False

def game_over(): # display the game over text
	over_font = game_over_font.render("GAME OVER", True, (255, 255, 255))
	screen.blit(over_font, (100, 250))

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
					bullet_sound = pygame.mixer.Sound("./media/laser.wav")
					bullet_sound.play()
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
	for i in range(num_enemies):

		#Game Over
		if enemyY[i] > 440: #trigger the end of the game
			for j in range(num_enemies):
				enemyY[j] = 2000
			game_over()
			break 
		
		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyX_change[i] = 4
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] = -4
			enemyY[i] += enemyY_change[i]

		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY) 
		if collision:
			explosion_sound = pygame.mixer.Sound("./media/explosion.wav")
			explosion_sound.play()
			bulletY = 480
			bullet_state = "ready"
			score_value += 1
			enemyX[i] = random.randint(0, 800) 
			enemyY[i] = random.randint(50, 150) 

		enemy(enemyX[i], enemyY[i], i)

	# Bullet Animation
	if bulletY <= 0:
		bulletY = 480 
		bullet_state = "ready" 

	if bullet_state is "fire": 
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change 

	player(playerX, playerY)
	show_score(textX, textY)

	pygame.display.update()