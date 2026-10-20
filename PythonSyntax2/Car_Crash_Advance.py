
import pygame
import random
import os

pygame.init()

# -------------------- SETTINGS --------------------
WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("F1 Racing - Car Crash Challenge")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (240, 50, 50)
GREEN = (50, 230, 100)
YELLOW = (255, 220, 0)
GRAY = (65, 65, 70)
DARK = (20, 20, 25)
BLUE = (50, 160, 255)
ORANGE = (255, 145, 30)

# Road settings
ROAD_LEFT = 180
ROAD_RIGHT = 620
LANES = [250, 400, 550]
LANE_WIDTH = 150

# Change this path if your image is stored elsewhere
CAR_IMAGE_PATH = (
    r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv"
    r"\Python\PythonSyntax2\F1_CAR.png"
)

font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 65)
small_font = pygame.font.Font(None, 24)

HIGH_SCORE_FILE = "car_highscore.txt"


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def draw_text(text, font_obj, color, x, y, center=False):
    image = font_obj.render(text, True, color)

    if center:
        rect = image.get_rect(center=(x, y))
        screen.blit(image, rect)
    else:
        screen.blit(image, (x, y))


# -------------------- PLAYER --------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        original = pygame.image.load(
            CAR_IMAGE_PATH
        ).convert_alpha()

        self.image = pygame.transform.scale(
            original, (60, 100)
        )

        self.rect = self.image.get_rect(
            center=(400, 490)
        )

        self.mask = pygame.mask.from_surface(self.image)

        self.lives = 3
        self.nitro = 100
        self.invincible = 0

    def update(self):
        keys = pygame.key.get_pressed()

        # Smooth movement
        move_speed = 6

        if keys[pygame.K_SPACE] and self.nitro > 0:
            move_speed = 10
            self.nitro = max(0, self.nitro - 0.8)
        else:
            self.nitro = min(100, self.nitro + 0.25)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= move_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += move_speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 4

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 4

        # Keep car inside road and screen
        self.rect.left = max(ROAD_LEFT + 5, self.rect.left)
        self.rect.right = min(ROAD_RIGHT - 5, self.rect.right)
        self.rect.top = max(HEIGHT // 3, self.rect.top)
        self.rect.bottom = min(HEIGHT - 10, self.rect.bottom)

        if self.invincible > 0:
            self.invincible -= 1


# -------------------- ENEMY TRAFFIC --------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()

        original = pygame.image.load(
            CAR_IMAGE_PATH
        ).convert_alpha()

        self.image = pygame.transform.scale(
            original, (55, 95)
        )

        # Turn the car around to face the player
        self.image = pygame.transform.rotate(
            self.image, 180
        )

        lane_x = random.choice(LANES)

        self.rect = self.image.get_rect(
            center=(lane_x, random.randint(-180, -100))
        )

        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed + random.randint(-1, 2)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()


# -------------------- ROAD --------------------
def draw_road(offset):
    screen.fill(GREEN)

    # Road surface
    pygame.draw.rect(
        screen, GRAY,
        (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT)
    )

    # Road edges
    pygame.draw.rect(
        screen, WHITE,
        (ROAD_LEFT, 0, 6, HEIGHT)
    )
    pygame.draw.rect(
        screen, WHITE,
        (ROAD_RIGHT - 6, 0, 6, HEIGHT)
    )

    # Animated lane dividers
    for lane_x in [325, 475]:
        for y in range(-40, HEIGHT, 60):
            pygame.draw.rect(
                screen, YELLOW,
                (lane_x - 3, y + offset, 6, 35)
            )


# -------------------- HUD --------------------
def draw_hud(score, player, speed_level):
    pygame.draw.rect(screen, DARK, (0, 0, WIDTH, 70))

    draw_text(
        f"SCORE: {score}", font, WHITE, 20, 12
    )

    draw_text(
        f"LEVEL: {speed_level}", font, YELLOW, 20, 42
    )

    draw_text(
        f"LIVES: {player.lives}", font, RED, 270, 12
    )

    draw_text(
        f"SPEED: {speed_level * 10}", font, BLUE, 270, 42
    )

    # Nitro bar
    draw_text("NITRO", small_font, WHITE, 520, 12)

    pygame.draw.rect(
        screen, WHITE, (520, 35, 200, 18), 2
    )

    nitro_width = int(194 * player.nitro / 100)

    if nitro_width > 0:
        pygame.draw.rect(
            screen, BLUE,
            (523, 38, nitro_width, 12)
        )


# -------------------- MENUS --------------------
def main_menu(high_score):
    while True:
        screen.fill(DARK)

        draw_text(
            "F1 RACING", big_font, RED,
            WIDTH // 2, 150, True
        )

        draw_text(
            "CAR CRASH CHALLENGE", font, WHITE,
            WIDTH // 2, 205, True
        )

        draw_text(
            "Press ENTER to Start", font, GREEN,
            WIDTH // 2, 310, True
        )

        draw_text(
            "Arrow Keys / WASD: Move",
            small_font, WHITE,
            WIDTH // 2, 370, True
        )

        draw_text(
            "SPACE: Nitro     P: Pause",
            small_font, BLUE,
            WIDTH // 2, 405, True
        )

        draw_text(
            f"BEST SCORE: {high_score}",
            font, YELLOW, WIDTH // 2, 465, True
        )

        draw_text(
            "ESC: Quit", small_font, WHITE,
            WIDTH // 2, 520, True
        )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True

                if event.key == pygame.K_ESCAPE:
                    return False

        clock.tick(FPS)


def game_over_screen(score, high_score):
    while True:
        screen.fill(DARK)

        draw_text(
            "GAME OVER!", big_font, RED,
            WIDTH // 2, 170, True
        )

        draw_text(
            f"YOUR SCORE: {score}", font, WHITE,
            WIDTH // 2, 260, True
        )

        draw_text(
            f"BEST SCORE: {high_score}",
            font, YELLOW, WIDTH // 2, 305, True
        )

        draw_text(
            "Press R to Restart",
            font, GREEN, WIDTH // 2, 390, True
        )

        draw_text(
            "Press ESC for Menu",
            font, WHITE, WIDTH // 2, 435, True
        )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"

                if event.key == pygame.K_ESCAPE:
                    return "menu"

        clock.tick(FPS)


# -------------------- GAMEPLAY --------------------
def play_game(high_score):
    player = Player()

    all_sprites = pygame.sprite.Group(player)
    enemies = pygame.sprite.Group()

    road_offset = 0
    start_time = pygame.time.get_ticks()
    spawn_timer = 0
    score = 0
    paused = False
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", high_score

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu", high_score

                if event.key == pygame.K_p:
                    paused = not paused

        if paused:
            draw_text(
                "PAUSED", big_font, YELLOW,
                WIDTH // 2, HEIGHT // 2, True
            )

            draw_text(
                "Press P to Resume",
                font, WHITE, WIDTH // 2,
                HEIGHT // 2 + 55, True
            )

            pygame.display.flip()
            continue

        seconds = (pygame.time.get_ticks() - start_time) // 1000
        score = seconds * 10

        # Difficulty gradually increases
        speed_level = min(1 + seconds // 15, 10)
        enemy_speed = min(5 + seconds // 8, 12)

        # Nitro increases the road's scrolling speed
        keys = pygame.key.get_pressed()
        road_speed = 8

        if keys[pygame.K_SPACE] and player.nitro > 0:
            road_speed = 13

        road_offset = (road_offset + road_speed) % 60

        # Spawn traffic at controlled intervals
        spawn_timer += 1

        spawn_interval = max(22, 65 - seconds // 2)

        if spawn_timer >= spawn_interval:
            spawn_timer = 0

            enemy = Enemy(enemy_speed)

            # Avoid spawning directly on top of another car
            overlapping = any(
                abs(enemy.rect.centerx - other.rect.centerx) < 65
                and abs(enemy.rect.centery - other.rect.centery) < 120
                for other in enemies
            )

            if not overlapping:
                enemies.add(enemy)
                all_sprites.add(enemy)

        # Update game objects
        all_sprites.update()

        # Collision detection
        if player.invincible == 0:
            hits = pygame.sprite.spritecollide(
                player, enemies, True,
                pygame.sprite.collide_mask
            )

            if hits:
                player.lives -= 1
                player.invincible = FPS * 2

                if player.lives <= 0:
                    running = False

        # Draw scene
        draw_road(road_offset)

        # Flash player after a crash
        if player.invincible == 0 or (player.invincible // 6) % 2 == 0:
            screen.blit(player.image, player.rect)

        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)

        draw_hud(score, player, speed_level)

        draw_text(
            "SPACE = NITRO", small_font, WHITE,
            WIDTH // 2, HEIGHT - 28, True
        )

        pygame.display.flip()

    # Save best score
    high_score = max(high_score, score)
    save_high_score(high_score)

    return "gameover", high_score


# -------------------- MAIN PROGRAM --------------------
def main():
    high_score = load_high_score()

    while True:
        if not main_menu(high_score):
            break

        while True:
            result, high_score = play_game(high_score)

            if result == "quit":
                pygame.quit()
                return

            if result == "menu":
                break

            if result == "gameover":
                choice = game_over_screen(
                    high_score if False else 0,
                    high_score
                )

                # The restart option begins a fresh race
                if choice == "restart":
                    continue

                if choice == "menu":
                    break

                if choice == "quit":
                    pygame.quit()
                    return

    pygame.quit()


if __name__ == "__main__":
    main()
