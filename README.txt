Инструкция: Как запустить Django-проект (карточка риска)

1. Установи Python 3.10 или выше (если будешь запускать локально).
2. Установи зависимости:
   pip install -r requirements.txt

3. Запусти миграции:
   python manage.py migrate

4. Запусти сервер:
   python manage.py runserver

5. Перейди в браузер: http://127.0.0.1:8000/api/risks/

Если хочешь загрузить проект на Render:
1. Создай репозиторий на GitHub
2. Загрузи туда все файлы из этой папки
3. На Render укажи:
   - Build command: pip install -r requirements.txt
   - Start command: gunicorn risk_project.wsgi:application
   - Python version: 3.10