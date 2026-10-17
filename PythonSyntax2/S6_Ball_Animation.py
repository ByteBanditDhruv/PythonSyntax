# ## Single Ball Animation

# import pygame
# import time
# pygame.init()
# screen = pygame.display.set_mode([500,500])
# clock=pygame.time.Clock()
# x=250
# y=250
# run=True
# while run:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
#     screen.fill((255,255,255))
#     pygame.draw.circle(screen,(0,0,255),(x,y),75)
#     pygame.display.flip()
#     x=x+1
#     y=y+1
#     clock.tick(30)
# pygame.quit()


## Multiple Balls
import pygame
from random import randint

# Initialize pygame
pygame.init()

# Create window
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Balls Colliding")

clock = pygame.time.Clock()


# Ball Class
class Ball:

    def __init__(self):
        # Random position
        self.x = randint(30, WIDTH - 30)
        self.y = randint(30, HEIGHT - 30)

        # Random size
        self.radius = randint(15, 80)

        # Random colour
        self.color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

        # Random speed
        self.x_speed = randint(2, 6)
        self.y_speed = randint(2, 6)

        # Random direction
        if randint(0, 1):
            self.x_speed *= -1
        if randint(0, 1):
            self.y_speed *= -1

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce(self):

        # Left & Right Wall
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.x_speed = -self.x_speed

        # Top & Bottom Wall
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.y_speed = -self.y_speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


# Create a list to store all balls
balls = []

# Create 10 balls
for i in range(20):
    balls.append(Ball())


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Update every ball
    for ball in balls:
        ball.move()
        ball.bounce()
        ball.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()