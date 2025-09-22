import pytest
import sys
import pathlib

project_root = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from reports.stud_marks_report import StudentPerformanceReport


class TestStudentPerformanceReport:

    @pytest.fixture
    def student_report(self, sample_student_data):

        return StudentPerformanceReport(sample_student_data)

    def test_average_calculation(self, student_report):

        student_report.process_data()

        students = {s["student_name"]: s for s in student_report.processed_data}

        assert students["Иван Иванов"]["grade"] == 4.0

        assert students["Петр Петров"]["grade"] == 4.0

        assert students["Мария Сидорова"]["grade"] == 5.0

    def test_sorting_order(self, student_report):

        student_report.process_data()
        grades = [student["grade"] for student in student_report.processed_data]
        assert grades == [5.0, 4.0, 4.0]

    def test_headers_correct(self, student_report):

        headers = student_report.get_headers()
        assert headers == ["student_name", "grade"]

    def test_report_name(self):

        report = StudentPerformanceReport([])
        assert report.report_name == "student-performance"

    def test_invalid_grades_skipped(self):

        data = [
            {"student_name": "Иван", "grade": "5"},
            {"student_name": "Петр", "grade": "не_число"},
            {"student_name": "Мария", "grade": "4"},
        ]
        report = StudentPerformanceReport(data)
        report.process_data()
        assert len(report.processed_data) == 2
