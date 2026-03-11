from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_masked = mask_account_card("MasterCard 7158300734726758")
print(card_masked)

date_formatted = get_date("2023-12-31T23:59:59.999999")
print(date_formatted)

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Сначала фильтруем по статусу, потом сортируем
executed_and_sorted = sort_by_date(filter_by_state(operations))
print("Выполненные транзакции, отсортированные по дате:")
for op in executed_and_sorted:
    print(f"{op['date']}: {op['state']} - ID {op['id']}")
