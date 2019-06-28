from zenhan import z2h
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
strptime = datetime.datetime.strptime


def extract_data_from_html(filename):
    # html to table
    url_filename = "file://{}".format(filename)
    html = urlopen(url_filename)
    bsObj = BeautifulSoup(html, "html.parser")
    table = bsObj.findAll("table")

    # table to update_date
    updated_date = strptime(z2h(table[1].get_text().strip(), 2), "%Y年%m月%d日")

    # table to gpa_list
    gpa_table = table[4]
    gpa_rows = gpa_table.findAll("tr")
    gpa_list = []
    gpa_items = ["course_title", "lecturer", "year_completed",
                 "grade_points", "grade", "credits", "gp"]
    gpa_rows.pop(0)
    for gpa_row in gpa_rows:
        tmp_dict = {item:None for item in gpa_items}
        is_append_list = True
        for i, cell in enumerate(gpa_row.findAll(['td', 'th'])):
            tmp_celltext = z2h(cell.get_text().strip().replace("\u3000", " "), 3)
            if i == 3 and tmp_celltext == "":
                is_append_list = False
                continue
            tmp_dict[gpa_items[i]] = tmp_celltext

        if is_append_list is True:
            # tmp_dict["year_completed"] = []
            tmp_dict["grade_points"] = int(tmp_dict["grade_points"])
            tmp_dict["credits"] = float(tmp_dict["credits"])
            gpa_list.append(tmp_dict)

    return updated_date, gpa_list
