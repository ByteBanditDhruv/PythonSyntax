import pygame, sys

pygame.init()

WIDTH, HEIGHT = 300, 340
GRID = WIDTH // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LW = 6

board = [[""] * 3 for _ in range(3)]
player = "X"
game_over = False
winner_line = None


def draw():
    screen.fill(WHITE)

    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * GRID, 0), (i * GRID, 300), LW)
        pygame.draw.line(screen, BLACK, (0, i * GRID), (300, i * GRID), LW)

    for r in range(3):
        for c in range(3):
            x, y = c * GRID, r * GRID
            if board[r][c] == "X":
                pygame.draw.line(screen, BLACK, (x + 20, y + 20), (x + 80, y + 80), LW)
                pygame.draw.line(screen, BLACK, (x + 80, y + 20), (x + 20, y + 80), LW)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLACK, (x + 50, y + 50), 30, LW)

    if winner_line:
        pygame.draw.line(screen, RED, *winner_line, 5)

    msg = (
        "Draw! Press R"
        if game_over and not winner_line
        else f"{player}'s Turn" if not game_over else f"{player} Wins! Press R"
    )

    screen.blit(font.render(msg, True, BLACK), (10, 308))


def check():
    global winner_line

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            winner_line = ((10, i * 100 + 50), (290, i * 100 + 50))
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            winner_line = ((i * 100 + 50, 10), (i * 100 + 50, 290))
            return True

    if board[0][0] == board[1][1] == board[2][2] != "":
        winner_line = ((10, 10), (290, 290))
        return True

    if board[0][2] == board[1][1] == board[2][0] != "":
        winner_line = ((290, 10), (10, 290))
        return True

    return False


while True:
    draw()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            board = [[""] * 3 for _ in range(3)]
            player = "X"
            game_over = False
            winner_line = None

        if e.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = e.pos
            if y < 300:
                r, c = y // GRID, x // GRID
                if board[r][c] == "":
                    board[r][c] = player
                    if check():
                        game_over = True
                    elif all(
                        board[i][j] != " " and board[i][j] != ""
                        for i in range(3)
                        for j in range(3)
                    ):
                        game_over = True
                    else:
                        player = "O" if player == "X" else "X"

    pygame.display.flip()



# import pygame

# def create_gradient_surface(width, height, color_top, color_bottom):
#     """Creates a smooth vertical gradient surface."""
#     # Create a 1x2 pixel surface
#     tiny_surface = pygame.Surface((1, 2))
    
#     # Set the top pixel and bottom pixel colors
#     tiny_surface.set_at((0, 0), color_top)
#     tiny_surface.set_at((0, 1), color_bottom)
    
#     # Smoothly scale it up to fill the required dimensions
#     gradient_surface = pygame.transform.smoothscale(tiny_surface, (width, height))
#     return gradient_surface

# # --- Example Usage ---
# pygame.init()
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Define your colors
# BLUE = (30, 144, 255)
# PURPLE = (75, 0, 130)

# # Generate the background once before the loop (highly efficient!)
# background = create_gradient_surface(SCREEN_WIDTH, SCREEN_HEIGHT, BLUE, PURPLE)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     # Draw the gradient background to the screen
#     screen.blit(background, (0, 0))
    
#     pygame.display.flip()

pygame.quit()