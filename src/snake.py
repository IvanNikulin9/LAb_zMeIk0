"""Модуль с классом Snake (Змейка)."""


class Snake:
    """Класс, описывающий змейку."""

    def __init__(
        self, start_pos: tuple[int, int], direction: tuple[int, int] = (0, 1)
    ) -> None:
        """Инициализация змейки.

        :param start_pos: Начальная позиция головы (x, y).
        :param direction: Начальное направление (dx, dy).
        """
        self.body: list[tuple[int, int]] = [start_pos]
        self.direction: tuple[int, int] = direction

    def head(self) -> tuple[int, int]:
        """Возвращает текущую позицию головы."""
        return self.body[0]

    def move(self) -> None:
        """Двигает змейку в текущем направлении."""
        head_x, head_y = self.head()
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)

    def grow(self) -> None:
        """Увеличивает длину змейки (оставляет хвост на месте)."""
        pass

    def change_direction(self, new_dir: tuple[int, int]) -> None:
        """Меняет направление, запрещая разворот на 180 градусов."""
        dx, dy = self.direction
        ndx, ndy = new_dir

        if (dx + ndx == 0) and (dy + ndy == 0):
            return
        self.direction = new_dir

    def collides_self(self) -> bool:
        """Проверяет, врезалась ли змейка в себя."""
        head = self.head()
        return head in self.body[1:]
