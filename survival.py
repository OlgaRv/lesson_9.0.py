import pygame
import random

# Инициализация игры
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Survival Game")
clock = pygame.time.Clock()

player = pygame.Rect(400, 300, 10, 10)
enemies = []

def generate_enemy():
    enemy = pygame.Rect(random.randint(20, 700), 0, 10, 10)
    enemies.append(enemy)

def move_enemies():
    for enemy in enemies:
        enemy.y += 5
def check_collision():
    for enemy in enemies:
        if player.colliderect(enemy):
            return True
    return False

# Основной игровой цикл
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    generate_enemy()
    move_enemies()

    if check_collision():
        running = False

    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.draw.rect(screen, (0, 255, 0), player)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()


# Этот код создает игру на выживание, где игрок управляет зеленым прямоугольником с клавиатуры,
# избегая касания красных прямоугольников (врагов), которые случайно появляются на экране.
# Если игрок касается врага, игра завершается. В игре нет изменения сложности и победы,
# это просто основа для реализации игры на выживание.
