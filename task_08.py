from functools import reduce


def multiply_numbers(inputs: any = None) -> int | None:
    """
    Возвращает произведение цифр, входящих в inputs
    :param inputs: любой тип данных, содержащий цифры
    :return: произведение цифр или None, если цифр нет
    """

    if inputs is None:
        return None

    digits = [int(i) for i in str(inputs) if i.isdigit()]

    if not digits:
        return None

    return reduce(lambda x, y: x * y, digits, 1)
