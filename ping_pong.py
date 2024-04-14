import pygame

pygame.init()

width = 800
height = 600
white = (255, 255, 255)
black = (0, 0, 0)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Ракетки
racket_width = 10
racket_height = 100
racket_speed = 5

player1 = pygame.Rect(50, height // 2 - racket_height // 2, racket_width, racket_height)
player2 = pygame.Rect(width - 50 - racket_width, height // 2 - racket_height // 2, racket_width, racket_height)

# Шарик
ball_x = width // 2
ball_y = height // 2
ball_radius = 10
ball_speed_x = 7
ball_speed_y = 7

# Счет
score_player1 = 0
score_player2 = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= racket_speed
    if keys[pygame.K_s] and player1.y < height - racket_height:
        player1.y += racket_speed
    if keys[pygame.K_UP] and player2.y > 0:
        player2.y -= racket_speed
    if keys[pygame.K_DOWN] and player2.y < height - racket_height:
        player2.y += racket_speed

    # Движение шарика
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y > height - ball_radius or ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    if player1.collidepoint(ball_x, ball_y) or player2.collidepoint(ball_x, ball_y):
        ball_speed_x = -ball_speed_x
    if ball_x > width:
        score_player1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = -ball_speed_x
    if ball_x < 0:
        score_player2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = -ball_speed_x

    win.fill(black)
    pygame.draw.rect(win, white, player1)
    pygame.draw.rect(win, white, player2)
    pygame.draw.circle(win, white, (ball_x, ball_y), ball_radius)
    score_text = font.render(f"{score_player1} : {score_player2}", True, white)
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))
    pygame.display.update()

    clock.tick(60)
pygame.quit()
sys.exit()

# Клавиши управления
# up: Управление для первого игрока
# down: Управление для второго игрока
# w: Движение вверх первого игрока
# s: Движение вниз первого игрока
# ↑: Движение вверх второго игрока
# ↓: Движение вниз торого игрока
