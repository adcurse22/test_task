Проект "Вычисление рабочего времени водителя"
Приветствуем вас в проекте "Вычисление рабочего времени водителя"! Этот проект представляет собой реализацию функционала для вычисления рабочего времени водителя на основе данных, хранящихся в модели DriverLog при использовании фреймворков Django, Django REST framework (DRF) и Django ORM.

Установка
Клонируйте репозиторий с GitHub:
bash
Copy code
git clone https://github.com/adcurse22/test_task.git
Перейдите в папку проекта:
bash
Copy code
cd test_task
Создайте виртуальное окружение и активируйте его:
bash
Copy code
python -m venv venv
source venv/bin/activate   # Для Windows: venv\Scripts\activate
Установите зависимости:
bash
Copy code
pip install -r requirements.txt
Создайте файл .env в корневой папке проекта и добавьте необходимые переменные окружения:
env
Copy code
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
SECRET_KEY=your_secret_key
Выполните миграции:
bash
Copy code
python manage.py migrate
Запустите сервер:
bash
Copy code
python manage.py runserver
Использование
Проект предоставляет API для вычисления рабочего времени водителя за день и за неделю на основе данных, хранящихся в модели DriverLog. Вы можете использовать следующий эндпоинт:

GET /driver-working-time/<int:driver_id>/ - Получить данные о рабочем времени водителя за день и за неделю.
Тестирование
Для запуска тестов используйте следующую команду:

bash
Copy code
python manage.py test driver
Вклад
Если вы обнаружите ошибки или хотите внести улучшения, будем рады вашим Pull Request'ам.

Лицензия
Проект лицензирован в соответствии с условиями MIT License.

