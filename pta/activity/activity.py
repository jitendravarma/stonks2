import requests
import csv
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# link to download data 
# https://www1.nseindia.com/archives/equities/mkt/MA121121.csv
class DailyAcitivityReport(object):

    def __init__(self):
        self.working_date = self.get_working_date()
        self.ma_url = 'https://www1.nseindia.com/archives/equities/mkt/'
        self.REPORT_NAME = f'{self.working_date}-activity.csv'
        # self.data, self.nify_100 = self.get_nifty100()
    
    def get_working_date(self):
        days = []
        start = datetime.now() - timedelta(4)
        end = datetime.now()
        excluded = (6, 7)
        while start.date() <= end.date():
            # as ma report is generated eod,skip if it runs before it ie 8pm
            if start.isoweekday() not in excluded and not (start.day == end.day and end.hour < 20):
                days.append(start.strftime('%d%m%y'))
            start += timedelta(days=1)
        return days.pop()
    
    def get_daily_active_sectors(self):
        print(f'{self.ma_url}MA{self.working_date}.csv')
        open('templates/your_file.html', "w").close()
        with requests.get(f'{self.ma_url}MA{self.working_date}.csv', stream=True) as source:
            lines = (line.decode('utf-8') for line in source.iter_lines())
            rdr = csv.reader(lines)
            with open("temp-results.csv", "w") as result:
                wtr = csv.writer(result)
                for index, r in enumerate(rdr):
                    if index > 7 and index < 68:
                        wtr.writerow((r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

        activity_report = pd.read_csv('temp-results.csv', index_col ="INDEX")
        activity_report['GAIN/LOSS LOG'] = np.log2(activity_report['CLOSE'] / activity_report['PREVIOUS CLOSE'])
        activity_report.drop(['Nifty Bank', 'India VIX'], inplace = True)
        activity_report = activity_report.sort_values(by=["GAIN/LOSS LOG"],  ascending=False).round(3)

        activity_report.to_csv(self.REPORT_NAME)


    def get_performing_stocks(self):
        print(f'{self.ma_url}MA{self.working_date}.csv')
        with requests.get(f'{self.ma_url}MA{self.working_date}.csv', stream=True) as source:
            lines = (line.decode('utf-8') for line in source.iter_lines())
            rdr = csv.reader(lines)
            with open(self.REPORT_NAME, "a") as result:
                wtr = csv.writer(result)
                wtr.writerow("")
                wtr.writerow([f'Top gainer/losers list for {self.working_date}'])
                for index, row in enumerate(rdr):
                    try:
                        if row[1] == "Securities Price Volume Data in Normal market":
                            break
                    except Exception as e:
                        pass
                    if (index > 104 and index < 140) and row:
                        try:
                            wtr.writerow((row[1], row[2], row[3], row[4],row[5]))
                        except:
                            wtr.writerow([''])
                            wtr.writerow([row[1]])
                            pass
        activity_report = pd.read_csv(self.REPORT_NAME, index_col ="INDEX")
        activity_report.to_html('templates/your_file.html')


a = DailyAcitivityReport()
a.get_daily_active_sectors()
a.get_performing_stocks()
