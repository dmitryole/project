from flask import current_app
import logging
import requests


# Функция проверки статуса Jira
def status_jira():
    # Обработка ответа Jira
    try:
        # Запрос
        result = requests.get(current_app.config['JIRA_URL'])
        # Обработка сетевых ошибок
        result.raise_for_status()
        return {'bool': True,
                'text': 'Сервер Jira доступен'}
    # Обработка ошибок Jira
    except (ValueError):
        logging.info('Ошибка: Ошибка при на стороне сервиса')
        return {'bool': False,
                'text': 'Сервер Jira не доступна - обратитесь к ДЦС'}
    # Обработка ответа при отсутствии VPN
    except (requests.exceptions.ConnectionError):
        logging.info('Ошибка: Ошибка при на стороне пользователя')
        return {'bool': False,
                'text': 'Сервер Jira не доступна - проверте VPN'}


if __name__ == "__main__":
    print(status_jira())
