import pygame
import sys



def ball_animation():

  global ball_speed_x, ball_speed_y

  ball.x += ball_speed_x
  ball.y += ball_speed_y

  # Ball Collision
  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1

  if ball.left <= 0 or ball.right >= screen_width:
    ball_speed_x *= -1

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


# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                                            0), (screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)
