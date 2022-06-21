import calendar
from re import A
from unittest import result
import pandas as pd
from datetime import date, datetime, timedelta

from nsepy import get_history

nifty_100 = pd.read_csv('NIFTY_100.csv')['SYMBOL \n'][1:]

now = datetime.now()

current_month = now.month
today = now.day
previous_month = (date.today().replace(day=1) - timedelta(days=1)).month

month_start_date = 1
last_day_of_previous_month = calendar.monthrange(now.year, previous_month)[1]

results = pd.DataFrame()
results = []

# get_history(symbol="ADANIGREEN", start=date(2022, 3, 1), end=date(2022, 3, 31))


def get_max(data, name):
    return data[name].max()


def get_max_on(data, name):
    return data[name].idxmax()


def get_first_max(data, value, name):
    result = data[data[name].gt(value)]
    if not result.empty:
        row_index = data[data[name].gt(value)].index[0]
        return data.iloc[row_index][name]
    return None


def correct_colums(data):
    data.to_csv('tmp.csv')
    return pd.read_csv('tmp.csv')


def check_breakout(index):
    # get current months data
    current_month_data = get_history(symbol=index, start=date(
        2022, current_month, month_start_date), end=date(2022, current_month, today))

    current_month_data = correct_colums(current_month_data)

    # get last months data
    previous_month_data = get_history(symbol=index, start=date(
        2022, previous_month, month_start_date), end=date(2022, previous_month, last_day_of_previous_month))

    previous_month_data = correct_colums(previous_month_data)

    # get previous months max volume
    previous_month_max_volume = get_max(previous_month_data, 'Volume')

    # get current months max volume
    current_month_max_volume = get_first_max(
        current_month_data, previous_month_max_volume, 'Volume')

    if not current_month_max_volume:
        print('not having max volumne for current month')
        return

    previous_month_max_delivery = get_max(
        previous_month_data, 'Deliverable Volume')
    current_month_max_delivery = get_first_max(
        current_month_data, previous_month_max_delivery, 'Deliverable Volume')

    if not current_month_max_delivery:
        print(previous_month_max_delivery)
        print('not having max del volumne for current month')
        return
    print(previous_month_max_delivery, previous_month_max_volume)
    print(current_month_max_delivery, current_month_max_volume)

    if(current_month_max_volume > previous_month_max_volume) and \
            (current_month_max_delivery > previous_month_max_delivery):
        print(f"Monthly volume breakout confirmed in {index}")
        results.append(current_month_data.loc[get_max_on(
            current_month_data, 'Deliverable Volume')])
        results.append(previous_month_data.loc[
            get_max_on(previous_month_data, 'Deliverable Volume')])


def main():
    for index in nifty_100:
        check_breakout(index)
    results_df = pd.DataFrame(results)
    results_df['Date'] = pd.to_datetime(
        results_df['Date']).dt.strftime('%d-%m-%Y')
    results_df.reset_index(drop=True, inplace=True)
    results_df.to_csv(
        f"{now.date().strftime('%d-%m-%Y')}-MONTHLY-BREAKOUT.csv")


if __name__ == '__main__':
    main()

# pd.to_datetime(d['Date'].astype(str), format='%d/%m/%Y')
