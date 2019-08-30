import re


class AnalyzeGPA_Okadai:
    def __init__(self, course_list):
        self.course_list = course_list

    def get_gpa(self):
        year_completed_set = set()
        for course_dict in self.course_list:
            year_completed_set.add(course_dict["year_completed"])

        year_completed_list = []
        for yc in year_completed_set:
            if re.match(r"\d\d\d\d年度 第\d学期", yc):
                year_completed_list.append(yc)
            elif not re.match(r".*またがり", yc):
                if "その他" not in year_completed_list:
                    year_completed_list.append("その他")
        year_completed_list.sort()

        tmp_yc_dict = {yc: 0.0 for yc in year_completed_list}
        sum_gp_by_credits_dict = tmp_yc_dict.copy()
        sum_credits_dict = tmp_yc_dict.copy()
        gpa_dict = tmp_yc_dict.copy()

        for course_dict in self.course_list:
            year_completed = course_dict["year_completed"]
            if re.match(r".*またがり", year_completed):
                tmp_yc = year_completed.rstrip("またがり").split(".", 1)
                year_completed =\
                    "{} 第{}".format(tmp_yc[0].split(" ")[0], tmp_yc[1])
            sum_gp_by_credits_dict[year_completed] +=\
                course_dict["gp"] * course_dict["credits"]
            sum_credits_dict[year_completed] += course_dict["credits"]

        sum_gp_by_credits = 0.0
        sum_credits = 0.0

        for yc in year_completed_list:
            sum_gp_by_credits += sum_gp_by_credits_dict[yc]
            sum_credits += sum_credits_dict[yc]

            try:
                gpa = sum_gp_by_credits_dict[yc] / sum_credits_dict[yc]
                accumulated_gpa = sum_gp_by_credits / sum_credits
            except ZeroDivisionError:
                continue

            gpa_dict[yc] = {"gpa": gpa, "accumulated_gpa": accumulated_gpa}
            print("{}, {}, {}".format(yc, gpa, accumulated_gpa))

        return year_completed_list, gpa_dict

if __name__ == "__main__":
    from main import open_gradefile
    _, course_list = open_gradefile()
    agpa_us = AnalyzeGPA_Okadai(course_list)
    print(agpa_us.get_gpa())
