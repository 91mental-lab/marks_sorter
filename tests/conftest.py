import pytest
import csv
import tempfile
import os
import sys
import pathlib

project_root = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_student_data():

    return [
        {"student_name": "Иван Иванов", "subject": "Математика", "grade": "5"},
        {"student_name": "Петр Петров", "subject": "Физика", "grade": "4"},
        {"student_name": "Иван Иванов", "subject": "Физика", "grade": "3"},
        {"student_name": "Мария Сидорова", "subject": "Химия", "grade": "5"},
    ]


@pytest.fixture
def sample_csv_content():
    """Возвращает содержимое CSV без создания файла"""
    return """student_name,subject,teacher_name,date,grade
Иван Иванов,Математика,Иванова И.И.,2023-10-10,5
Петр Петров,Физика,Петров П.П.,2023-10-12,4
Мария Сидорова,Химия,Сидоров С.С.,2023-10-15,5"""


@pytest.fixture
def sample_csv_file(sample_csv_content):
    """Создает временный CSV файл с правильным закрытием"""
    fd, path = tempfile.mkstemp(suffix=".csv")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(sample_csv_content)
        yield path
    finally:
        try:
            os.unlink(path)
        except:
            pass


@pytest.fixture
def invalid_csv_content():
    """Содержимое CSV с некорректными данными"""
    return """student_name,subject,grade
Иван Иванов,Математика,5
Петр Петров,Физика,не_число
Мария Сидорова,Химия,5"""


@pytest.fixture
def invalid_csv_file(invalid_csv_content):
    """Создает CSV с некорректными данными"""
    fd, path = tempfile.mkstemp(suffix=".csv")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(invalid_csv_content)
        yield path
    finally:
        try:
            os.unlink(path)
        except:
            pass


@pytest.fixture
def empty_csv_file():
    """Создает пустой CSV файл"""
    fd, path = tempfile.mkstemp(suffix=".csv")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("student_name,subject,grade\n")
        yield path
    finally:
        try:
            os.unlink(path)
        except:
            pass
