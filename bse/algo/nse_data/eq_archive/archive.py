import os
from datetime import datetime, timedelta
from urllib.error import HTTPError

import pandas as pd
from nsepy import get_history

"""https: // www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol = auropharma & segmentLink = 3 & symbolCount = 1 & series = EQ & dateRange = week & fromDate = &toDate = &dataType = PRICEVOLUMEDELIVERABLE

"https: // www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol = auropharma & segmentLink = 3 & symbolCount = 1 & series = EQ & dateRange = + & fromDate = 04-02-2021 & toDate = 05-02-2021 & dataType = PRICEVOLUMEDELIVERABLE"""


class GenerateEQArchive(object):
    def __init__(self):
        self.data = None
        self.nify_100 = self.get_nifty100()

    def get_scrip_history(self, scrip, start, end):
        return get_history(symbol=scrip,
                           start=start,
                           end=end)

    def get_nifty100(self):
        nifty_csv = pd.read_csv('data/reports/CURRENT-NIFTY-100.csv')
        nifty_csv.columns = nifty_csv.columns.str.strip()
        return list(nifty_csv['SYMBOL'])

    def check_diff(self, df):
        descripency = 0
        detail = "-"
        if (df['Volume'][0] > df['Volume'][1]) and (df['Deliverable Volume'][0] < df['Deliverable Volume'][1]):
            descripency = 1
            detail = "Vol Down, Delivery Up"
        if (df['Volume'][0] < df['Volume'][1]) and (df['Deliverable Volume'][0] > df['Deliverable Volume'][1]):
            descripency = 1
            detail = "Vol Up, Delivery Down"
        df['Descripency Detail'] = detail
        df['Descripency'] = descripency
        return df

    def get_report(self):
        start_date, end_date = self.get_working_dates()
        print(f'Generating report from {start_date} to {end_date}')
        nifty_100 = self.nify_100
        for index, scrip in enumerate(nifty_100):
            try:
                df = self.get_scrip_history(scrip, start_date, end_date)
                df = self.check_diff(df)
                if index == 1:
                    self.data = df
                if index != 1:
                    self.data = pd.concat([self.data, df])
            except Exception as error:
                print(error)
                print(f"{scrip } indexing error has occurred")
                continue
        self.data = self.data.rename(columns={'Symbol': 'SYMBOL'})

    def save_report(self):
        data = self.data.reset_index().set_index(['SYMBOL'])
        data['%Deliverble'] = data['%Deliverble'].astype(float) * 100
        data = data.sort_values(by=["Descripency", "SYMBOL"],  ascending=False)
        cwd = os.getcwd()
        path = cwd + "/reports"
        data.to_csv(
            f'{path}/{datetime.now().strftime("%b-%d-%Y")}-archive.csv')
        print("Equity archive generated ====> Done\n")

    def get_working_dates(self):
        days = []
        start = datetime.now() - timedelta(4)
        end = datetime.now()
        excluded = (6, 7)
        while start.date() <= end.date():
            if start.isoweekday() not in excluded:
                days.append(start.date())
            start += timedelta(days=1)
        if end > end.replace(
                hour=0, minute=0, second=0, microsecond=0) and end < end.replace(
                hour=19, minute=30, second=0, microsecond=0):
            days.pop()
        days = days[len(days)-2:]
        return days[0], days[1]


if __name__ == '__main__':
    archive = GenerateEQArchive()
    archive.get_report()
    archive.save_report()
