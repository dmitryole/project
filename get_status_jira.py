import requests
from config import STAGE_JIRA_URL

def status_jira():
    # Обработка ответа при ответе Jira
    try:
        result = requests.get(STAGE_JIRA_URL)
        result.raise_for_status()
        return 'Stage Jira доступен'
    # Обработка ошибок Jira
    except (ValueError):
        return 'Stage Jira не доступна - обратитесь к ДЦС'
    # Обработка ответа при отсутствии VPN 
    except (requests.exceptions.ConnectionError, ValueError):
        return 'Stage Jira не доступна - проверте VPN'

if __name__ == "__main__":
    print(status_jira())