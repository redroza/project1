import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты для функции маскировки номера карты"""

    @pytest.mark.parametrize("input_number,expected", [
        ("1234567890123456", "1234 56** **** 3456"),
        ("4111111111111111", "4111 11** **** 1111"),
        ("5555555555554444", "5555 55** **** 4444"),
    ])
    def test_valid_card_numbers(self, input_number, expected):
        """Тестирование правильности маскирования номера карты"""
        assert get_mask_card_number(input_number) == expected

    def test_card_number_with_spaces(self, sample_card_numbers):
        """Проверка работы функции с номерами, содержащими пробелы"""
        result = get_mask_card_number(sample_card_numbers['valid_with_spaces'])
        assert result == "1234 56** **** 3456"

    def test_card_number_boundary_values(self) -> None:
        """Тестирование граничных случаев"""
        # Минимальный допустимый номер
        with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
            get_mask_card_number("123456789012345")  # 15 цифр

        # Максимальный номер (ровно 16 цифр)
        result = get_mask_card_number("1234567890123456")
        assert result == "1234 56** **** 3456"

    @pytest.mark.parametrize("invalid_input", [
        "",  # Пустая строка
        "1234",  # Слишком короткий
        "12345678901234567890",  # Слишком длинный
        "abcdabcdabcdabcda",  # Буквы вместо цифр
        "1234 5678 90",  # Некорректный формат
    ])
    def test_invalid_card_numbers(self, invalid_input):
        """Проверка обработки некорректных номеров карт"""
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_input)

    def test_card_number_none_input(self) -> None:
        """Проверка обработки None (если функция ожидает строку)"""
        with pytest.raises(AttributeError):
            get_mask_card_number(None)


class TestGetMaskAccount:
    """Тесты для функции маскировки номера счета"""

    @pytest.mark.parametrize("input_number,expected", [
        ("12345678901234567890", "**7890"),
        ("40817810099910004356", "**4356"),
        ("73654108430135874305", "**4305"),
    ])
    def test_valid_account_numbers(self, input_number, expected):
        """Тестирование правильности маскирования номера счета"""
        assert get_mask_account(input_number) == expected

    def test_account_number_with_spaces(self, sample_account_numbers):
        """Проверка работы функции с номерами, содержащими пробелы"""
        result = get_mask_account(sample_account_numbers['valid_with_spaces'])
        assert result == "**7890"

    def test_account_number_boundary_values(self) -> None:
        """Тестирование граничных случаев"""
        # Минимальный допустимый номер
        with pytest.raises(ValueError, match="Номер счета должен содержать минимум 20 цифр"):
            get_mask_account("1234567890123456789")  # 19 цифр

        # Ровно 20 цифр
        result = get_mask_account("12345678901234567890")
        assert result == "**7890"

    @pytest.mark.parametrize("invalid_input", [
        "",  # Пустая строка
        "1234",  # Слишком короткий
        "1234567890",  # 10 цифр (слишком мало)
        "abcdabcdabcdabcdabcda",  # Буквы вместо цифр
        "1234 5678 90",  # Некорректный формат
    ])
    def test_invalid_account_numbers(self, invalid_input):
        """Проверка обработки некорректных номеров счетов"""
        with pytest.raises(ValueError):
            get_mask_account(invalid_input)

    def test_account_number_none_input(self) -> None:
        """Проверка обработки None"""
        with pytest.raises(AttributeError):
            get_mask_account(None)
