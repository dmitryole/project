import csv

from webapp.config import jira

"""Функция запроса задач с определеными полями"""


def get_all_issues(jql_str, fields):
    # Список задач с полями
    issues = []
    # Стартовый элемент
    start_at = 0
    # Количество возрашаемых элементов
    max_results = 100
    # Цыкл прохода по страницам запроса
    while True:
        chunk_issues = jira.search_issues(
                                          # JQL поиск
                                          jql_str=jql_str,
                                          # Начальный элемент страницы
                                          startAt=start_at,
                                          # Элементов на странице
                                          maxResults=max_results,
                                          # Определяем поля
                                          fields=fields)
        # Выход из цыкла, когда страница пустая
        if len(chunk_issues) == 0:
            print('break')
            break
        # Перебор задач
        for issue in chunk_issues:          
            # Вытаскивание полей из задач
            issues.append(get_fields_issues(issue, fields))
        # Переход на элемент на следующей страницы
        start_at += max_results
    return issues


"""Функция вытаскиванния полей из задачи"""


def get_fields_issues(issue, fields):
    field_issue = {}
    # Перебор полей
    for field in fields:
        # Фиксируем ключ задачи
        field_issue = {'key': issue.key}
        # Добавляем поля в словарик задачи
        field_issue[field] = getattr(issue.fields, field)
    return field_issue


"""Функция записи полученого словаря в CSV"""


def generate_data(data):
    with open('issues.csv', 'w', encoding='utf-8', newline='') as f:
        # Вытаскиваем ключи словаря
        fields = list(data[0].keys())
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for chunk_data in data:
            writer.writerow(chunk_data)


if __name__ == "__main__":
    sample_jql = \
        'project = ATL AND Sprint = 325'
    # Поле ключ будет по умолчанию
    sample_fields = ['summary']
    data = get_all_issues(sample_jql, sample_fields)
    print(data)
    # generate_data(data)


"""
print:
[
    {
        'key': 'SIRIUS-36549',
        'summary': 'тест',
        'description': None,
        'customfield_21501': ['187711367 (CLIBD-392)']
    },
    {
        'key': 'SIRIUS-36505',
        'summary': 'Обновление в новом ЛК',
        'description': 'Доброе время суток',
        'customfield_21501': ['207700677 (CLIBD-61544)']
    }
]
"""
