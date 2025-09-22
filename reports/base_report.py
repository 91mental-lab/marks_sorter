from tabulate import tabulate


class BaseReport:

    report_name = "base-report"

    def __init__(self, data):
        self.data = data
        self.processed_data = []

    def process_data(self):
        raise NotImplementedError("Метод process_data должен быть переопределен")

    def get_headers(self):
        raise NotImplementedError("Метод get_headers должен быть переопределен")

    def print(self):
        self.process_data()

        table_data = []
        for i, row in enumerate(self.processed_data, 1):
            row_data = [i]
            for header in self.get_headers():
                row_data.append(row.get(header, "N/A"))
            table_data.append(row_data)
        headers = ["#"] + self.get_headers()

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
