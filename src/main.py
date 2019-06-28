#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:40:34 2018

@author: dongsiku
"""

import re
import tkinter
from tkinter.filedialog import askopenfilename
from os import path
from pathlib import Path
import datetime
from extract_data_from_html import extract_data_from_html

strptime = datetime.datetime.strptime


class AnalyzeGPA:
    def __init__(self):
        pass

    def main(self):
        filename = self.get_filename()
        if filename is False:
            return 0
        updated_date, gpa_list = extract_data_from_html(filename)
        return gpa_list

    def get_filename(self):
        root = tkinter.Tk()
        root.withdraw()
        filename = askopenfilename(filetypes=[("単位修得状況確認表.html", "*.html")],
                                   initialdir=path.join(str(Path.home()), "Downloads"))

        if filename == "":
            print("no file")
            return False

        print(filename)
        return filename


if __name__ == "__main__":
    an = AnalyzeGPA()
    print(an.main())
