def filter_by_state(data: list[dict[str, any]], state: str = "EXECUTED") -> list[dict[str, any]]:
    """Возвращает список словарей с указанным состоянием."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список операций по дате."""
    return sorted(data, key=lambda operation: operation["date"], reverse=reverse)
