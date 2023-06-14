import logging
import requests
from .config import STAGE_JIRA_URL, STAGE_JIRA_API_KEY

from .model import db, Fields

"""API-запрос всех полей Jira"""
def get_fields():
    url = f'{STAGE_JIRA_URL}/rest/api/2/field'
    headers = {
    "Authorization": f'Bearer {STAGE_JIRA_API_KEY}'
    }
    response = requests.get(url,headers=headers)
    if response.ok:
        data = response.json()
        return data
    else:
        logging.info('Ошибка: Ошибка при подключении к Jira', response)

"""Вытаскивание значения атрибутов id и name"""
def get_fields_id_and_name():
    data = get_fields()
    """Проходимся по JSON"""
    for field in data:
        save_fields(field['id'], field['name'])

    

""" Функция записи в БД 
(Требуется реализовать проверку, что у кортежа не изменился атрибут name.
В случае изменения - перезаписать атрибут name)"""
def save_fields(field_id, field_name):
    """Выборка из БД"""
    new_fields = Fields.query.filter(Fields.field_id == field_id).count()
    print(new_fields)
    if not new_fields:
        """Создаем объект класса Fields"""
        new_fields = Fields(field_id=field_id, field_name=field_name)
        """Кладем в сессию SQLAlchemy"""
        db.session.add(new_fields)
        """Проливаем в БД"""
        db.session.commit()

if __name__ == "__main__":
    print(get_fields())

"""
[
    {
        "id": "customfield_20310",
        "name": "Заводской номер и Стикер",
        "custom": true,
        "orderable": true,
        "navigable": true,
        "searchable": true,
        "clauseNames": [
            "cf[20310]",
            "Заводской номер и Стикер"
        ],
        "schema": {
            "type": "string",
            "custom": "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
            "customId": 20310
        }
    },
    {
    ....
    }
]
"""