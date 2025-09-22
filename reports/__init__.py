from .stud_marks_report import StudentPerformanceReport

# Собираем все доступные отчеты
ALL_REPORTS = [StudentPerformanceReport]

# Создаем словарь для быстрого доступа: имя -> класс
REPORT_CLASSES = {report.report_name: report for report in ALL_REPORTS}


def get_available_report_names():
    """Возвращает список доступных имен отчетов"""
    return list(REPORT_CLASSES.keys())


def get_report_class(report_name):
    """Возвращает класс отчета по имени"""
    if report_name not in REPORT_CLASSES:
        available = get_available_report_names()
        raise ValueError(
            f"Отчет '{report_name}' не найден. Доступные: {', '.join(available)}"
        )

    return REPORT_CLASSES[report_name]


def create_report(report_name, data):
    """Создает экземпляр отчета"""
    report_class = get_report_class(report_name)
    return report_class(data)
