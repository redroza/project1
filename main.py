from src.widget import mask_account_card, get_date

card_masked = mask_account_card("MasterCard 7158300734726758")
print(card_masked)

date_formatted = get_date("2023-12-31T23:59:59.999999")
print(date_formatted)
