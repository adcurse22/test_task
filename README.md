<div align="center">
  <h1>Проект "Вычисление рабочего времени водителя"</h1>
  <p>Реализация функционала для вычисления рабочего времени водителя на основе данных, хранящихся в модели DriverLog.</p>
</div>

## Оглавление

- [Установка](#установка)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Вклад](#вклад)
- [Лицензия](#лицензия)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/adcurse22/test_task.git
   
   cd test_task
Создайте и активируйте виртуальное окружение:
  ```bash

python -m venv venv
source venv/bin/activate   # Для Windows: venv\Scripts\activate
   ```
Установка зависимостей

   ```
pip install -r requirements.txt
```
Выполните Миграции

   ```bash
py manage.py migrate

   ```
Запустите сервер

   ```
py manage.py runserver
   ```
Использование
Проект предоставляет API для вычисления рабочего времени водителя за день и за неделю на основе данных, хранящихся в модели DriverLog. Используйте эндпоинт:

GET /driver-working-time/<int:driver_id>/ - Получить данные о рабочем времени водителя за день и неделю.

## Тестирование 
```
py manage.py test driver 



