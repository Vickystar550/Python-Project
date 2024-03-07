import requests
from bs4 import BeautifulSoup


URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"


class CollegeSalaryReport:
    def __init__(self):
        self.url = URL
        self.response = requests.get(url=self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def get_report(self):
        values = [data.getText() for data in self.soup.find_all('span', attrs={"class": "data-table__value"})]

        count = 5
        iterations = len(values) // count
        report = []

        for i in range(iterations):
            row = values[:count + 1]
            if not row:
                break
            report.append({
                "Rank": row[0],
                "Major": row[1],
                "Degree": row[2],
                "Early Career Pay ($)": float(row[3].replace('$', '').replace(',', '')),
                "Mid-Career Pay ($)": float(row[4].replace('$', '').replace(',', '')),
                "% High Meaning": row[5].replace('%', '')
            })
            values = values[count + 1:]

        return report


college = CollegeSalaryReport()
print(college.get_report())
