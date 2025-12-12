from datetime import datetime, timedelta


def date_in_future(days: int) -> str:
    """
    Возвращает дату через указанное количество дней
    Если days не является целым числом, возвращает текущую дату

    :param days: количество дней
    :return: строка с датой в формате 'DD-MM-YYYY HH:MM:SS'
    """

    current_date = datetime.now()

    if type(days) is not int:
        return current_date.strftime('%d-%m-%Y %H:%M:%S')

    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')
