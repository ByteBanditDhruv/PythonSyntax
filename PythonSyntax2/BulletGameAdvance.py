import pygame
import random

pygame.init()

W, H = 700, 450
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
game_over_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
RED = (255, 70, 80)
BLUE = (70, 180, 255)
CYAN = (50, 240, 255)
YELLOW = (255, 220, 0)
GREEN = (80, 255, 120)
BG = (8, 12, 35)

MAX_BULLETS = 25
bullets_left = MAX_BULLETS

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            r"C:\Users\OMOLP247\Downloads\ufo-alien-isolated-transparent-background-futuristic-ufo-spaceship-png-generative-ai_667511-3838.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, (60, 20))

        self.speed = random.randint(60, 100)

        self.direction = random.choice([-1, 1])

        y = random.randint(50, 250)

        if self.direction == 1:
            self.rect = self.image.get_rect(midright=(0, y))
        else:
            self.rect = self.image.get_rect(midleft=(W, y))

    def update(self, dt):

        self.rect.x += int(self.speed * self.direction * dt)

        if self.rect.right < 0 or self.rect.left > W:
            self.kill()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 35), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.image,
            RED,
            [(25, 0), (0, 35), (25, 27), (50, 35)]
        )
        pygame.draw.polygon(
            self.image,
            CYAN,
            [(25, 6), (17, 25), (25, 22), (33, 25)]
        )
        self.rect = self.image.get_rect(
            center=(W // 2, H - 35)
        )

    def update(self, dt):
        mouse_x = pygame.mouse.get_pos()[0]
        self.rect.centerx = mouse_x
        self.rect.clamp_ip(screen.get_rect())

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 18), pygame.SRCALPHA)
        pygame.draw.rect(
            self.image,
            CYAN,
            (0, 0, 6, 18),
            border_radius=3
        )
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        self.speed = 500

    def update(self, dt):
        self.rect.y -= int(self.speed * dt)
        if self.rect.bottom < 0:
            self.kill()

player = Player()
all_sprites.add(player)

score = 0

game_over = False

SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN, 700)

stars = []

for i in range(50):
    x = random.randrange(W)
    y = random.randrange(H)
    stars.append((x, y))

def restart_game():

    global bullets_left
    global score
    global game_over

    bullets_left = MAX_BULLETS
    score = 0
    game_over = False

    enemies.empty()

    bullets.empty()

    all_sprites.empty()

    all_sprites.add(player)

    player.rect.center = (W // 2, H - 35)

restart_button = pygame.Rect(
    W // 2 - 100,
    H // 2 + 50,
    200,
    55
)

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                if bullets_left > 0:
                    bullet = Bullet(
                        player.rect.centerx,
                        player.rect.top
                    )
                    bullets.add(bullet)
                    all_sprites.add(bullet)
                    bullets_left -= 1
                    if bullets_left == 0:
                        game_over = True

            else:

                if restart_button.collidepoint(event.pos):
                    restart_game()

        elif event.type == SPAWN:

            if not game_over:
                enemy = Enemy()
                enemies.add(enemy)
                all_sprites.add(enemy)

    if not game_over:

        all_sprites.update(dt)

        for bullet in bullets:
            hit_enemy = pygame.sprite.spritecollide(
                bullet,
                enemies,
                True
            )
            if hit_enemy:
                bullet.kill()
                score += len(hit_enemy)

    screen.fill(BG)
    for x, y in stars:
        pygame.draw.circle(
            screen,
            WHITE,
            (x, y),
            1
        )

    all_sprites.draw(screen)

    text = font.render(
        f"SCORE {score}",
        True,
        WHITE
    )

    screen.blit(text, (15, 12))

    bullet_text = font.render(
        f"BULLETS {bullets_left}",
        True,
        YELLOW
    )

    screen.blit(
        bullet_text,
        (530, 12)
    )


    if game_over:
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))

        screen.blit(overlay, (0, 0))

        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            RED
        )

        game_over_rect = game_over_text.get_rect(
            center=(W // 2, H // 2 - 60)
        )

        screen.blit(
            game_over_text,
            game_over_rect
        )

        final_score = font.render(
            f"Final Score: {score}",
            True,
            WHITE
        )

        final_score_rect = final_score.get_rect(
            center=(W // 2, H // 2 + 5)
        )

        screen.blit(
            final_score,
            final_score_rect
        )

        pygame.draw.rect(
            screen,
            GREEN,
            restart_button,
            border_radius=10
        )

        restart_text = button_font.render(
            "RESTART",
            True,
            BG
        )

        restart_text_rect = restart_text.get_rect(
            center=restart_button.center
        )

        screen.blit(
            restart_text,
            restart_text_rect
        )

    pygame.display.flip()


pygame.quit()