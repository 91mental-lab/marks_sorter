from .base_report import BaseReport


class StudentPerformanceReport(BaseReport):

    report_name = "student-performance"

    def process_data(self):

        student_grades = {}

        for row in self.data:
            try:
                name = row["student_name"]
                grade = float(row["grade"])
                if name not in student_grades:
                    student_grades[name] = []

                student_grades[name].append(grade)

            except (KeyError, ValueError):
                continue

        self.processed_data = []
        for name, grades in student_grades.items():
            avg_grade = sum(grades) / len(grades)
            self.processed_data.append(
                {"student_name": name, "grade": round(avg_grade, 2)}
            )

        self.processed_data.sort(key=lambda x: x["grade"], reverse=True)

    def get_headers(self):
        return ["student_name", "grade"]
