[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19940492&assignment_repo_type=AssignmentRepo)
# [Мини-проект «Заметки»](https://github.com/Solva-technology/django-notes-orm-aishabay.git)
## Author: [Aisha](https://www.linkedin.com/in/aisha-zhumagul/) | Python Developer
## Stack / Technologies used:
- Python, Django
- PostgreSQL
- Docker, Docker Compose

## Project Description
Это веб-приложение для ведения заметок, реализованное на Django с использованием PostgreSQL и Docker. Пользователи могут создавать заметки, указывать их статус и категории, а также просматривать списки заметок и профили пользователей. Интерфейс отображения данных построен с использованием Django ORM и шаблонов, с оптимизацией запросов с помощью select_related и prefetch_related. Проект поддерживает локализацию и административную панель.

## Instruction to launch
1. Введите в терминале
```
git clone git@github.com:Solva-technology/django-notes-orm-aishabay.git
```

2. Перейдите в директорию данного проекта
```
cd django-notes-orm-aishabay
```

3. Убедитесь что Docker запущен.
```
docker version
```

4. Добавьте `.env` файл в проект
#### Пример .env файла:
```
POSTGRES_DB=notes_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

TIMEZONE=Asia/Almaty
LANGUAGE=ru-ru
```

5. Создайте и запустите контейнеры
```
docker compose up -d
```

6. Загрузите данные из фикстуры `dump.json` в базу данных
```
docker compose exec web python3 manage.py loaddata fixtures/dump.json
```

7. Перейдите по адресу `http://localhost:8000/admin` в браузере.
Введите имя пользователя ```root``` и пароль ```root``` чтобы войти в админку.
Здесь вы можете добавить/изменить/удалить данные.

8. 🔗 Ссылки проекта

| Назначение                                  | Ссылка                                               |
|--------------------------------------------|------------------------------------------------------|
| Главная страница со всеми заметками        | [http://localhost:8000/](http://localhost:8000/)     |
| Список пользователей                        | [http://localhost:8000/users/](http://localhost:8000/users/) |
| Заметки категории `study`                  | [http://localhost:8000/notes/category/study/](http://localhost:8000/notes/category/study/) |
| Заметка с `id = 1`                             | [http://localhost:8000/notes/1/](http://localhost:8000/notes/1/) |
| Профиль пользователя с `id = 1`               | [http://localhost:8000/users/1/](http://localhost:8000/users/1/) |

8. Остановите и удалите контейнеры
```
docker compose down -v
```
