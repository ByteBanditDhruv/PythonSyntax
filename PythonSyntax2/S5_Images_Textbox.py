# import pygame

# # # Step 1: Start Pygame
# pygame.init()

# # # Step 2: Create the game window
# screen = pygame.display.set_mode((1000, 800))
# pygame.display.set_caption("Displaying an Image")

# # # Step 3: Load the image
# car = pygame.image.load(
#     r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax2\F1_CAR.png"
# )
# car2 = pygame.image.load(
#     r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax2\F1_CAR.png"
# )

# # # Step 4: Keep the window open
# running = True

# while running:

# #     # Check events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# #     # Fill the screen with white
#     screen.fill((0, 0, 0))

#     car = pygame.transform.scale(car, (60, 120))

# #     # Draw the image on the screen
#     screen.blit(car, (80, 40))
#     screen.blit(car2, (360, 40))
    

# #     # Update the display
#     pygame.display.update()

# pygame.quit()


## Rotating the image
# import pygame

# # Step 1: Start Pygame
# pygame.init()

# # Step 2: Create the game window
# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Rotate Image")

# # Step 3: Load the image
# car = pygame.image.load(
#     r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax2\F1_CAR.png"
# )

# # (Optional) Resize the image
# car = pygame.transform.scale(car, (60, 120))

# # Step 4: Rotate the image by 90 degrees
# rotated_car = pygame.transform.rotate(car, 45)

# # Create a clock to control the frame rate
# clock = pygame.time.Clock()

# # Step 5: Game Loop
# running = True

# while running:

#     # Check for events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the background with white
#     screen.fill((255, 255, 255))

#     # Display the rotated image
#     screen.blit(car, (80, 40))

#     screen.blit(rotated_car, (225, 100))

#     # Update the screen
#     pygame.display.flip()

#     # Limit the game to 60 FPS
#     clock.tick(60)

# # Step 6: Quit Pygame
# pygame.quit()


## TEXTBOX
import pygame

pygame.init()

screen = pygame.display.set_mode((700,400))
pygame.display.set_caption("Simple Textbox")

font = pygame.font.Font(None, 32)

input_box = pygame.Rect(200,150,200,40)

text = ""

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]

            else:
                text += event.unicode

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(0,0,255),input_box,2)

    text_surface = font.render(text,True,(0,0,0))
    
    screen.blit(text_surface,(input_box.x+5,input_box.y+5))

    pygame.display.update()

pygame.quit()