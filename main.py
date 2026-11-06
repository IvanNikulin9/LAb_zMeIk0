"""Точка входа для запуска игры Змейка."""

import argparse
import msvcrt
import os
import sys
import time

from src.game import Game


def draw_board(game: Game) -> None:
    """Отрисовка поля в терминале."""
    os.system("cls" if os.name == "nt" else "clear")

    print(f"Счет: {game.score} | Управление: WASD / Стрелки")
    print("Пауза: Пробел | Выход: Q")

    print("╔" + "═" * (game.width * 2) + "╗")

    for y in range(game.height):
        print("║", end="")
        for x in range(game.width):
            if (x, y) == game.snake.head():
                print("@@", end="")
            elif (x, y) in game.snake.body:
                print("()", end="")
            elif (x, y) == game.food:
                print("**", end="")
            else:
                print("  ", end="")
        print("║")

    print("╚" + "═" * (game.width * 2) + "╝")


def get_input() -> str | tuple[int, int] | None:
    """Считывает нажатие клавиши без Enter (Windows)."""
    if msvcrt.kbhit():
        key = msvcrt.getwch()

        if key in ("\xe0", "\x00"):
            arrow = msvcrt.getwch()
            if arrow == "H":
                return (0, -1)
            if arrow == "P":
                return (0, 1)
            if arrow == "K":
                return (-1, 0)
            if arrow == "M":
                return (1, 0)
            return None

        if key in ("q", "Q", "й", "Й"):
            sys.exit(0)

        if key == " ":
            return "pause"

        if key in ("w", "W", "ц", "Ц"):
            return (0, -1)
        if key in ("s", "S", "ы", "Ы"):
            return (0, 1)
        if key in ("a", "A", "ф", "Ф"):
            return (-1, 0)
        if key in ("d", "D", "в", "В"):
            return (1, 0)

    return None


def main() -> None:
    """Главная функция запуска."""
    parser = argparse.ArgumentParser(description="Игра Змейка")
    parser.add_argument("--width", type=int, default=20, help="Ширина поля")
    parser.add_argument("--height", type=int, default=15, help="Высота поля")
    parser.add_argument("--speed", type=int, default=8, help="Скорость")
    args = parser.parse_args()

    if args.width < 5 or args.width > 40 or args.height < 5 or args.height > 40:
        print("Ошибка: Ширина и высота поля должны быть не меньше 5 и не больше 40.")
        sys.exit(1)
    if args.speed < 1:
        print("Ошибка: Скорость должна быть положительным числом (1 и выше).")
        sys.exit(1)

    game = Game(width=args.width, height=args.height, speed=args.speed)

    print("Игра начинается! Нажмите любую клавишу...")
    msvcrt.getwch()

    while not game.is_over:
        draw_board(game)
        time.sleep(1.0 / args.speed)

        action = get_input()

        if action == "pause":
            print("\nПАУЗА. Нажмите любую клавишу для продолжения...")
            msvcrt.getwch()
            continue

        if isinstance(action, tuple) or action is None:
            game.step(action)

    draw_board(game)
    print(f"\nИгра окончена! Ваш счет: {game.score}")


if __name__ == "__main__":
    main()
