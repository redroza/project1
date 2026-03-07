from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.
    Пример: "MasterCard 7158300734726758" → "MasterCard 7158 30** **** 6758"
    Пример: "Счет 73654108430135874305" → "Счет **4305"
    """
    # Находим последний пробел, чтобы отделить название от номера
    last_space_index = data.rfind(' ')

    if last_space_index == -1:
        return data  # Если нет пробелов, возвращаем как есть

    # Разделяем на название и номер
    name = data[:last_space_index].strip()
    number = data[last_space_index + 1:].replace(" ", "")

    # Определяем тип и маскируем
    if len(number) == 16:
        # Карта
        masked_number = get_mask_card_number(number)
    elif len(number) == 20:
        # Счет
        masked_number = get_mask_account(number)
    else:
        # Если длина не подходит ни под карту, ни под счет
        return data

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат "ДД.ММ.ГГГГ".

    Args:
        date_string: Строка с датой в формате "2024-03-11T02:26:18.671407"

    Returns:
        Строка с датой в формате "ДД.ММ.ГГГГ"
    """
    # Удаляем часть с микросекундами, если она есть
    if '.' in date_string:
        date_string = date_string.split('.')[0]

    # Парсим строку в объект datetime
    dt = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

    # Форматируем в нужный формат
    return dt.strftime("%d.%m.%Y")
