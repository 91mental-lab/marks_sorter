import csv


def read_csv_files(file_paths):
    all_records = []
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    all_records.append(row)
        except FileNotFoundError:
            print(f"Ошибка: Файл {file_path} не найден")
            continue
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
            continue
    return all_records
