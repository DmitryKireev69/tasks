def max_odd(lst: list) -> int | None:
    """
    Находит максимальный нечётный числовой элемент в массиве

    :param lst: Список элементов
    :return: Максимальный нечётный элемент int или None
    """

    odd_num = list((i for i in lst if isinstance(i, (int, float)) and int(i) % 2 != 0))

    if not odd_num:
        return None
    return int(max(odd_num))
