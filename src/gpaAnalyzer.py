import sys
from os import path
sys.path.append(path.dirname(path.abspath(sys.argv[0])))
from export_to_excelfile import ExportToExcelFile


def main():
    etef = ExportToExcelFile()
    etef.export_to_excel_file()


if __name__ == "__main__":
    main()
