import os
from datetime import datetime, timedelta
from urllib.error import HTTPError

import pandas as pd

NIFTY_100 = ["ACC", "AMBUJACEM", "ADANITRANS", "BIOCON", "BPCL", "TATAMOTORS", "SHREECEM", "EICHERMOT", "MARUTI", "ULTRACEMCO", "GODREJCP", "ASIANPAINT", "RELIANCE", "GLAND", "UPL", "TCS", "HDFCLIFE", "HINDUNILVR", "TATACONSUM", "IOC", "HDFC", "ICICIPRULI", "PIDILITIND", "DRREDDY", "BHARTIARTL", "BOSCHLTD", "INFY", "HCLTECH", "NESTLEIND", "BAJAJ-AUTO", "ICICIGI", "INDIGO", "COLPAL", "WIPRO", "INDUSTOWER", "BERGEPAINT", "ZYDUSLIFE", "DMART", "ADANIPORTS", "MINDTREE", "ADANIENT", "TITAN", "JUBLFOOD", "GRASIM", "MARICO", "HDFCBANK", "BRITANNIA", "LUPIN",
             "KOTAKBANK", "DIVISLAB", "M&M", "CIPLA", "BAJAJHLDNG", "MUTHOOTFIN", "INDUSINDBK", "HINDALCO", "NMDC", "HAVELLS", "SRF", "COALINDIA", "HEROMOTOCO", "TECHM", "NAUKRI", "MCDOWELL-N", "SBILIFE", "PNB", "TORNTPHARM", "SBICARD", "DABUR", "DLF", "SUNPHARMA", "ZOMATO", "NTPC", "SIEMENS", "PEL", "BANDHANBNK", "BANKBARODA", "AXISBANK", "SBIN", "HDFCAMC", "POWERGRID", "ITC", "APOLLOHOSP", "ONGC", "PIIND", "TATASTEEL", "LT", "VEDL", "JSWSTEEL", "ICICIBANK", "BAJAJFINSV", "PGHH", "NYKAA", "SAIL", "PAYTM", "ADANIGREEN", "GAIL", "BAJFINANCE", "CHOLAFIN", "LTI"]
a = ['JSWSTEEL', 'TITAN', 'SBIN', 'MARUTI', 'ONGC', 'CHOLAFIN',  'BANDHANBNK', 'TATACONSUM', 'AXISBANK',  'GRASIM', 'ADANITRANS', 'PEL', 'SAIL', 'MINDTREE', 'DLF', 'TECHM', 'DMART', 'HINDALCO', 'UPL', 'INDUSINDBK', 'ADANIENT', 'GAIL', 'LUPIN',
     'EICHERMOT', 'SBICARD', 'MARICO', 'BIOCON', 'NMDC', 'INDUSTOWER', 'MUTHOOTFIN', 'TATAMOTORS', 'KOTAKBANK', 'BPCL', 'INDIGO', 'CIPLA', 'PNB', 'TATASTEEL', 'M&M', 'MCDOWELL-N', 'HDFC', 'BANKBARODA', 'COALINDIA', 'GODREJCP', 'VEDL', 'ICICIBANK', 'ADANIGREEN', 'ADANIPORTS', 'HAVELLS']


class GenerateVolitalityReport(object):
    """
    This script generates volitality report for nifty 100 scrips for past 15 
    days, it skips public holiday.
    This hits nes server to get daily volitality report and merges them, then 
    takes the average of them.

    URL: 
    for volitality report:
        https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_{date}.CSV
    for nse list:
        https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20100
    to download nify 100:
        https://www.nseindia.com/api/equity-stockIndices?csv=true&index=NIFTY%20100
    """

    def __init__(self):
        self.working_dates = self.get_working_dates()
        self.data, self.nify_100 = self.get_nifty100()

    def get_nifty100(self):
        nifty_csv = pd.read_csv('NIFTY-100.csv')
        nifty_csv.columns = nifty_csv.columns.str.strip()
        nify_100 = list(nifty_csv['SYMBOL'])
        return pd.DataFrame(nify_100, columns=['SYMBOL']), nify_100

    def get_report(self):
        dates = self.working_dates
        print(self.working_dates, "here")
        for date in dates:
            try:
                url = f'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_{date}.CSV'
                v_report = pd.read_csv(url)
                filtered_data = v_report.loc[v_report['Symbol'].isin(
                    self.nify_100)]
                report_date = filtered_data.iloc[0]['Date']
                filtered_data = filtered_data[[
                    'Symbol', 'Underlying Annualised Volatility (F) = E*Sqrt(365)']]
                filtered_data = filtered_data.rename(
                    columns={'Underlying Annualised Volatility (F) = E*Sqrt(365)': str(report_date).strip(),
                             'Symbol': 'SYMBOL'})
                filtered_data[f'{str(report_date).strip()}'] = filtered_data[f'{str(report_date).strip()}'].astype(
                    float)
                self.data = pd.merge(self.data, filtered_data, on='SYMBOL')
            except HTTPError as error:
                print(f"{url} has no report")
                continue
            except IndexError as error:
                print(f"{url} has no report")
                continue

    def save_report(self):
        data = self.data.set_index(['SYMBOL'])
        data = data.iloc[:, pd.to_datetime(
            data.columns, format="%d-%b-%Y").argsort()].reset_index()
        data.index = data.index + 1
        data['V AVERAGE'] = data.drop('SYMBOL', axis=1).apply(
            lambda x: x.mean(), axis=1).round(3)
        data = data.sort_values(by=["V AVERAGE"],  ascending=False)
        data.to_csv(f'{datetime.now().strftime("%b-%d-%Y")}-vreport.csv')
        print("Volitality report generated ====> Done\n")

    def get_working_dates(self):
        days = []
        start = datetime.now() - timedelta(5)
        end = datetime.now()
        excluded = (6, 7)
        while start.date() <= end.date():
            if start.isoweekday() not in excluded:
                days.append(start.strftime('%d%m%Y'))
            start += timedelta(days=1)
        return days


if __name__ == '__main__':
    vreport = GenerateVolitalityReport()
    vreport.get_report()
    vreport.save_report()
