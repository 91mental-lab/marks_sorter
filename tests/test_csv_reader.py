import pytest
import os
import tempfile


class TestCSVReader:

    def test_read_nonexistent_file(self):

        from file_readers.csv_file_reader import read_csv_files

        result = read_csv_files(["nonexistent.csv"])
        assert result == []

    def test_empty_file(self, empty_csv_file):

        from file_readers.csv_file_reader import read_csv_files

        result = read_csv_files([empty_csv_file])
        assert len(result) == 0

    def test_invalid_data_skipped(self, invalid_csv_file):

        from file_readers.csv_file_reader import read_csv_files

        result = read_csv_files([invalid_csv_file])
        # Должны прочитаться только корректные строки
        valid_students = [
            row
            for row in result
            if row["student_name"] in ["Иван Иванов", "Мария Сидорова"]
        ]
        assert len(valid_students) == 2

    def test_valid_data_read_correctly(self, sample_csv_file):

        from file_readers.csv_file_reader import read_csv_files

        result = read_csv_files([sample_csv_file])
        assert len(result) == 3
        assert all("student_name" in row for row in result)
        assert all("grade" in row for row in result)
