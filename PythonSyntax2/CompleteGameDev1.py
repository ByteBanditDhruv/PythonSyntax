import pygame
from pygame.locals import (
    K_ESCAPE, KEYDOWN, QUIT
)

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Centered Square")

# Create a surface (square)
surf = pygame.Surface((50, 50))
surf.fill((0, 0, 0))

# Get the centered position
surf_center = (
    (screen_width - surf.get_width()) / 2,
    (screen_height - surf.get_height()) / 2
)

run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False
        elif event.type == QUIT:
            run = False

    # Drawing section
    screen.fill((255, 255, 255))
    screen.blit(surf, surf_center)
    pygame.display.flip()

pygame.quit()
