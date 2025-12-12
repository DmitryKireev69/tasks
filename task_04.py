def sort_list(arr: list[int]) -> list[int]:
    """
    Обрабатывает список целых чисел, заменяя все минимальные элементы
    на максимальные и все максимальные элементы на минимальные, а затем
    добавляет одно минимальное значение в конец списка

    :param arr: список целых чисел
    :return: Обработанный список с выполненными заменами и добавленным
    минимальным значением в конец или пустой список
    """

    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr + [min_val]

    result = []
    for num in arr:
        if num == min_val:
            result.append(max_val)
        elif num == max_val:
            result.append(min_val)
        else:
            result.append(num)
    return result + [min_val]
