"""Модуль с классом Game (Игра)."""

import random

from src.snake import Snake


class Game:
    """Класс, описывающий игровой процесс."""

    def __init__(self, width: int, height: int, speed: int) -> None:
        """Инициализация игры."""
        self.width: int = width
        self.height: int = height
        self.speed: int = speed
        self.score: int = 0
        self.is_over: bool = False

        start_x = width // 2
        start_y = height // 2
        self.snake: Snake = Snake((start_x, start_y), (1, 0))

        self.food: tuple[int, int] = (0, 0)
        self.spawn_food()

    def spawn_food(self) -> None:
        """Спавнит еду в случайной свободной клетке."""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            new_food = (x, y)
            if new_food not in self.snake.body:
                self.food = new_food
                break

    def step(self, new_direction: tuple[int, int] | None = None) -> None:
        """Один шаг логики игры."""
        if self.is_over:
            return

        if new_direction is not None:
            self.snake.change_direction(new_direction)

        self.snake.move()
        head = self.snake.head()

        if not (0 <= head[0] < self.width and 0 <= head[1] < self.height):
            self.is_over = True
            return

        if head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.body.pop()

        if self.snake.collides_self():
            self.is_over = True
