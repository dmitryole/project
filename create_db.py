from webapp import db, create_app

"""Инициализируем создание модели"""
db.create_all(app=create_app())

"""Результат: создалась ББ jira.bd и таблица fields"""