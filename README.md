# Blogicum

Учебный проект Яндекс Практикума (спринт 3) — блог на Django 5.2.

## Запуск

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py runserver
```

## Тесты и линтер

Из корня проекта:

```bash
pytest
flake8 blogicum
```
