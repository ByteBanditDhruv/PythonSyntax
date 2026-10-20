import pygame, random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Crash Game")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (70,70,70)
YELLOW = (255,255,0)

road_y = 0
font = pygame.font.Font(None,40)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\Python\PythonSyntax2\F1_CAR.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,120))
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT-10))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\Python\PythonSyntax2\F1_CAR.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,120))
        self.image = pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH-90), y=random.randint(-300,-100))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = random.randint(5,8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

start = pygame.time.get_ticks()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.speed = -7
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.speed = 7

        elif event.type == pygame.KEYUP:
            player.speed = 0

    if random.randint(1,100) < 4:
        enemy = Enemy()
        if not pygame.sprite.spritecollide(enemy, enemies, False, pygame.sprite.collide_mask):
            enemies.add(enemy)
            all_sprites.add(enemy)

    seconds = (pygame.time.get_ticks() - start) // 1000

    for enemy in enemies:
        enemy.speed = min(15 + seconds//5, 12)

    all_sprites.update()

    # Draw Road
    screen.fill(GRAY)

    # Moving Lane Divider
    road_y = (road_y + 8) % 40
    for y in range(-40, HEIGHT, 40):
        pygame.draw.rect(screen, YELLOW, (395, y + road_y, 10, 25))

    all_sprites.draw(screen)

    score = font.render(f"Score : {seconds}", True, WHITE)
    screen.blit(score, (20,20))

    if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
        text = pygame.font.Font(None,70).render("GAME OVER...😔😔", True, RED)
        screen.blit(text, (WIDTH//2-text.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()