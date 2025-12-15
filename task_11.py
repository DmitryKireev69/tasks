class Dessert:
    """Класс для представления десерта"""

    def __init__(self, name: str = None, calories: int = None):
        """
        Конструктор класса Dessert

        :param name: название десерта (необязательно)
        :param calories: количество калорий (необязательно)
        """
        self._name = name
        self._calories = calories

    @property
    def name(self):
        """Возвращает название десерта"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        """
        Проверяет, является ли десерт высококалорийным

        :return: True если калорийность менее 200, иначе False
        """

        return isinstance(self._calories, int) and self._calories < 200

    @staticmethod
    def is_delicious():
        """
        Проверяет, является ли десерт вкусным.

        :return: Всегда True (все десерты вкусные)
        """
        return True

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f"Dessert(name='{self._name}', calories={self._calories})"

    def __repr__(self) -> str:
        """Представление объекта для отладки."""
        return f"Dessert(name={repr(self._name)}, calories={repr(self._calories)})"
