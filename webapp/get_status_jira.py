import logging
import requests
from .config import JIRA_URL


def status_jira():
    """Функция проверки статуса Jira"""
    """Обработка ответа при ответе Jira"""
    try:
        """Запрос"""
        result = requests.get(JIRA_URL)
        """Обработка сетевых ошибок"""
        result.raise_for_status()
        return 'Сервер Jira доступен'
    # Обработка ошибок Jira
    except (ValueError):
        logging.info('Ошибка: Ошибка при на стороне сервиса')
        return 'Сервер Jira не доступна - обратитесь к ДЦС'
    # Обработка ответа при отсутствии VPN
    except (requests.exceptions.ConnectionError):
        logging.info('Ошибка: Ошибка при на стороне пользователя')
        return 'Сервер Jira не доступна - проверте VPN'


if __name__ == "__main__":
    print(status_jira())
