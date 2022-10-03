import pygame
import random
import sys


# FUNCTIONS

def ball_animation():

  global ball_speed_x, ball_speed_y, player_score, opponent_score

  ball.x += ball_speed_x
  ball.y += ball_speed_y

  # Ball Collision
  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1

  # Ball Collision Left
  if ball.left <= 0:
    player_score += 1
    ball_restart()

  # Ball CollisionRight
  if ball.right >= screen_width:
    opponent_score += 1
    ball_restart()


  # Ball Collision (Player)
  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1


def player_animation():

  global player_speed

  player.y += player_speed

  # Player Collision
  if player.top <= 0:
    player.top = 0

  if player.bottom >= screen_height:
    player.bottom = screen_height


def opponent_ai():
  
  global opponent_speed

  if opponent.top < ball.top : #opponent is above ball
    opponent.y += opponent_speed

  if opponent.bottom > ball.bottom: # opponent is below ball
    opponent.y -= opponent_speed

  if opponent.top <= 0:
    opponent.top = 0

  if opponent.bottom >= screen_height:
    opponent.bottom = screen_height

  
def ball_restart():
  
  global ball_speed_x, ball_speed_y

  ball.center = (screen_width/2, screen_height/2)

  ball_speed_y *= random.choice((1, -1)) 
  ball_speed_x *= random.choice((1, -1)) 
  


# GLOBAL VARIABLES

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangle
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height/ \
                     2-70, 10, 140)  # -70 missing
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)  # -70 missing

# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

# Game Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Sound Variables
pong_sound = pygame.mixer.Sound("./media/pong.ogg")
score_sound = pygame.mixer.Sound("./media/score.ogg")

# GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            player_speed -= 6
          if event.key == pygame.K_DOWN:
            player_speed += 6
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            player_speed += 6
          if event.key == pygame.K_DOWN:
            player_speed -= 6

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                                            0), (screen_width/2, screen_height))


    # Create a surface for the scores
    player_text = basic_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660,470))

    opponent_text = basic_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600,470))


    pygame.display.flip()
    clock.tick(60)
