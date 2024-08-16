# /reporting/report_generation.py

import pandas as pd

class ReportGeneration:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        report = self.data.describe()
        return report

# Usage
link_data = pd.read_csv("data/main_link_data.csv")
transaction_data = pd.read_csv("data/main_transaction_data.csv")

report_gen_link = ReportGeneration(link_data)
report_link = report_gen_link.generate_report()

report_gen_transaction = ReportGeneration(transaction_data)
report_transaction = report_gen_transaction.generate_report()
