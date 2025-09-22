import argparse
from file_readers.csv_file_reader import read_csv_files
from reports import get_available_report_names, create_report


def main():

    available_reports = get_available_report_names()

    parser = argparse.ArgumentParser(description="Генератор отчетов по студентам")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV файлам через пробел"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=available_reports,
        help=f'Тип отчета. Доступные: {", ".join(available_reports)}',
    )

    args = parser.parse_args()

    print(f"Чтение файлов: {args.files}")
    data = read_csv_files(args.files)

    if not data:
        print("Ошибка: Не удалось прочитать данные")
        return

    print(f"Прочитано {len(data)} записей")

    try:
        report = create_report(args.report, data)
        report.print()

    except Exception as e:
        print(f"Ошибка при создании отчета: {e}")


if __name__ == "__main__":
    main()
