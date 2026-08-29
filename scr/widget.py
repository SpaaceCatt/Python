from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Маскирует номер карты или счёта"""
    parts = card_number.rsplit(" ", 1)

    name = parts[0]
    number = parts[1]

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")
