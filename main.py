# заготовка ИИ для "тетрис"
import pygame
import random

# Инициализация игры
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tetris")

# Основные переменные
block_size = 30
grid_width = 10
grid_height = 20
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
clock = pygame.time.Clock()


# Функции для отрисовки и обработки событий
def draw_grid():
    for i in range(grid_height):
        for j in range(grid_width):
            pygame.draw.rect(screen, (255, 255, 255), (j * block_size, i * block_size, block_size, block_size), 1)


def draw_block(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x * block_size, y * block_size, block_size, block_size))


def generate_block():
    return random.choice([(3, 0), (4, 0), (5, 0), (6, 0)])


# Основной игровой цикл
running = True
while running:
    screen.fill((0, 0, 0))
    draw_grid()

    current_block = generate_block()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Движение блока влево
            pass
        if keys[pygame.K_RIGHT]:
            # Движение блока вправо
            pass
        if keys[pygame.K_DOWN]:
            # Ускоренное падение блока
            pass

        draw_block(*current_block)

        # Логика падения блока
        current_block = (current_block[0], current_block[1] + 1)

        clock.tick(1)  # Скорость падения блока

        pygame.display.flip()