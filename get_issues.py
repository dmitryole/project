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
            break
        # Вытаскивание полей из задач
        issues.append(get_fields_issues(chunk_issues, fields))
        # Переход на элемент на следующей страницы
        start_at += max_results
        return issues


"""Функция вытаскиванния полей из задачи"""


def get_fields_issues(chunk_issues, fields):
    # Перебор задач
    for issue in chunk_issues:
        # Фиксируем ключ задачи
        field_issue = {'key': issue.key}
        # Перебор полей
        for field in fields:
            # Добавляем поля в словарик задачи
            field_issue[field] = getattr(issue.fields, field)
    return field_issue


if __name__ == "__main__":
    sample_jql = \
        'key = SIRIUS-36505 OR key = SIRIUS-36549'
    # Поле ключ будет по умолчанию
    sample_fields = ['summary',
                     'customfield_21501',
                     'description']
    print(get_all_issues(sample_jql, sample_fields))


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
