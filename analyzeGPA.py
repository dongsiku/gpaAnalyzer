#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:40:34 2018

@author: crantu
"""

import pandas as pd
import re
import tkinter
from tkinter.filedialog import askopenfilename
from os import path
from pathlib import Path
import datetime
from zenhan import z2h
strptime = datetime.datetime.strptime


class AnalyzeGPA:

    def __init__(self):
        # pd.set_option("max_rows", 200)
        # pd.options.display.max_rows
        pass

    def main(self):
        filename = self.get_filename()
        if filename is False:
            return 0

        updated_date, gpa_df = self.open_html(filename)
        return gpa_df

        gdf, csv_filename = self.extract_data_from_html()
        if gdf is not False:
            self.calculateGPA(gdf).to_csv(csv_filename)
            print("END")
        else:
            return 0

    def get_filename(self):
        root = tkinter.Tk()
        root.withdraw()
        filename = askopenfilename(filetypes=[("単位修得状況確認表.html", "*.html")],
                                   initialdir=path.join(str(Path.home()), "Downloads"))

        if filename == "":
            print("no file")
            return False
        # else:
            # url_filename = "file://{}".format(filename)
        print(filename)
        # df = pd.read_html(url_filename, encoding="Shift-JIS", header=0)

        return filename

    def open_html(self, filename):
        url_filename = "file://{}".format(filename)
        df = pd.read_html(url_filename, encoding="Shift-JIS", header=0)
        print(df)
        gpa_df = df[4].dropna(subset=["評点"]).reset_index(drop=True)

        updated_date = strptime(z2h(df[1].columns[0], 2), "%Y年%m月%d日")
        return updated_date, gpa_df

    def extract_data_from_html(self):
        df, filename = self.open_html()
        gdf = df[4].dropna(subset=["単位", "GP"]).reset_index(drop=True)

        updated_date = strptime(z2h(df[1].columns[0], 2), "%Y年%m月%d日").strftime("%Y%m%d")
        csv_filename = filename.replace(".html", "_{}.csv".format(updated_date))

        return gdf, csv_filename

if __name__ == "__main__":
    an = AnalyzeGPA()
    print(an.main())
