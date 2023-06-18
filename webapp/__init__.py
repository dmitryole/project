import logging
from flask import Flask, render_template
from .get_status_jira import status_jira
from .model import db, Fields

# Конфигурация логов
logging.basicConfig(filename='project.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO,
                    encoding='utf-8')

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    """Инициализируем БД"""
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Микросервис отчетов Jira"
        feilds_list = Fields.query.order_by(Fields.id.desc()).all()
        status = status_jira()
        """Передаем значения переменных на фронт"""
        return render_template('index.html', page_title=title, feilds_list=feilds_list, status=status)
    
    logging.info("Сервис запустился")
    return app

"""Команда запуска приложения: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run"""

"""Результат: фрон запустился"""