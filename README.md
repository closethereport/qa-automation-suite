# QA Automation Suite

![CI](https://github.com/closethereport/qa-automation-suite/actions/workflows/tests.yml/badge.svg)

Фреймворк для автоматизации тестирования: UI, API и нагрузочные тесты.

## Стек

| Тип | Инструмент |
|-----|-----------|
| UI тесты | Playwright + Pytest |
| API тесты | Requests + Pytest |
| Нагрузочные тесты | Locust |
| Отчёты | pytest-html |
| CI/CD | GitHub Actions |

## Возможности

- **Page Object Model** — UI тесты с разделением логики и локаторов
- **API клиент с логированием** — все запросы и ответы пишутся в лог
- **Маркеры** `smoke` / `regression` — запускай только нужный набор тестов
- **Мультиокружение** — запуск на dev, staging или prod через `--env`
- **Retry** — автоматический перезапуск нестабильных тестов
- **Скриншоты при падении** — Playwright сохраняет скриншот при каждом упавшем UI тесте
- **Тесты времени ответа** — проверка что API отвечает в пределах допустимого

## Структура проекта

```
qa-automation-suite/
├── ui_tests/
│   ├── pages/
│   └── tests/
├── api_tests/
│   ├── client.py
│   └── tests/
├── load_tests/
│   └── locustfile.py
├── .github/workflows/
├── conftest.py
└── requirements.txt
```

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
# Все тесты
pytest

# Только smoke
pytest -m smoke

# Только regression
pytest -m regression

# На конкретном окружении
pytest --env=staging

# Только API или UI
pytest api_tests/ -v
pytest ui_tests/ -v
```

### Нагрузочные тесты

```bash
locust -f load_tests/locustfile.py
# Открыть http://localhost:8089
```

## CI/CD

Пайплайн состоит из трёх уровней: сначала запускаются smoke тесты, и только после их успешного прохождения — полные API и UI тесты параллельно. Отчёты сохраняются как артефакты в каждом запуске.
