# import pygame

# # # Start Pygame
# pygame.init()

# # # Create a game window
# screen = pygame.display.set_mode((600, 400))

# # # Give the window a title
# pygame.display.set_caption("My First Pygame Window")

# running = True

# # # Game Loop
# while running:

# #     # Check for events
#     for event in pygame.event.get():

# #         # If the user clicks the X button
#         if event.type == pygame.QUIT:
#             running = False

# # # Close Pygame
# pygame.quit()


## ADDING BACKGROUND COLOR
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Blue Screen")

# running = True

# while running:

#     # Fill the screen with blue
#     screen.fill((0, 0, 255))
#     # screen.fill((253, 112, 244)) ##PINK

#     # Update the display so the color appears
#     pygame.display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_UP:
#                 print("UP!")

#             if event.key == pygame.K_DOWN:
#                 print("DOWN!")

#             if event.key == pygame.K_LEFT:
#                 print("LEFT!")

#             if event.key == pygame.K_RIGHT:
#                 print("RIGHT!")

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print("Clicked at: ", event.pos)

#         if event.type == pygame.MOUSEMOTION:
#                     print("MOUSE IS MOVING")

# pygame.quit()


# screen.fill((255, 0, 0)) RED
# (Red, Green, Blue)

# screen.fill((0, 255, 0)) GREEN
# screen.fill((0, 0, 255)) BLUE

# screen.fill((255, 255, 255)) WHITE
# screen.fill((0, 0, 0)) BLACK

# screen.fill((255, 255, 0)) RED + GREEN = YELLOW

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Color Changer")

# Starting color
color = (255, 255, 255)

running = True

while running:

    screen.fill(color)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Clicked!")

        # Keyboard
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                color = (255, 0, 0)

            if event.key == pygame.K_g:
                color = (0, 255, 0)

            if event.key == pygame.K_b:
                color = (0, 0, 255)

            if event.key == pygame.K_SPACE:
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

    pygame.display.flip()

pygame.quit()
