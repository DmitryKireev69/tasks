def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    """
    Группирует слова по анаграммам

    :param words_array: список слов для группировки
    :return: список групп анаграмм
    """

    anagram_groups = {}

    for word in words_array:
        anagram_groups.setdefault(''.join(sorted(word.lower())), []).append(word)

    return list(anagram_groups.values())
