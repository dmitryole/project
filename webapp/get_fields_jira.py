from .config import jira

from .model import db, Fields

"""Зарос всех полей jira"""


def get_fields():
    data = jira.fields()
    return data


"""Вытаскивание значения атрибутов id и name"""


def get_fields_id_and_name():
    data = get_fields()
    """Проходимся по JSON"""
    for field in data:
        save_field(field['id'], field['name'])


""" Функция записи в БД"""


def save_field(field_id, field_name):
    """Проверяем есть ли такой field_id уже в БД"""
    query = Fields.query.filter(Fields.field_id == field_id).one_or_none()
    
    if query is None:
        """Создаем объект класса Fields"""
        new_field = Fields(field_id=field_id, field_name=field_name)
        """Кладем в сессию SQLAlchemy"""
        db.session.add(new_field)
        """Проливаем в БД"""
        db.session.commit()
    
    else:
        """Проверяем совпадает ли атрибут field_name"""
        if query.field_name != field_name:
            """Обновляем атрибут field_name"""
            query.field_name = field_name
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
            "custom":
                "com.atlassian.jira.plugin.system.customfieldtypes:textfield",
            "customId": 20310
        }
    },
    {
    ....
    }
]
"""
