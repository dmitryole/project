from flask import Flask, render_template
from .get_status_jira import status_jira
from .model import db, Fields


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    """Инициализируем БД"""
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Микросервис отчетов Jira"
        filds_list = Fields.query.order_by(Fields.id.desc()).all()
        status = status_jira()
        """Передаем значения переменных на фронт"""
        return render_template('index.html', page_title=title, filds_list=filds_list, status=status)
    return app

"""Команда запуска приложения: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run"""

"""Результат: фрон запустился, но не отобразились атрибуты поля"""