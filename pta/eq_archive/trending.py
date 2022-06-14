import os
from datetime import datetime, timedelta
from urllib.error import HTTPError

import numpy as np
import pandas as pd


class GenerateVolitalityReport(object):
    """
   This script will generate list of trending stocks for top gainer and top 
   losers.

    URL: 
    for market activity report:
        https://www1.nseindia.com/ArchieveSearch?h_filetype=eqmkt&date=03-09-2021&section=EQ
    for nse list:
        https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20100
    """

    def __init__(self):
        self.date = self.get_last_working_day()
        # self.data, self.nify_100 = self.get_nifty100()

    def get_nifty100(self):
        nifty_csv = pd.read_csv('data/reports/CURRENT-NIFTY-100.csv')
        nifty_csv.columns = nifty_csv.columns.str.strip()
        nify_100 = [scrip for scrip in nifty_csv['SYMBOL']]
        return pd.DataFrame(nify_100, columns=['SYMBOL']), nify_100

    def get_report(self):
        try:
            url = f'https://www1.nseindia.com/archives/equities/mkt/MA{self.date}.csv'
            archive = pd.read_csv(url, skiprows=7)
            index_archive = archive[1:64]
            index_archive['NET RETURN'] = np.log2(index_archive['CLOSE'].astype(
                float)/index_archive['PREVIOUS CLOSE'].astype(float)) * 100
            index_archive = index_archive.set_index('INDEX')
            index_archive = index_archive.drop(['India VIX', 'Nifty Bank'])
            index_archive = index_archive.sort_values('NET RETURN', ascending=False)
            print(index_archive[:10])
            print(index_archive[-10:])
            self.data = index_archive
        except HTTPError as error:
            print(error)
            print(f"{url} has no report")

    def save_report(self):
        data = self.data.set_index(['SYMBOL'])
        data = data.iloc[:, pd.to_datetime(data.columns, format="%d-%b-%Y").argsort()].reset_index()
        data.index = data.index + 1
        data['V AVERAGE'] = data.drop('SYMBOL', axis=1).apply(lambda x: x.mean(), axis=1).round(3)
        data = data.sort_values(by=["V AVERAGE"],  ascending=False)
        data.to_csv(f'{datetime.now().strftime("%b-%d-%Y")}-vreport.csv')
        print("Volitality report generated ====> Done\n")

    def get_last_working_day(self):
        days = []
        start = datetime.now() - timedelta(4)
        end = datetime.now()
        excluded = (6, 7)
        while start.date() <= end.date():
            # reports are generated only after 8pm
            if start.isoweekday() not in excluded:
                days.append(start.strftime('%d%m%y'))
            start += timedelta(days=1)
        print(days)
        if start.isoweekday() not in excluded and end.hour < 20:
            return days[-2]
        return days.pop()


if __name__ == '__main__':
    vreport = GenerateVolitalityReport()
    vreport.get_report()
    # vreport.save_report()
