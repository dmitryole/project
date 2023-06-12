from webapp import create_app
from webapp.get_fields_jira import get_filds_id_and_name

"""Инициализируем заполнение таблицы fields"""
app = create_app()
with app.app_context():
    get_filds_id_and_name()

"""Результат: В таблица fields заполнилась данными"""