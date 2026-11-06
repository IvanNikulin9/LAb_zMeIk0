"""Тесты для класса Snake."""

from src.snake import Snake


def test_snake_move() -> None:
    """Проверяет, что змейка движется в правильном направлении."""
    snake = Snake((2, 2), (1, 0))
    snake.move()
    assert snake.head() == (3, 2)


def test_snake_collides_self() -> None:
    """Проверяет самопересечение."""
    snake = Snake((2, 2), (1, 0))
    snake.move()  # Голова (3,2), тело [(3,2), (2,2)]
    snake.move()  # Голова (4,2), тело [(4,2), (3,2), (2,2)]

    snake.body.insert(0, (3, 2))
    assert snake.collides_self() is True
