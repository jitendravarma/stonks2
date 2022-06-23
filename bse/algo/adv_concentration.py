from datetime import datetime
import pandas as pd
import traceback
from pprint import pprint
from client.udun import Udun
import time

from backtest.constants import ACCESS_TOKEN, VSCRIPS


client = Udun(ACCESS_TOKEN)


# VSCRIPS = ['DLF']

final_result = []
min_percent = 50

# VSCRIPS = [{'name': 'INDUSTOWER', 'atr': 3.5, 'price': 547.0}]


def floor(value):
    return round(value + (0.05-value) % 0.05, 2)


def get_date_string(date):
    return date.strftime('%Y-%m-%d')


def get_histroy(symbol):
    today = datetime.now()
    data = {
        "symbol": symbol, "resolution": "10",
        "date_format": "1", "range_from": get_date_string(today),
        "range_to": get_date_string(today), "cont_flag": "1"}
    return client.get_history(data)


def get_data(symbol, timeframe="15min"):
    try:
        # data = get_historical_data(symbol, timeframe, barsize)
        data = get_histroy(symbol)
        df = pd.DataFrame(data['candles'], columns=[
                          "t", "o", "h", "l", "c", "v"])

        # convert epoch time to normal datetime
        df['t'] = df['t'].apply(
            lambda x:  datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
        # convert date string to date time object
        df['t'] = pd.to_datetime(df['t'], errors='coerce')
        df['cbs'] = df['c'] - df['o']
        df['cs'] = df['h'] - df['l']
        return df[(df['t'].dt.hour == 9) & (df['t'].dt.minute <= 25)]
    except Exception as error:
        print(error)
        print(data)
        print(symbol)
        print(traceback.print_exc())
        # exit()
        return None


def check_ohol(df):

    first = df.iloc[0]
    second = df.iloc[1]
    if first['o'] <= first['l'] and second['c'] >= first['c']:
        return True, f"OL watch above {second['c']} sl {second['l']} =====> O=L"
    if first['o'] >= first['h'] and second['c'] <= first['c']:
        return True, f"OH watch below {second['c']} sl {second['c']} =====> O=H"
    if first['l'] < second['l'] and second['c'] >= first['h']:
        return True, f"OL watch above {second['c']} sl {second['c']}"
    if first['h'] > second['h'] and second['c'] <= first['l']:
        return True, f"OH watch below {second['c']} sl {second['c']}"
    return False, None


print("Advanced concentration method!")

for scrip in VSCRIPS:
    time.sleep(.3)
    try:
        td_code = f"NSE:{scrip['name']}-EQ"
        CONCENTRATION_CANDLE = get_data(td_code, timeframe="10")
        if CONCENTRATION_CANDLE.empty:
            continue
        response, msg = check_ohol(CONCENTRATION_CANDLE)
        if response:
            print(scrip['name'], msg)
    except Exception as error:
        continue
