from jira import JIRA
from datetime import datetime
import requests
import logging
import csv

from config import JIRA_URL, JIRA_API_KEY


def process_general_CSV_from_filter(filter, jira_api_key):
    # Вытаскивание JQL из фильтра
    sql = get_jql_filter(filter, jira_api_key)
    # Вытаскивание колонок из фильтра
    columns = get_columns_filter(filter, jira_api_key)
    # Вытаскивание наименования колонок фильтра
    label_columns = get_label_of_columns(columns)
    # Функция вытаскивания значений полей из задачи
    value_columns = get_value_of_columns(columns)
    # Создание сессии с Jira
    client_jira = jira(jira_api_key)
    # Функция запроса задач с определенными полями
    issues = get_all_issues(client_jira, sql, value_columns)
    # Функция записи полученного словаря в CSV
    generate_data(issues, label_columns, filter)


# Вытаскивание JQL из фильтра
def get_jql_filter(filter, api_key):
    url = f'{JIRA_URL}rest/api/2/filter/{filter}'
    headers = {"Authorization": f'Bearer {api_key}'}
    result = requests.get(url, headers=headers)
    return result.json()['jql']


# Вытаскивание колонок из фильтра
def get_columns_filter(filter, api_key):
    url = f'{JIRA_URL}rest/api/2/filter/{filter}/columns'
    headers = {"Authorization": f'Bearer {api_key}'}
    columns = requests.get(url, headers=headers)
    return columns.json()


# Вытаскивание наименования колонок фильтра
def get_label_of_columns(columns):
    label_columns = []
    for column in columns:
        label_columns.append(column['label'])
    return label_columns


# Функция вытаскивания значений полей из задачи
def get_value_of_columns(columns):
    value_columns = []
    for column in columns:
        # Вытаскиваем значение атрибута "key"
        if column['value'] == "issuekey":
            value_columns.append('key')
        # Вытаскиваем значение остальных атрибутов
        else:
            value_columns.append(column['value'])
    return value_columns


# Создание сессии с Jira
def jira(api_key):
    try:
        jira = JIRA(
            server=JIRA_URL,
            token_auth=api_key)
        return jira
    except (ConnectionError):
        logging.info('Ошибка: Соединение с JIRA не успешно')


# Функция запроса задач с определенными полями
def get_all_issues(jira, jql_str, fields):
    # Список задач с полями
    issues = []
    # Стартовый элемент
    start_at = 0
    # Количество возвращаемых элементов
    max_results = 100
    # Цикл прохода по страницам запроса
    while True:
        chunk_issues = jira.search_issues(
                                          # JQL поиск
                                          jql_str=jql_str,
                                          # Начальный элемент страницы
                                          startAt=start_at,
                                          # Кол. элементов на странице
                                          maxResults=max_results,
                                          # Запрашиваемые поля
                                          fields=fields)
        # Выход из цикла, когда страница пустая
        if len(chunk_issues) == 0:
            break
        # Перебор задач
        for issue in chunk_issues:
            # Вытаскивание полей из задач
            issues.append(get_fields_issues(issue, fields))
        # Переход на элемент на следующей страницы
        start_at += max_results
    return issues


# Функция вытаскиванния полей из задачи
def get_fields_issues(issue, fields):
    # Фиксируем ключ задачи
    field_issue = {}
    # Перебор полей
    for field in fields:
        # Правильно записываем атрибут "Key"
        if field == 'issuekey':
            field_issue['key'] = issue.key
        # Добавляем поля в словарь задачи
        else:
            field_issue[field] = get_value_field(issue, field)
    return field_issue


# Функция обработки значений полей
def get_value_field(issue, field):
    value_field = str(getattr(issue.fields, field))
    # Вытаскивание значений из списка
    if type(value_field) == list:
        return ','.join(value_field)
    # Преобразуем значение в строку
    elif type(value_field) != str:
        return str(value_field)
    elif type(value_field) == str:
        # Если в строке дата и время
        try:
            value_field = datetime.strptime(
                value_field, '%Y-%m-%dT%H:%M:%S.%f%z')
            return value_field.strftime('%d.%m.%y')
        # Если строка не преобразуется, то возвращаем
        except (ValueError):
            return value_field


# Функция записи полученного словаря в CSV
def generate_data(data, label, filter):
    with open(f'webapp\issues_from_filter_{filter}.csv',
              'w', encoding='utf-8', newline='') as f:
        # Записиваем заголовок в CSV-файл
        writer_label = csv.writer(f, delimiter=';')
        writer_label.writerow(label)
        # Записываем поля в CSV-файл
        fields = list(data[0].keys())
        writer_fields = csv.DictWriter(f, fields, delimiter=';')
        for chunk_data in data:
            writer_fields.writerow(chunk_data)


if __name__ == "__main__":
    jira_api_key = JIRA_API_KEY
    filter = '25700'
    process_general_CSV_from_filter(filter, jira_api_key)
