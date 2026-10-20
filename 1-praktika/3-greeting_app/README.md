# Приветствие на Django (кейс-задача № 3)

Веб-приложение: пользователь вводит имя, оно сохраняется в БД и показывается на главной странице как приветствие.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations greetings
python manage.py migrate
python manage.py runserver
```

Открыть: http://127.0.0.1:8000/

## Что реализовано
- Модель `UserName` с единственным полем `name`.
- Форма ввода имени и кнопка Submit.
- Сохранение имени в БД и вывод приветствия на главной странице.
- Обработка ошибок: пустое поле (в том числе из одних пробелов) и слишком длинное имя.
- Стилизация через CSS.
- Защита от CSRF: `CsrfViewMiddleware` и `{% csrf_token %}` в форме.
