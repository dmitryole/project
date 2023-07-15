# Отчеты из Jira Data Center

Программа предоставляет возможность сформировать отчет по настроенному фильтру в Jir

### Проблематика

1. Экспорт фильтра содержит только 1000 задач
- [Filter export only contains 1000 issues in Jira server](https://confluence.atlassian.com/jirakb/how-to-use-insight-custom-field-to-dynamically-filter-a-jira-custom-field-1093993792.html)

2. Экспорт фильтра не отображает атрибуты Insight объекта указанного в поле
- [Export Assets Object fields to Spreadsheets and Word](https://confluence.atlassian.com/jirakb/export-assets-object-fields-to-spreadsheets-and-word-1167741095.html)

### Установка

1. Клонируйте репозиторий, создайте виртуальное окружение:
  ```
  > git clone https://github.com/dmitryole/project.git
  > python -m venv env
  > env\Scripts\activate
  ```
2. Установите зависимости:
  ```
  > pip install -r requirements.txt
  ```
3. Создайте файл config.py и создайте в нем базовые переменные:
  ```
  JIRA_URL = "URL инстанса Jira"
  ```
### Запуск программы

Для запуска программы запустите файл run.bat:
```
  > run
```
