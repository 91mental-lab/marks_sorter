import pytest
import subprocess
import tempfile
import os


class TestIntegration:

    @pytest.fixture
    def sample_csv_file(self):

        content = """student_name,subject,teacher_name,date,grade
Иван Иванов,Математика,Иванова И.И.,2023-10-10,5
Петр Петров,Физика,Петров П.П.,2023-10-12,4"""

        fd, path = tempfile.mkstemp(suffix=".csv")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(content)
            yield path
        finally:
            try:
                os.unlink(path)
            except:
                pass

    def test_cli_with_valid_args(self, sample_csv_file):

        result = subprocess.run(
            [
                "python",
                "main.py",
                "--files",
                sample_csv_file,
                "--report",
                "student-performance",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )

        assert result.returncode == 0
        assert "student_name" in result.stdout

    def test_cli_with_invalid_report(self):

        result = subprocess.run(
            ["python", "main.py", "--report", "invalid-report"],
            capture_output=True,
            text=True,
            timeout=30,
        )

        assert result.returncode != 0
