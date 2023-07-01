from flask import Flask
import logging

from webapp.filter.views import blueprint as search_blueprint

# Конфигурация логов
logging.basicConfig(filename='project.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO,
                    encoding='utf-8')


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(search_blueprint)

    logging.info("Сервис запустился")
    return app
