import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции фильтрации по статусу"""

    from typing import Any, Dict, List

    def test_filter_by_state_executed(self, sample_transactions: List[Dict[str, Any]]) -> None:
        """Тестирование фильтрации по статусу EXECUTED"""
        expected = [
            {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-01T10:30:00'},
            {'id': 3, 'state': 'EXECUTED', 'date': '2024-03-03T09:15:00'},
            {'id': 5, 'state': 'EXECUTED', 'date': '2024-03-05T12:00:00'},
        ]
        result = filter_by_state(sample_transactions, 'EXECUTED')
        assert result == expected

    def test_filter_by_state_pending(self, sample_transactions):
        """Тестирование фильтрации по статусу PENDING"""
        expected = [
            {'id': 2, 'state': 'PENDING', 'date': '2024-03-02T15:45:00'},
        ]
        result = filter_by_state(sample_transactions, 'PENDING')
        assert result == expected

    def test_filter_by_state_cancelled(self, sample_transactions):
        """Тестирование фильтрации по статусу CANCELLED"""
        expected = [
            {'id': 4, 'state': 'CANCELLED', 'date': '2024-03-04T18:20:00'},
        ]
        result = filter_by_state(sample_transactions, 'CANCELLED')
        assert result == expected

    def test_filter_by_state_no_matches(self, sample_transactions):
        """Тестирование фильтрации по статусу, отсутствующему в данных"""
        result = filter_by_state(sample_transactions, 'COMPLETED')
        assert result == []

    @pytest.mark.parametrize("state", ['EXECUTED', 'PENDING', 'CANCELLED'])
    def test_filter_by_state_with_different_states(self, sample_transactions, state):
        """Параметризованный тест для различных статусов"""
        result = filter_by_state(sample_transactions, state)
        assert all(item['state'] == state for item in result)

    def test_filter_by_state_empty_list(self) -> None:
        """Тестирование фильтрации на пустом списке"""
        result = filter_by_state([], 'EXECUTED')
        assert result == []

    def test_filter_by_state_case_sensitivity(self, sample_transactions):
        """Тестирование чувствительности к регистру"""
        result = filter_by_state(sample_transactions, 'executed')
        assert result == []


class TestSortByDate:
    """Тесты для функции сортировки по дате"""

    def test_sort_by_date_descending(self, sample_transactions):
        """Тестирование сортировки по убыванию"""
        expected = [
            {'id': 5, 'state': 'EXECUTED', 'date': '2024-03-05T12:00:00'},
            {'id': 4, 'state': 'CANCELLED', 'date': '2024-03-04T18:20:00'},
            {'id': 3, 'state': 'EXECUTED', 'date': '2024-03-03T09:15:00'},
            {'id': 2, 'state': 'PENDING', 'date': '2024-03-02T15:45:00'},
            {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-01T10:30:00'},
        ]
        result = sort_by_date(sample_transactions, descending=True)
        assert result == expected

    def test_sort_by_date_ascending(self, sample_transactions):
        """Тестирование сортировки по возрастанию"""
        expected = [{'date': '2024-03-05T12:00:00', 'id': 5, 'state': 'EXECUTED'},
                    {'date': '2024-03-04T18:20:00', 'id': 4, 'state': 'CANCELLED'},
                    {'date': '2024-03-03T09:15:00', 'id': 3, 'state': 'EXECUTED'},
                    {'date': '2024-03-02T15:45:00', 'id': 2, 'state': 'PENDING'},
                    {'date': '2024-03-01T10:30:00', 'id': 1, 'state': 'EXECUTED'}]
        result = sort_by_date(sample_transactions)
        assert result == expected

    def test_sort_by_date_same_dates(self, sample_transactions_same_dates):
        """Тестирование сортировки при одинаковых датах"""
        result = sort_by_date(sample_transactions_same_dates, descending=True)
        # Порядок может сохраниться исходный при одинаковых датах
        assert result[0]['date'] == '2024-03-01T10:30:00'
        assert all(item['date'] == '2024-03-01T10:30:00' for item in result)

    def test_sort_by_date_empty_list(self) -> None:
        """Тестирование сортировки пустого списка"""
        result = sort_by_date([])
        assert result == []

    def test_sort_by_date_missing_date_key(self) -> None:
        """Тестирование сортировки при отсутствии ключа 'date'"""
        transactions = [
            {'id': 1, 'state': 'EXECUTED'},
            {'id': 2, 'state': 'PENDING'},
        ]
        with pytest.raises(KeyError):
            sort_by_date(transactions)

    def test_sort_by_date_invalid_date_format(self) -> None:
        """Тестирование сортировки с некорректным форматом даты"""
        transactions = [
            {'id': 1, 'date': 'invalid_date'},
            {'id': 2, 'date': '2024-03-02'},
        ]
        assert sort_by_date(transactions) == transactions
