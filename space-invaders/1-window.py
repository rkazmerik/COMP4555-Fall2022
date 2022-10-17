import pygame

pygame.init() #initialize pygame

# Game Screen
screen = pygame.display.set_mode((800, 600)) #create the screen with a tuple
pygame.display.set_caption("Space Invaders") #set the window title

# Game Loop
running = True
while running: #create the main game loop

  # Game Events
  for event in pygame.event.get(): #loop through the game events
    if event.type == pygame.QUIT: #listen for the quit event
      running = False #end the game loop

  # Screen Attributes
  screen.fill((0, 0, 0)) #colour the game screen
  pygame.display.update()