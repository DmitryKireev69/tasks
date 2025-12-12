def connect_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    """
    Соединяет два словаря по определенным правилам:
    1. Приоритетный словарь определяется по сумме значений
    2. Удаляются ключи со значениями < 10
    3. Результат сортируется по значениям в порядке возрастания

    :param dict1: первый словарь
    :param dict2: второй словарь
    :return: объединенный и отсортированный словарь
    """

    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    priority_dict = dict2 if sum2 >= sum1 else dict1
    secondary_dict = dict1 if priority_dict is dict2 else dict2

    result = {}

    for key, value in priority_dict.items():
        if value >= 10:
            result[key] = value

    for key, value in secondary_dict.items():
        if value >= 10 and key not in result:
            result[key] = value

    return dict(sorted(result.items(), key=lambda item: item[1]))
