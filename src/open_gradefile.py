#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:40:34 2018

@author: dongsiku
"""

import re
from os import path
from pathlib import Path
from extract_data_from_html import extract_data_from_html
import sys


def open_gradefile():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = get_filename()

    if filename is False:
        return False, False, False
    updated_date, course_list = extract_data_from_html(filename)
    return filename, updated_date, course_list


def get_filename():
    import tkinter
    from tkinter.filedialog import askopenfilename
    root = tkinter.Tk()
    root.withdraw()
    filename = askopenfilename(filetypes=[("単位修得状況確認表.html", "*.html")],
                               initialdir=path.join(str(Path.home()),
                               "Downloads"))

    if filename == "":
        print("no file")
        return False

    print(filename)
    return filename


if __name__ == "__main__":
    open_gradefile()
