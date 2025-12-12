class WrongNumberOfPlayersError(Exception):
    """Исключение для неправильного количества игроков"""
    pass


class NoSuchStrategyError(Exception):
    """Исключение для неправильной стратегии"""
    pass


def rps_game_winner(players: list) -> str:
    """
     Определяет победителя в игре Камень-Ножницы-Бумага

    :param players: список игроков в формате [['имя1', 'ход1'], ['имя2', 'ход2']]
    :return: строка 'имя ход' победителя
    :raise WrongNumberOfPlayersError: если количество игроков != 2
    :raise NoSuchStrategyError: если ход не 'R', 'P' или 'S'
    """

    if len(players) != 2:
        raise WrongNumberOfPlayersError(f'Ожидается 2 игрока, получено {len(players)}')

    valid_moves = ('R', 'P', 'S')

    p1, p1_move = players[0]
    p2, p2_move = players[1]

    if p1_move not in valid_moves:
        raise NoSuchStrategyError(f'Недопустимый ход игрока 1: "{p1_move}"')
    elif p2_move not in valid_moves:
        raise NoSuchStrategyError(f"Недопустимый ход игрока 2: '{p2_move}'")

    if p1_move == p2_move:
        return f'{p1} {p1_move}'

    winning_combinations: dict[str, str] = {
        'R': 'S',  # Камень бьет ножницы
        'S': 'P',  # Ножницы бьют бумагу
        'P': 'R'  # Бумага бьет камень
    }

    if winning_combinations[p1_move] == p2_move:
        return f'{p1} {p1_move}'
    else:
        return f'{p2} {p2_move}'
