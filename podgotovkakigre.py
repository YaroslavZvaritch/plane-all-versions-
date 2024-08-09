import pygame
pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Игра")
# Основной игровой цикл
running = True
A = pygame.Rect(0,0,100,100)
X = 0
Y = 0
clock = pygame.time.Clock()
while running:
    window.fill((213,132,123))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Здесь вы можете добавить код для обновления игры
    X += 1
    Y += 1
    A.x = X
    A.y = Y

    pygame.draw.rect(window,[193,238,236],A)

    # Отображение изменений на экране
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
