from typing import Generator


class EvenNumbers:
    """
    Итерируемый объект, который генерирует первые n четных чисел
    """

    def __init__(self, n: int):
        """
        Конструктор

        :param n: количество четных чисел для генерации
        :raises TypeError: если n не является целым числом
        :raises ValueError: если n отрицательное
        """
        if not isinstance(n, int):
            raise TypeError(f"n должно быть целым числом, получено {type(n).__name__}")

        if n < 0:
            raise ValueError(f"n не может быть отрицательным, получено {n}")

        self.n = n

    def __iter__(self) -> Generator[int, None, None]:
        """
        Генератор четных чисел

        :return: четное число
        """
        for i in range(self.n):
            yield 2 * i

    def __len__(self) -> int:
        return self.n

    def __repr__(self) -> str:
        return f"EvenNumbers({self.n})"
