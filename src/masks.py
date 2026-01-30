def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX"""
    # Удаляем пробелы, если они есть
    card_number = card_number.replace(" ", "")

    # Проверяем длину номера карты
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Форматируем номер карты
    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формате **XXXX"""
    # Удаляем пробелы, если они есть
    account_number = account_number.replace(" ", "")

    # Проверяем длину номера счета
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать минимум 20 цифр")

    # Форматируем номер счета
    masked = f"**{account_number[-4:]}"
    return masked
