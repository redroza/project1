import pytest


@pytest.fixture
def sample_card_numbers():
    """Фикстура с различными номерами карт для тестирования"""
    return {
        'valid': '1234567890123456',
        'valid_with_spaces': '1234 5678 9012 3456',
        'visa': '4111111111111111',
        'mastercard': '5555555555554444',
        'short': '1234567890',
        'long': '12345678901234567890',
        'empty': '',
        'with_chars': '1234abcd5678efgh'
    }


@pytest.fixture
def sample_account_numbers():
    """Фикстура с различными номерами счетов для тестирования"""
    return {
        'valid': '12345678901234567890',
        'valid_with_spaces': '1234 5678 9012 3456 7890',
        'short': '1234567890',
        'long': '123456789012345678901234',
        'empty': '',
        'with_chars': '1234abcd5678efgh9012'
    }


@pytest.fixture
def sample_card_data():
    """Фикстура с различными данными карт и счетов для mask_account_card"""
    return [
        ('Visa Classic 1234567890123456', 'Visa Classic 1234 56** **** 3456'),
        ('MasterCard 5555555555554444', 'MasterCard 5555 55** **** 4444'),
        ('Счет 12345678901234567890', 'Счет **7890'),
        ('Visa Platinum 4111111111111111', 'Visa Platinum 4111 11** **** 1111'),
        ('Maestro 1234567890123456', 'Maestro 1234 56** **** 3456'),
    ]


@pytest.fixture
def sample_dates():
    """Фикстура с различными форматами дат"""
    return {
        'standard': '2024-03-11T02:26:18.671407',
        'without_microseconds': '2024-03-11T02:26:18',
        'future': '2025-12-31T23:59:59.999999',
        'past': '2000-01-01T00:00:00.000000',
        'invalid': '2024-13-11T02:26:18',
        'empty': '',
        'wrong_format': '11/03/2024'
    }


@pytest.fixture
def sample_transactions():
    """Фикстура со списком транзакций для тестирования функций фильтрации и сортировки"""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-01T10:30:00'},
        {'id': 2, 'state': 'PENDING', 'date': '2024-03-02T15:45:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-03-03T09:15:00'},
        {'id': 4, 'state': 'CANCELLED', 'date': '2024-03-04T18:20:00'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2024-03-05T12:00:00'},
    ]


@pytest.fixture
def sample_transactions_same_dates():
    """Фикстура с транзакциями, имеющими одинаковые даты"""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-01T10:30:00'},
        {'id': 2, 'state': 'PENDING', 'date': '2024-03-01T10:30:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-03-01T10:30:00'},
    ]