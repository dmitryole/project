# Отчеты из Jira Data Center

Программа предоставляет возможность формировать выборку задач по JQL и настраивать колонки отчета по полям зада

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
  JIRA_USER_LOGIN = "Username для авторизации в Jira"
  JIRA_API_KEY = "Токен Username"
  JIRA_URL = "URL инстанса Jira"
  basedir = os.path.abspath(os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'jira.db')
  ```
### Запуск программы

Для запуска программы запустите файл __init__.py:
```
  > set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```