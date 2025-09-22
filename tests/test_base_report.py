import pytest
import sys
import pathlib

project_root = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from reports.base_report import BaseReport


class TestBaseReport:
    """Тесты базового класса отчетов"""

    @pytest.fixture
    def base_report(self, sample_student_data):
        """Фикстура базового отчета"""
        return BaseReport(sample_student_data)

    def test_base_report_initialization(self, base_report):
        """Тест инициализации базового отчета"""
        assert base_report.data is not None
        assert base_report.processed_data == []

    def test_process_data_not_implemented(self, base_report):
        """Тест что process_data не реализован в базовом классе"""
        with pytest.raises(NotImplementedError):
            base_report.process_data()

    def test_get_headers_not_implemented(self, base_report):
        """Тест что get_headers не реализован в базовом классе"""
        with pytest.raises(NotImplementedError):
            base_report.get_headers()

    def test_print_without_processing(self, base_report, capsys):
        """Тест что print не работает без process_data"""
        with pytest.raises(NotImplementedError):
            base_report.print()
