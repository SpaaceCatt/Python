# BankProject

## Цель проекта

BankProject — учебный проект на Python для работы с банковскими операциями.

В проекте реализованы функции для:

* маскирования номеров банковских карт и счетов;
* обработки банковских операций;
* фильтрации операций по статусу;
* сортировки операций по дате.

## Установка

Для работы с проектом необходимо установить Python и Poetry.

Клонируйте репозиторий:

```bash
git clone <ссылка-на-репозиторий>
```

Перейдите в директорию проекта:

```bash
cd BankProject
```

Установите зависимости:

```bash
poetry install
```

Активируйте виртуальное окружение:

```bash
poetry shell
```

## Использование

### Фильтрация операций

Функция `filter_by_state()` принимает список словарей и необязательный параметр `state`.

По умолчанию используется значение `"EXECUTED"`.

```python
from src.processing import filter_by_state

operations = [
    {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
    {"state": "CANCELED", "date": "2024-03-10T01:15:30.123456"},
    {"state": "EXECUTED", "date": "2024-03-12T12:00:00.000000"},
]

result = filter_by_state(operations)

print(result)
```

Результат:

```text
[
    {'state': 'EXECUTED', 'date': '2024-03-11T02:26:18.671407'},
    {'state': 'EXECUTED', 'date': '2024-03-12T12:00:00.000000'}
]
```

Можно указать другое состояние:

```python
result = filter_by_state(operations, "CANCELED")

print(result)
```

Результат:

```text
[
    {'state': 'CANCELED', 'date': '2024-03-10T01:15:30.123456'}
]
```

### Сортировка операций

Функция `sort_by_date()` сортирует список словарей по ключу `date`.

По умолчанию используется сортировка по убыванию:

```python
from src.processing import sort_by_date

result = sort_by_date(operations)

print(result)
```

Сортировка по возрастанию:

```python
result = sort_by_date(operations, descending=False)

print(result)
```

Параметр `descending`:

* `True` — от самой поздней даты к самой ранней;
* `False` — от самой ранней даты к самой поздней.

## Проверка качества кода

Для проверки кода используются:

```bash
poetry run black .
poetry run isort .
poetry run flake8 .
poetry run mypy .
```

## Технологии

* Python
* Poetry
* Black
* isort
* Flake8
* mypy
