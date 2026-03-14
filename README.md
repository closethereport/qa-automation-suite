# QA Automation Suite

![CI](https://github.com/closethereport/qa-automation-suite/actions/workflows/tests.yml/badge.svg)

Проект по автоматизации тестирования: UI, API и нагрузочные тесты.

## Стек

| Тип | Инструмент |
|-----|-----------|
| UI тесты | Playwright + Pytest |
| API тесты | Requests + Pytest |
| Нагрузочные тесты | Locust |
| Отчёты | pytest-html |
| CI/CD | GitHub Actions |

## Структура проекта

```
qa-automation-suite/
├── ui_tests/
│   ├── pages/
│   └── tests/
├── api_tests/
│   └── tests/
├── load_tests/
│   └── locustfile.py
├── .github/workflows/
├── conftest.py
└── requirements.txt
```

## Приложения под тестами

- **UI:** [SauceDemo](https://www.saucedemo.com) — демо-магазин
- **API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — демо REST API

## Установка и запуск

```bash
git clone https://github.com/closethereport/qa-automation-suite.git
cd qa-automation-suite
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
```

### Запуск тестов

```bash
# API тесты
pytest api_tests/ -v

# UI тесты
pytest ui_tests/ -v

# С HTML-отчётом
pytest api_tests/ -v --html=reports/report.html --self-contained-html
```

### Нагрузочные тесты

```bash
locust -f load_tests/locustfile.py
# Открыть http://localhost:8089
```

## CI/CD

Пайплайн состоит из трёх уровней: сначала запускаются smoke тесты, и только после их успешного прохождения — полные API и UI тесты параллельно. Отчёты сохраняются как артефакты в каждом запуске.
