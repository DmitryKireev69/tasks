import re
from collections import Counter


def count_words(string: str) -> dict[str, int]:
    """
    Возвращает словарь со статистикой частоты употребления слов

    :param string: входная строка (может быть любого типа)
    :return: словарь {слово: количество_вхождений}
    """
    if not isinstance(string, str):
        return {}
    pattern = r"\b[a-zа-яё]+(?:'[a-zа-яё]+)?(?:-[a-zа-яё]+)?\b"
    return dict(Counter(re.findall(pattern, string.lower())))
