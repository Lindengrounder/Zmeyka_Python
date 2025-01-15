import random
import curses

# Инициализация экрана и окна
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Определение стенок
w.border(0)

# Начальные координаты змейки
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Начальные координаты еды
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

# Основной игровой цикл
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Проверка на столкновение со стеной или самим собой
    if snake[0][0] in [0, sh - 1] or \
            snake[0][1] in [0, sw - 1] or \
            snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    # Обработка нажатия клавиш
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Обработка поедания еды
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 2),
                random.randint(1, sw - 2)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)