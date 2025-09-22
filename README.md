# Анализ успеваемости студентов 

Простой скрипт для генерации отчетов об успеваемости студентов из CSV-файлов.

#🚀 Быстрый старт

## Клонировать репозиторий
git clone <repository-url>
cd PythonProject

## Установить зависимости
pip install -r requirements.txt

## Запустить скрипт
python main.py --files <файл> --report <Название отчёта>

Примеры работы:
##2 файла 

![2 файла](https://github.com/user-attachments/assets/bf4301a6-416b-4dff-9740-6a524eb50f01)

##1 файл 
![1 файл](https://github.com/user-attachments/assets/9ec10350-2fd8-4991-872c-195660d0cbfd)


##Неверное название отчёта 
![неверное имя отчёта](https://github.com/user-attachments/assets/046384ab-85e3-4114-a03b-db988952143c)


#🤔 Как добавить новый отчёт? 
1. Создать класс в reports/:

``` Python
from reports.base_report import BaseReport

class NewReport(BaseReport):
    report_name = "new-report"
    
    def process_data(self):
        # логика обработки
        pass
    
    def get_headers(self):
        return ['header1', 'header2']
```

2. Добавить в реестр (reports/__init__.py):

``` Python
from .new_report import NewReport
REPORT_CLASSES = {
    'student-performance': StudentPerformanceReport,
    'new-report': NewReport  # ← добавить эту строку
}
```

