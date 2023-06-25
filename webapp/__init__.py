import logging
from flask import Flask, render_template
from flask_migrate import Migrate
from .get_status_jira import status_jira
from .db import db
from .fields.models import Fields

""" Конфигурация логов """
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
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        title = "Микросервис отчетов Jira"
        status = status_jira()
        feilds_list = Fields.query.filter(Fields.field_status_del == 0
                                          ).order_by(Fields.id.desc()).all()
        """Передаем значения переменных на фронт"""
        return render_template(
            'base.html',
            page_title=title,
            feilds_list=feilds_list,
            status=status)
    logging.info("Сервис запустился")
    return app
