# Compas-pro тестовое задание.

Запуск проекта
----------
1. Клонируйте репозиторий, наберите в командной строке:
```bash
git clone 'git@github.com:valeriy-kirichenko/compaspro_test_task.git'
```
2. Переместитесь в папку /infra, создайте там файл .env и заполните его данными:
```bash
cd compaspro_test_task/test_task/infra/
touch .env
nano .env
... # .env
# Настройки проекта
SECRET_KEY= # Секретный ключ Django пректа
DEBUG=1 # Режим отладки

# Настройки БД
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER= # Придумайте имя пользователя
POSTGRES_PASSWORD= # Придумайте пароль
DB_HOST=db
DB_PORT=5432

# Настройки Redis
REDIS_HOST = redis
REDIS_PORT = 6379

# Настройки для создания суперпользователя
DJANGO_SUPERUSER_USERNAME = # Придумайте имя пользователя
DJANGO_SUPERUSER_PASSWORD = # Придумайте пароль

... # сохраните (Ctl + x)
```
3. Не выходя из /infra выполните команду:
```bash
docker-compose up -d --build
```
4. При желании можно создать 3 пользователей 
(User, Manager и CRM-admin), для этого необходимо выполнить команду:
```bash
 docker-compose exec web python manage.py create_users
```
----------
Автор:
----------
* **Кириченко Валерий Михайлович**
GitHub - [valeriy-kirichenko](https://github.com/valeriy-kirichenko)