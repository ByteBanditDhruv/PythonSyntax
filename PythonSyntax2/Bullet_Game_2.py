import pygame, random

pygame.init()

W, H = 700, 450
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

WHITE = (255, 255, 255)
RED = (255, 70, 80)
BLUE = (70, 180, 255)
CYAN = (50, 240, 255)
YELLOW = (255, 220, 0)
BG = (8, 12, 35)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

BULLET_SPEED = 9
MAX_BULLETS = 25


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 25), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, BLUE,
            [(0, 8), (10, 0), (25, 0), (35, 8), (28, 23), (7, 23)])
        pygame.draw.rect(self.image, CYAN, (12, 7, 11, 8))

        self.speed = random.randint(2, 5)
        self.direction = random.choice([-1, 1])
        y = random.randint(50, 250)

        if self.direction == 1:
            self.rect = self.image.get_rect(midright=(0, y))
        else:
            self.rect = self.image.get_rect(midleft=(W, y))

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right < 0 or self.rect.left > W:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 35), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, RED,
            [(25, 0), (0, 35), (25, 27), (50, 35)])
        pygame.draw.polygon(self.image, CYAN,
            [(25, 6), (17, 25), (25, 22), (33, 25)])
        self.rect = self.image.get_rect(center=(W // 2, H - 35))

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(screen.get_rect())


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 18), pygame.SRCALPHA)
        pygame.draw.rect(self.image, YELLOW, (0, 0, 6, 18), border_radius=3)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= BULLET_SPEED

        if self.rect.bottom < 0:
            self.kill()


player = Player()
all_sprites.add(player)

score = 0
bullets_left = MAX_BULLETS

running = True

SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN, 700)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bullets_left > 0:
                b = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(b)
                all_sprites.add(b)
                bullets_left -= 1

        elif event.type == SPAWN:
            e = Enemy()
            enemies.add(e)
            all_sprites.add(e)

    all_sprites.update()

    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, enemies, True):
            bullet.kill()
            score += 1

    screen.fill(BG)

    for i in range(50):
        x = random.randrange(W)
        y = random.randrange(H)
        pygame.draw.circle(screen, WHITE, (x, y), 1)

    all_sprites.draw(screen)

    score_text = font.render(f"SCORE {score}", True, WHITE)
    screen.blit(score_text, (15, 12))

    bullet_text = font.render(f"BULLETS {bullets_left}", True, YELLOW)
    screen.blit(bullet_text, (530, 12))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()