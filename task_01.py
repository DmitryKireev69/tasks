def is_palindrome(value: any) -> bool:
    """
    Проверяет, является ли параметр палиндромом
    игнорирует пробелы, знаки препинания и регистр

    :param value: любой тип данных
    :return: True если строка палиндром, иначе False
    """
    clean_string = ''.join([s.lower() for s in str(value) if s.isalpha()])
    return clean_string == clean_string[::-1]
