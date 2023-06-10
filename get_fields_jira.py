import requests
from config import STAGE_JIRA_URL, STAGE_JIRA_API_KEY

"""API-запрос всех полей Jira"""
def get_fields():
    url = f'{STAGE_JIRA_URL}/rest/api/2/field'
    headers = {
    "Authorization": f'Bearer {STAGE_JIRA_API_KEY}'
    }
    responce = requests.get(url,headers=headers)
    """Логика при статусе ответа Jira"""
    if 200 <= responce.status_code < 300:
        data = responce.json()
        return data
    else:
        print('Ошибка: Ошибка при подключении к Jira', responce)

if __name__ == "__main__":
    print((get_fields()))