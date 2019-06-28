from analyzeGPA import AnalyzeGPA
import re


class AnalyzeGPA_US:
    def __init__(self):
        pass

    def main(self):
        a_gpa = AnalyzeGPA()

        gdf, filename = a_gpa.extract_data_from_html()
        print(self.calculateGPA(gdf))

    def calculateGPA(self, gdf):
        point = 0.0
        credit = 0.0

        for i in range(len(gdf["授業科目"])):
            if gdf["評点"][i] is not False:
                point += gdf["評点"][i] * gdf["単位"][i]
                credit += gdf["単位"][i]

        return point/credit


if __name__ == "__main__":
    an = AnalyzeGPA_US()
    an.main()
