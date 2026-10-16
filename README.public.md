# Django_all_indicators

Обзор исходного кода для портфолио. Названия и структура авторских файлов сохранены.

Сайт на Django с графиками Bitcoin, индексом страха и жадности и сигналами стратегии EMA.

## Состав
```text
  manage.py
  requirements.txt
  App/__init__.py
  App/app2.py
  App/app3.py
  App/calculate_profit.py
  App/newapp.py
  App/plotly_charts.py
  App/views.py
  Django_all_indicators/__init__.py
  Django_all_indicators/asgi.py
  Django_all_indicators/settings.py
  Django_all_indicators/urls.py
  Django_all_indicators/wsgi.py
  static/css/style.css
  templates/page.html
```

## Публикация
Логика исходников не перерабатывалась. Чувствительные значения и пустые поля доступа обозначены `YOUR_...` / `REDACTED_SECRET_SET_IN_ENV`. Это заглушки, а не действующие доступы. Настройки через переменные окружения перечислены в `.env.example`, когда они есть в коде.

Окружения Python, сторонние библиотеки, базы данных, токены, журналы, обученные модели и массивы рыночных данных не включены. Это компактная копия для чтения; для запуска исторических проектов могут понадобиться собственные настройки, данные, модели и совместимые зависимости. Наличие requirements.txt не означает, что старые API проверены сегодня.

Сгенерированные HTML-графики со встроенной библиотекой Plotly также не включены: App/chart.html, templates/chart.html, templates/file_btc.html, templates/file_fear_and_greed.html. Их создают исходные Python-скрипты; визуальный результат доступен в галерее.

## Даты
Начало - сентябрь 2022. Изменения - октябрь-ноябрь 2022, январь и апрель 2023, декабрь 2025.

Скриншоты и описание находятся в каталоге портфолио. Видео будет добавлено отдельно.
