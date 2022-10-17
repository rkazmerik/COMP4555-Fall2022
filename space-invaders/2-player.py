import pygame

pygame.init()

# Game Screen
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load("./media/spaceship.png") #load an image for the player
playerX = 370 #position the start point for the player
playerY = 480
playerX_change = 0

def player(x, y):
	screen.blit(playerImg, (x, y)) #draw the player on the screen

# Game Loop
running = True
while running:

	# Game Events
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN: #detect key press events
			if event.key == pygame.K_LEFT:
				playerX_change = -3 #move the player to the left

			if event.key == pygame.K_RIGHT:
				playerX_change = 3 #move the player to the right

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0 #stop the player in current position

	# Screen Attributes
	screen.fill((0, 0, 0))
 
	playerX += playerX_change
	
	if playerX <= 0: #create a right left side boundary for the player
		playerX = 0
	elif playerX >= 736: #create a right side boundary for the player
		playerX = 736

	player(playerX, playerY) #draw the player on the screen

	pygame.display.update()