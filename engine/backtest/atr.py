import time
import sys
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

from constants import ACCESS_TOKEN, VSCRIPS

sys.path.append('../')


# days = df['Time'].dt.day
# list(set(days))[1:]
client = None


def get_date_string(date):
    return date.strftime('%Y-%m-%d')


def get_average(min, max):
    return round((min+max)/2, 2)


def get_working_days(df):
    return list(set(df['Time'].dt.day))[1:]


def get_data(symbol, time_delta):
    today = datetime.now()
    first_date = today - timedelta(time_delta + 1)
    data = {"symbol": f"NSE:{symbol}-EQ", "resolution": "15",
            "range_from":  get_date_string(first_date),
            "range_to": get_date_string(today),
            "date_format": "1", "cont_flag": "1"}

    data = client.get_history(data)
    df = pd.DataFrame(data['candles'], columns=[
        "Time", "Open Value", "Highest Value", "Lowest Value", "Close Value", "Volume"])
    df['Time'] = df['Time'].apply(
        lambda x:  datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
    df['Name'] = symbol
    return df


def get_atr_diffs(df):
    high_low = df['Highest Value'] - df['Lowest Value']
    high_close = np.abs(df['Highest Value'] - df['Close Value'].shift())
    low_close = np.abs(df['Lowest Value'] - df['Close Value'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    atr = true_range.rolling(14).sum()/14
    df['ATR'] = atr
    return df


def get_mean_atr(df):
    days = get_working_days(df)
    mean_atr = []
    print(days)
    for day in days:
        data = df[df['Time'].dt.day == day]
        max_atr = data['ATR'].max()
        min_atr = data['ATR'].min()
        mean = get_average(min_atr, max_atr)
        mean_atr.append(mean)
    return sum(mean_atr)/len(mean_atr)


def main():
    from client.udun import Udun
    global client
    client = Udun(ACCESS_TOKEN)
    result = []
    for script in VSCRIPS:
        time.sleep(.05)
        df = get_data(script['name'], 14)
        average_atr = get_atr_diffs(df)
        mean = get_mean_atr(average_atr)
        result.append({"name": script['name'], "atr":  round(
            mean, 2), "price": df.iloc[-1]['Close Value']})
    return result


result = main()
print(result)
