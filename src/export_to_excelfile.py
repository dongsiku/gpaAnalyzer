import openpyxl as px
from datetime import datetime
from shutil import copyfile
from os import path
from sys


class ExportToExcelFile:
    def __init__(self, dirname):
        datetimeNow = datetime.now()
        self.excel_filename =\
            "gpaAnalyzer_{}.xlsx".format(datetimeNow.strftime('%Y%m%d_%H%M%S'))
        self.excel_filename = path.join(dirname, self.excel_filename)

    def copy_excel_file(self):
        original_excel_filename =\
            path.join(path.dirname(path.abspath(sys.argv[0])),
                                   "gpaAnalyzer.xlsx")
        copyfile(original_excel_filename, self.excel_filename)

    def export_to_excel_file(self):
        wb = px.load_workbook(filename)
        ws_gpa_okadai = wb['Okadai']
        ws_gpa_summary = wb['Summary']
