# Kittygram Backend

REST API для платформы Kittygram — сервиса публикации котиков с **системой тегов** и поиском похожих питомцев.

## Стек технологий

- **Python 3.11**, **Django 6.0.5**, **Django REST Framework 3.16**
- **Аутентификация**: Token (djoser)
- **Документация**: Postman-коллекция (планируется)
- **БД**: SQLite (dev)

## Функциональность

- Регистрация и аутентификация пользователей.
- Полноценный CRUD для карточек котиков с загрузкой фотографий (Base64).
- **Система тегов настроения/характера:**
  - CRUD тегов доступен только администраторам.
  - Просмотр списка тегов доступен всем.
- **Назначение тегов котикам** (через админ-панель).
- Фильтрация списка котиков по тегам (`?tags__slug=...`).
- Эндпоинт «похожие коты» (`/cats/{id}/similar/`) на основе общих тегов.

## Как запустить локально

1. **Клонируйте репозиторий и перейдите в него:**
    ```bash
    git clone https://github.com/anasstasiakusch-tech/-.git
    cd -
## 2. Функциональность

- Регистрация и аутентификация пользователей.
- Полноценный CRUD для карточек котиков с загрузкой фотографий (Base64).
- **Система тегов настроения/характера:**
  - CRUD тегов доступен только администраторам.
  - Просмотр списка тегов доступен всем.
- **Назначение тегов котикам** (через админ-панель).
- Фильтрация списка котиков по тегам (`?tags__slug=...`).
- Эндпоинт «похожие коты» (`/cats/{id}/similar/`) на основе общих тегов.

## 3. Как запустить локально

1. **Клонируйте репозиторий и перейдите в него:**
    ```bash
    git clone https://github.com/anasstasiakusch-tech/-.git
    cd -

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    
   # Для Windows: venv\Scripts\activate
3. **Установка зависимостей:** 
   ```bash                                                                                                                  pip install -r requirements.txt   
4. **Настройка переменных окружения:** 
  Скопируйте .env.example в .env
   # Windows 
  copy .env.example .env
  # Mac/Linux
  cp .env.example .env
  При необходимости отредактируйте файл .env.  
5. **Миграции и создание суперпользователя:**                                                                            ```bash
 python manage.py migrate
 python manage.py createsuperuser
 

## Запуск через Docker
**Скопируйте .env.example в .env:**
bash
cp .env.example .env
Соберите и запустите контейнер:
bash
docker-compose up --build
API будет доступно по адресу: http://localhost:8000/api/

## Документация
Артефакт	Ссылка
Postman-коллекция	postman/My Collection.postman_collection.json
Диаграмма вариантов использования	docs/use_case_diagram.png
Диаграмма развёртывания	docs/deployment_diagram.png
Скриншоты тестирования	screenshots/

## API эндпоинты
**Аутентификация:**
Метод	URL	Описание
POST	/api/users/	Регистрация нового пользователя.
POST	/api/auth/token/login/	Получение токена аутентификации.
**Котики:**
Метод	URL	Описание	Auth
GET	/api/cats/	Список котиков (с пагинацией, фильтрацией по тегам).	Нет
POST	/api/cats/	Создать котика (владелец назначается автоматически).	Да
GET	/api/cats/{id}/	Детальная информация о котике (включая его теги).	Нет
PATCH	/api/cats/{id}/	Частичное обновление (только владелец).	Да
DELETE	/api/cats/{id}/	Удалить котика (только владелец).	Да
GET	/api/cats/{id}/similar/	Похожие котики (на основе общих тегов).	Нет
**Теги:**
Метод	URL	Описание	Auth
GET	/api/tags/	Список всех тегов.	Нет
GET	/api/tags/{id}/	Информация о конкретном теге.	Нет
POST	/api/tags/	Создать новый тег (генерация slug из названия).	Админ
PUT/PATCH	/api/tags/{id}/	Изменить тег (slug перегенерируется).	Админ
DELETE	/api/tags/{id}/	Удалить тег (связи с котами удалятся каскадно).	Админ
**Достижения:**
Метод	URL	Описание
GET	/api/achievements/	Список достижений.

## Примеры запросов
1. **Получение токена:**
bash
curl -X POST http://127.0.0.1:8000/api/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
Ответ:
json
{"auth_token": "abc123..."}
2. **Создание тега администратором:**
bash
curl -X POST http://127.0.0.1:8000/api/tags/ \
  -H "Authorization: Token abc123..." \
  -H "Content-Type: application/json" \
  -d '{"name": "ласковый"}'
Ответ:
json
{"id": 1, "name": "ласковый", "slug": "laskovyi"}
3. **Фильтрация котиков по тегу «ласковый»:**
bash
curl http://127.0.0.1:8000/api/cats/?tags__slug=laskovyi
Ответ:
json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [...]
}
4. **Похожие котики для кота с id = 1:**
bash
curl http://127.0.0.1:8000/api/cats/1/similar/
Ответ:
json
[
    {"id": 2, "name": "Пушистик", ...}
]

## Скриншоты тестирования
**Скриншоты запросов и ответов (успешные и ошибочные) находятся в папке screenshots/.**
## Лицензия
**Учебный проект. Не предназначен для коммерческого использования.**
## Контакты
**GitHub: anasstasiakusch-tech
Email: anasstasiakusch@gmail.com**
