"""Тесты для класса Game."""

from src.game import Game


def test_wall_collision() -> None:
    """Проверяет, что при ударе об стену игра заканчивается."""
    game = Game(width=5, height=5, speed=10)
    for _ in range(5):
        game.step()
    assert game.is_over is True


def test_eating_food() -> None:
    """Проверяет, что при поедании еды растет счет."""
    game = Game(width=10, height=10, speed=10)
    head = game.snake.head()
    game.food = (head[0] + 1, head[1])

    game.step()
    assert game.score == 1
