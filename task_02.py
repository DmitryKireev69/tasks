def coincidence(lst: list[any] = None, rng: range = None) -> list[int | float]:
    """
    Возвращает элементы списка, значения которых попадают в указанный диапазон

    :param lst: список значений
    :param rng: числовой диапазон (range)
    :return: новый список из элементов lst, попадающих в rng или None
    """

    if lst is None or rng is None:
        return []

    first_num, last_num = rng.start, rng.stop
    return [i for i in lst if isinstance(i, (int, float)) and first_num <= i < last_num]
