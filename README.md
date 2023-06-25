# Отчеты из Jira Data Center

Программа предоставляет возможность формировать выборку задач по JQL и настраивать колонки отчета по полям задач

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
  JIRA_API_KEY = "Токен Username"
  JIRA_URL = "URL инстанса Jira"
  basedir = os.path.abspath(os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webapp.db')
  ```
### Запуск программы

Для запуска программы запустите файл run.bat:
```
  > run
```