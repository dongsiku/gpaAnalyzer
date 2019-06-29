import re


class AnalyzeGPA_Okadai:
    def __init__(self, cource_list):
        self.cource_list = cource_list

    def get_gpa(self):
        sum_gp_by_credits = 0.0
        sum_credits = 0.0

        year_completed_set = set()
        for cource_dict in self.cource_list:
            year_completed_set.add(cource_dict["year_completed"])

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

        for cource_dict in self.cource_list:
            year_completed = cource_dict["year_completed"]
            if re.match(r".*またがり", year_completed):
                tmp_yc = year_completed.rstrip("またがり").split(".", 1)
                year_completed =\
                    "{} 第{}".format(tmp_yc[0].split(" ")[0], tmp_yc[1])
            sum_gp_by_credits_dict[year_completed] +=\
                cource_dict["gp"] * cource_dict["credits"]
            sum_credits_dict[year_completed] += cource_dict["credits"]

        for yc in year_completed_list:
            gpa = sum_gp_by_credits_dict[yc] / sum_credits_dict[yc]
            gpa_dict[yc] = gpa
            print("{}, {}".format(yc, gpa))

        return year_completed_list, gpa_dict

if __name__ == "__main__":
    from main import main
    agpa_us = AnalyzeGPA_Okadai(main())
    print(agpa_us.get_gpa())
