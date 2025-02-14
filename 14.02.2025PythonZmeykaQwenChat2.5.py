import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 400
screen_height = 400
block_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Часы для контроля скорости
clock = pygame.time.Clock()

# Функция для отрисовки змейки
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

# Основная функция игры
def game_loop():
    game_over = False
    game_exit = False

    # Начальная позиция змейки
    snake_x = screen_width // 2
    snake_y = screen_height // 2
    snake_dx = 0
    snake_dy = 0
    snake_list = []
    snake_length = 1

    # Позиция еды
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_exit:
        while game_over:
            screen.fill(black)
            font = pygame.font.SysFont(None, 50)
            message = font.render("Игра окончена! Нажмите Q для выхода или C для повторной игры.", True, red)
            screen.blit(message, [20, screen_height // 2])
            pygame.display.update()

            # Обработка событий после проигрыша
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dx == 0:
                    snake_dx = -block_size
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT and snake_dx == 0:
                    snake_dx = block_size
                    snake_dy = 0
                elif event.key == pygame.K_UP and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = -block_size
                elif event.key == pygame.K_DOWN and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = block_size

        # Обновление позиции змейки
        snake_x += snake_dx
        snake_y += snake_dy

        # Проверка столкновения со стенами
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_over = True

        # Проверка столкновения с собой
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Проверка, съела ли змейка еду
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        # Отрисовка
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        draw_snake(snake_list)
        pygame.display.update()

        # Установка скорости игры
        clock.tick(10)

    pygame.quit()
    quit()

# Запуск игры
game_loop()
