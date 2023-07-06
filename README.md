# Отчеты из Jira Data Center

Программа предоставляет возможность формировать отчет по настроеному фильтру в Jira

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
