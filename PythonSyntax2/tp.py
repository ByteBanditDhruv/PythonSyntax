import pygame
import math
import random
import sys

# 1. Initialize Window & Canvas Context
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Hockey: Pro AI Championship")
clock = pygame.time.Clock()

# Color Palettes & Fonts
ICE, RED, BLUE, PUCK_COLOR, LINES = (240, 245, 255), (240, 60, 60), (40, 100, 240), (30, 30, 40), (200, 210, 230)
DK_GRAY, WHITE, GREEN, AMBER = (30, 35, 45), (255, 255, 255), (46, 204, 113), (241, 196, 15)

font_ui = pygame.font.SysFont("Arial", 40, bold=True)
font_btn = pygame.font.SysFont("Arial", 28, bold=True)
font_title = pygame.font.SysFont("Arial", 50, bold=True)

# 2. Physics & Engine Setup Constants
MALLET_R, PUCK_R, GOAL_WIDTH = 30, 15, 180

# States: "MENU", "PLAYING", "PLAYER_WIN", "BOT_WIN"
state = "MENU"
bot_speed = 5.0
p_score, b_score = 0, 0

# Entity Coordinate Data Stems
px, py = WIDTH // 2, HEIGHT - 150
bx, by = WIDTH // 2, 150
puck_x, puck_y, puck_vx, puck_vy = WIDTH // 2, HEIGHT // 2, 0.0, 0.0

def reset_puck():
    global puck_x, puck_y, puck_vx, puck_vy
    puck_x, puck_y = WIDTH // 2, HEIGHT // 2
    puck_vx = random.choice([-4.0, 4.0])
    puck_vy = random.choice([-4.0, 4.0])

# Define Interactive Menu Rect Boxes [X, Y, W, H]
btn_easy = pygame.Rect(150, 320, 300, 60)
btn_med  = pygame.Rect(150, 410, 300, 60)
btn_hard = pygame.Rect(150, 500, 300, 60)

# 3. Core Structural Execution State Loop
running = True
while running:
    clock.tick(60)
   
    # Handle Input Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
       
        # --- LAYER A: MENU SELECTION LOGIC ---
        if state == "MENU" and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if btn_easy.collidepoint(mx, my):
                bot_speed, state, p_score, b_score = 3.2, "PLAYING", 0, 0
                reset_puck()
            elif btn_med.collidepoint(mx, my):
                bot_speed, state, p_score, b_score = 5.2, "PLAYING", 0, 0
                reset_puck()
            elif btn_hard.collidepoint(mx, my):
                bot_speed, state, p_score, b_score = 8.0, "PLAYING", 0, 0
                reset_puck()
       
        # --- LAYER B: WIN SCREEN INTERRUPT ---
        elif state in ["PLAYER_WIN", "BOT_WIN"] and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = "MENU"

    # --- STATE 1: MAIN MENU SELECTION LAYER ---
    if state == "MENU":
        screen.fill(DK_GRAY)
        title = font_title.render("ICE HOCKEY AI", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 180))
       
        pygame.draw.rect(screen, GREEN, btn_easy, border_radius=8)
        pygame.draw.rect(screen, AMBER, btn_med, border_radius=8)
        pygame.draw.rect(screen, RED, btn_hard, border_radius=8)
       
        t_easy = font_btn.render("EASY MODE", True, DK_GRAY)
        t_med  = font_btn.render("MEDIUM MODE", True, DK_GRAY)
        t_hard = font_btn.render("HARD MODE", True, WHITE)
       
        screen.blit(t_easy, (WIDTH // 2 - t_easy.get_width() // 2, 332))
        screen.blit(t_med,  (WIDTH // 2 - t_med.get_width() // 2, 422))
        screen.blit(t_hard, (WIDTH // 2 - t_hard.get_width() // 2, 512))

    # --- STATE 2: ACTIVE GAMEPLAY PHYSICS LAYER ---
    elif state == "PLAYING":
        screen.fill(ICE)
        mx, my = pygame.mouse.get_pos()
        px = max(MALLET_R, min(WIDTH - MALLET_R, mx))
        py = max(HEIGHT // 2 + MALLET_R, min(HEIGHT - MALLET_R, my))

        # Predictive Bot Vector tracking Engine
        if puck_y < HEIGHT // 2:
            if bx < puck_x - 10:   bx += bot_speed
            elif bx > puck_x + 10: bx -= bot_speed
            if by < puck_y - 20:   by += bot_speed
            elif by > 100:         by -= bot_speed
        else:
            if bx < WIDTH // 2:  bx += bot_speed
            elif bx > WIDTH // 2: bx -= bot_speed
            by = by + bot_speed if by < 150 else by - bot_speed if by > 150 else by

        bx = max(MALLET_R, min(WIDTH - MALLET_R, bx))
        by = max(MALLET_R, min(HEIGHT // 2 - MALLET_R, by))

        # Vector Puck Physics Calculations
        puck_vx *= 0.995; puck_vy *= 0.995
        puck_x += puck_vx; puck_y += puck_vy

        # Cushion Boundary Collisions
        if puck_x <= PUCK_R or puck_x >= WIDTH - PUCK_R:
            puck_vx *= -1
            puck_x = max(PUCK_R, min(WIDTH - PUCK_R, puck_x))

        if puck_y <= PUCK_R or puck_y >= HEIGHT - PUCK_R:
            if WIDTH // 2 - GOAL_WIDTH // 2 <= puck_x <= WIDTH // 2 + GOAL_WIDTH // 2:
                if puck_y <= PUCK_R: p_score += 1
                else:                b_score += 1
               
                # Check Championship Ending Trigger Criteria
                if p_score >= 5:   state = "PLAYER_WIN"
                elif b_score >= 5: state = "BOT_WIN"
                else:              reset_puck()
            else:
                puck_vy *= -1
                puck_y = max(PUCK_R, min(HEIGHT - PUCK_R, puck_y))

        # Pure Circle Intersect Elastic Reflection Solver Math (Pythagorus Theorem)
        for mx_pos, my_pos in [(px, py), (bx, by)]:
            dist = math.hypot(puck_x - mx_pos, puck_y - my_pos)
            min_dist = MALLET_R + PUCK_R
            if dist < min_dist:
                angle = math.atan2(puck_y - my_pos, puck_x - mx_pos)
                puck_x = mx_pos + math.cos(angle) * min_dist
                puck_y = my_pos + math.sin(angle) * min_dist
                speed_coefficient = 9.0 + (bot_speed * 0.4)
                puck_vx = math.cos(angle) * speed_coefficient
                puck_vy = math.sin(angle) * speed_coefficient

        # Field Layout Overlay Lines Rendering
        pygame.draw.line(screen, RED, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 4)
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 70, 4)
        pygame.draw.rect(screen, RED, (WIDTH // 2 - GOAL_WIDTH // 2, 0, GOAL_WIDTH, 10))
        pygame.draw.rect(screen, BLUE, (WIDTH // 2 - GOAL_WIDTH // 2, HEIGHT - 10, GOAL_WIDTH, 10))

        # Draw Active Entities
        pygame.draw.circle(screen, BLUE, (int(px), int(py)), MALLET_R)
        pygame.draw.circle(screen, RED, (int(bx), int(by)), MALLET_R)
        pygame.draw.circle(screen, PUCK_COLOR, (int(puck_x), int(puck_y)), PUCK_R)

        # Render Core Score String Interface Layouts
        txt_bot = font_ui.render(str(b_score), True, LINES)
        txt_plr = font_ui.render(str(p_score), True, LINES)
        screen.blit(txt_bot, (WIDTH - 50, HEIGHT // 2 - 60))
        screen.blit(txt_plr, (WIDTH - 50, HEIGHT // 2 + 20))

    # --- STATE 3 & 4: CHAMPIONSHIP ENDINGS ---
    elif state in ["PLAYER_WIN", "BOT_WIN"]:
        screen.fill(DK_GRAY)
        win_msg = "YOU WIN THE CUP!" if state == "PLAYER_WIN" else "BOT WINS THE CUP!"
        win_color = GREEN if state == "PLAYER_WIN" else RED
       
        txt_title = font_title.render(win_msg, True, win_color)
        txt_sub = font_btn.render("PRESS [SPACE] FOR MAIN MENU", True, WHITE)
       
        screen.blit(txt_title, (WIDTH // 2 - txt_title.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(txt_sub, (WIDTH // 2 - txt_sub.get_width() // 2, HEIGHT // 2 + 30))

    pygame.display.flip()

pygame.quit()
sys.exit()  