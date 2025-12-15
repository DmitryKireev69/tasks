from task_11 import Dessert


class JellyBean(Dessert):
    """
    Класс желе-бобов, расширяющий Dessert.
    """

    def __init__(
            self,
            name: str = None,
            calories: int = None,
            flavor: str = None
    ):
        """
        Конструктор класса JellyBean

        :param name: название (необязательно)
        :param calories: калории (необязательно)
        :param flavor: вкус (необязательно)
        """
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self) -> str:
        """Возвращает вкус желе-бобов."""
        return self._flavor

    @flavor.setter
    def flavor(self, value: str):
        """Устанавливает вкус желе-бобов."""
        self._flavor = value

    def is_delicious(self) -> bool:
        """
        Проверяет, являются ли желе-бобы вкусными.
        Возвращает False только если flavor == "black licorice".
        """
        if not isinstance(self._flavor, str):
            return True

        return self._flavor.lower() != "black licorice"

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        base_str = super().__str__()
        flavor = self._flavor or "неизвестный вкус"
        return f"{base_str}, вкус: {flavor}"

    def __repr__(self) -> str:
        """Представление для отладки."""
        return (f"JellyBean(name={repr(self._name)}, "
                f"calories={repr(self._calories)}, "
                f"flavor={repr(self._flavor)})")




dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
dessert.name = "test_name"
print(dessert.name)
# test_name
dessert.name = "test_name2"
print(dessert.name)
# test_name2
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
# test_calories
dessert.calories = "test_calories2"
print(dessert.calories)
# test_calories2
if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
# True
if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.flavor = "test_flavor"
print(dessert.flavor)
# test_flavor
print(dessert.is_healthy())
#      ----------------------
# Fail
# '<' not supported between instances of 'str' and 'int'
# --== Task task_12.py failed tests ==--