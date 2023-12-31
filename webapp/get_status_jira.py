import logging
import requests
from .config import STAGE_JIRA_URL

"""Функция проверки статуса Jira"""
def status_jira():
    # Обработка ответа при ответе Jira 
    try:
        # Запрос
        result = requests.get(STAGE_JIRA_URL)
        # Обработка сетевых ошибок
        result.raise_for_status()
        return 'Stage Jira доступен'
    # Обработка ошибок Jira
    except (ValueError):
        logging.info('Ошибка: Ошибка при на стороне сервиса')
        return 'Stage Jira не доступна - обратитесь к ДЦС'
    # Обработка ответа при отсутствии VPN
    except (requests.exceptions.ConnectionError):
        logging.info('Ошибка: Ошибка при на стороне пользователя')
        return 'Stage Jira не доступна - проверте VPN'

if __name__ == "__main__":
    print(status_jira())