const gameContainer = document.getElementById('game-container');
const gridSize = 20;
let snake = [{ x: 10, y: 10 }];
let food = { x: 5, y: 5 };
let dx = 0, dy = 0;
let intervalId;

// Создание сетки
function createGrid() {
  for (let row = 0; row < gridSize; row++) {
    for (let col = 0; col < gridSize; col++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      gameContainer.appendChild(cell);
    }
  }
}

// Отрисовка змейки и еды
function render() {
  const cells = document.querySelectorAll('.cell');
  cells.forEach(cell => cell.className = 'cell');

  // Отрисовка змейки
  snake.forEach(segment => {
    const cell = document.querySelector(`.cell:nth-child(${segment.y * gridSize + segment.x + 1})`);
    if (cell) cell.classList.add('snake');
  });

  // Отрисовка еды
  const foodCell = document.querySelector(`.cell:nth-child(${food.y * gridSize + food.x + 1})`);
  if (foodCell) foodCell.classList.add('food');
}

// Генерация новой позиции для еды
function generateFood() {
  food = {
    x: Math.floor(Math.random() * gridSize),
    y: Math.floor(Math.random() * gridSize)
  };
}

// Обновление состояния игры
function update() {
  const head = { x: snake[0].x + dx, y: snake[0].y + dy };
  snake.unshift(head);

  // Проверка столкновения со стенами или собой
  if (
    head.x < 0 || head.x >= gridSize ||
    head.y < 0 || head.y >= gridSize ||
    snake.some((segment, index) => index !== 0 && segment.x === head.x && segment.y === head.y)
  ) {
    clearInterval(intervalId);
    alert('Игра окончена!');
    return;
  }

  // Проверка, съела ли змейка еду
  if (head.x === food.x && head.y === food.y) {
    generateFood();
  } else {
    snake.pop();
  }

  render();
}

// Обработка нажатий клавиш
document.addEventListener('keydown', (event) => {
  switch (event.key) {
    case 'ArrowUp':
      if (dy === 0) { dx = 0; dy = -1; }
      break;
    case 'ArrowDown':
      if (dy === 0) { dx = 0; dy = 1; }
      break;
    case 'ArrowLeft':
      if (dx === 0) { dx = -1; dy = 0; }
      break;
    case 'ArrowRight':
      if (dx === 0) { dx = 1; dy = 0; }
      break;
  }
});

// Инициализация игры
function startGame() {
  createGrid();
  generateFood();
  render();
  intervalId = setInterval(update, 200);
}

startGame();
