# QA Automation Suite

Комплексный проект по автоматизации тестирования, покрывающий UI, API и нагрузочное тестирование.

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
│   ├── pages/          # Page Object Model
│   └── tests/          # UI тест-кейсы
├── api_tests/
│   └── tests/          # API тест-кейсы
├── load_tests/
│   └── locustfile.py   # Сценарии нагрузочного тестирования
├── .github/workflows/  # CI/CD пайплайн
├── conftest.py         # Общие фикстуры
└── requirements.txt    # Зависимости
```

## Приложения под тестами

- **UI:** [SauceDemo](https://www.saucedemo.com) — демо-магазин
- **API:** [ReqRes](https://reqres.in) — демо REST API

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/<your-username>/qa-automation-suite.git
cd qa-automation-suite
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

### 3. Настроить переменные окружения

```bash
cp .env.example .env
```

### 4. Запустить тесты

```bash
# Все тесты
pytest

# Только API тесты
pytest api_tests/ -v

# Только UI тесты
pytest ui_tests/ -v

# С HTML-отчётом
pytest api_tests/ -v --html=reports/report.html --self-contained-html
```

### 5. Запустить нагрузочные тесты

```bash
locust -f load_tests/locustfile.py
# Открыть http://localhost:8089
```

## CI/CD

При каждом пуше в `main` автоматически запускаются API и UI тесты через GitHub Actions.
Отчёты доступны во вкладке **Actions → Artifacts**.
