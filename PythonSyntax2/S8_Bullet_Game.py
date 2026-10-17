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

stars = [(random.randrange(W), random.randrange(H), random.choice([1, 1, 2]))
         for _ in range(70)]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 25), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, BLUE, [(0, 8), (10, 0), (25, 0), (35, 8), (28, 23), (7, 23)])
        pygame.draw.rect(self.image, CYAN, (12, 7, 11, 8))
        self.rect = self.image.get_rect(
            center=(random.randint(25, W - 25), random.randint(30, 220))
        )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 35), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, RED, [(25, 0), (0, 35), (25, 27), (50, 35)])
        pygame.draw.polygon(self.image, CYAN, [(25, 6), (17, 25), (25, 22), (33, 25)])
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
        self.rect.y -= 9
        if self.rect.bottom < 0:
            self.kill()



for i in range(25):
    e = Enemy()
    enemies.add(e)
    all_sprites.add(e)

player = Player()
all_sprites.add(player)

score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(b)
            all_sprites.add(b)

    all_sprites.update()

    for bullet in bullets:
        hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if hit:
            bullet.kill()
            score += len(hit)

    screen.fill(BG)

    for x, y, size in stars:
        pygame.draw.circle(screen, WHITE, (x, y), size)

    pygame.draw.line(screen, (30, 50, 90), (0, 40), (W, 40), 2)

    all_sprites.draw(screen)

    screen.blit(font.render(f"SCORE  {score}", True, WHITE), (15, 12))

    if len(enemies) == 0:
        win = font.render("YOU WIN!", True, YELLOW)
        screen.blit(win, win.get_rect(center=(W // 2, H // 2)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()