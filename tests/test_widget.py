import pytest
from src.widget import mask_account_card, get_date


class TestMaskAccountCard:
    """Тесты для функции маскировки карт и счетов"""

    @pytest.mark.parametrize("input_data,expected", [
        ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
        ("MasterCard 5555555555554444", "MasterCard 5555 55** **** 4444"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 4111111111111111", "Visa Platinum 4111 11** **** 1111"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ])
    def test_valid_input(self, input_data, expected):
        """Тестирование правильности маскировки для различных типов карт и счетов"""
        assert mask_account_card(input_data) == expected

    def test_input_with_extra_spaces(self):
        """Тестирование входных данных с лишними пробелами"""
        assert mask_account_card("  Visa   1234567890123456  ") == "  Visa   1234567890123456  "
        assert mask_account_card("Счет   73654108430135874305  ") == "Счет   73654108430135874305  "

    @pytest.mark.parametrize("input_data,expected", [
        ("", ""),
        ("Просто текст без номера", "Просто текст без номера"),
        ("12345678", "12345678"),
        ("Visa 1234", "Visa 1234"),
        ("Счет 1234567890", "Счет 1234567890"),  # Слишком короткий для счета
    ])
    def test_invalid_input(self, input_data, expected):
        """Тестирование обработки некорректных входных данных"""
        assert mask_account_card(input_data) == expected

    def test_mixed_card_and_account(self):
        """Тестирование с данными, похожими и на карту, и на счет"""
        # Номер длиной 16 символов, но это может быть счет
        assert mask_account_card("Счет 1234567890123456") == "Счет 1234 56** **** 3456"
        # Номер длиной 20 символов, но это может быть карта
        assert mask_account_card("Visa 12345678901234567890") == "Visa **7890"

    def test_none_input(self):
        """Тестирование обработки None"""
        with pytest.raises(AttributeError):
            mask_account_card(None)


class TestGetDate:
    """Тесты для функции преобразования даты"""

    @pytest.mark.parametrize("input_date,expected", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
        ("2000-01-01T00:00:00", "01.01.2000"),
    ])
    def test_valid_dates(self, input_date, expected):
        """Тестирование правильности преобразования даты"""
        assert get_date(input_date) == expected

    def test_date_without_time(self):
        """Тестирование даты без временной части (ожидаем ошибку)"""
        with pytest.raises(ValueError):
            get_date("2024-03-11")

    def test_date_with_microseconds(self, sample_dates):
        """Тестирование даты с микросекундами"""
        result = get_date(sample_dates['standard'])
        assert result == "11.03.2024"

    def test_date_without_microseconds(self, sample_dates):
        """Тестирование даты без микросекунд"""
        result = get_date(sample_dates['without_microseconds'])
        assert result == "11.03.2024"

    @pytest.mark.parametrize("invalid_date", [
        "",  # Пустая строка
        "2024-13-11T02:26:18",  # Несуществующая дата
        "11/03/2024",  # Неправильный формат
        "invalid_date",  # Строка без даты
        "2024-03-11 02:26:18",  # Неправильный разделитель
    ])
    def test_invalid_dates(self, invalid_date):
        """Тестирование обработки некорректных форматов дат"""
        with pytest.raises(ValueError):
            get_date(invalid_date)

