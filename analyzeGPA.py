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
        pass

    def main(self):
        gdf, csv_filename = self.extract_data_from_html()
        if gdf is not False:
            self.calculateGPA(gdf).to_csv(csv_filename)
            print("END")
        else:
            return 0

    def open_html(self):
        root = tkinter.Tk()
        root.withdraw()
        filename = askopenfilename(filetypes=[("単位修得状況確認表.html", "*.html")],
                                   initialdir=path.join(str(Path.home()), "Downloads"))

        if filename == "":
            print("no file")
            return False
        else:
            url_filename = "file://{}".format(filename)
        print(filename)
        df = pd.read_html(url_filename, encoding="Shift-JIS", header=0)

        return df, filename

    def extract_data_from_html(self):
        df, filename = self.open_html()
        gdf = df[4].dropna(subset=["単位", "GP"]).reset_index(drop=True)

        updated_date = strptime(z2h(df[1].columns[0], 2), "%Y年%m月%d日").strftime("%Y%m%d")
        csv_filename = filename.replace(".html", "_{}.csv".format(updated_date))

        return gdf, csv_filename

    def calculateGPA(self, gdf):
        quarter = []
        credit = {}
        cdt_gp = {}

        for i in range(len(gdf["授業科目"])):
            completed = gdf["修得年度"][i]
            if re.match(r".*またがり", completed):
                tmp = completed.rstrip("またがり").split(".", 1)
                completed = "{} 第{}".format(tmp[0].split(" ")[0], tmp[1])

            if (completed in quarter) is False:
                quarter.append(completed)
                credit.update({completed: 0.0})
                cdt_gp.update({completed: 0.0})

            cdt = float(gdf["単位"][i])
            credit[completed] += cdt
            cdt_gp[completed] += (cdt*float(gdf["GP"][i]))

        sum_c = 0.0
        sum_cg = 0.0

        quarter.sort()

        avg_list = []
        gavg_list = []

        for q in quarter:
            sum_c += credit[q]
            sum_cg += cdt_gp[q]
            avg_list.append(cdt_gp[q]/credit[q])
            gavg_list.append(sum_cg/sum_c)

        result = pd.DataFrame({"avg": avg_list, "gavg": gavg_list},
                              index=quarter)

        return result.round(3)


if __name__ == "__main__":
    an = AnalyzeGPA()
    an.main()
