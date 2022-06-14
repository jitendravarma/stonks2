from backtest import Diva
from pprint import pprint
from operator import itemgetter
from pprint import pprint
from constants import VSCRIPS, format_data

import pandas as pd


# VSCRIPS = ['DLF']

final_result = []
min_percent = 50

VSCRIPS = [{'name': 'INDUSTOWER', 'atr': 3.5, 'price': 547.0}]
for scrip in VSCRIPS:
    diva = Diva(SCRIP_NAME=f"NSE:{scrip['name']}-EQ", DAY_RANGE=18, TIME_FRAME=10,
                START_DELTA=0, SLEEP=0.3)
    diva.BO_CANDLE_HR = 13
    diva.BO_CANDLE_MIN = 25
    diva.STOP_LOSS_PERCENTAGE = .1
    diva.TARGET_IN_PERCENTAGE = .5
    diva.GET_DAILY_DATA = True
    diva.ATR = None
    # diva.FIRST_TARGET_SIZE = 3

    result = diva.meow()
    print(result)
    if result['win_%'] >= min_percent and result['total_target_count'] > result['total_sl_count']:
        final_result.append(result)
    # if result['total_sl_count'] > 100:
    #     final_result.append(result)

daily_data = []
custom_index = []
for data in final_result:
    daily_data.append(data['daily_data'])
    custom_index.append(data['scrip_name'])
    print(data['sl_with_atr'], data['scrip_name'],
          data['total_sl_days'], data['sl_hit_days'])

point_df = pd.DataFrame(daily_data, index=custom_index)
point_df["Total"] = point_df.sum(axis=1)
point_df["Total"] = point_df["Total"].round(2)
point_df = point_df.sort_values('Total')


score_df = []
atr_values = []
for data in final_result:
    atr_values.append({data['scrip_name']: data['values']})
    score_df.append(format_data(data))

print("\n")
print("Printing atr values")
(print(atr_values))

print("\n")
print("Printing points df")
print(print(point_df))
print("\n")
print("Printing final amount")
df = pd.DataFrame(sorted(score_df, key=itemgetter('FinalAmt')))
print(df)


# tsteel 10:00 am Tf 15
# Target 4rs  Total Points 42  win 100%

# sbin 10:00 am Tf 15
# Target 3.5 rs sl 3.50 Total Points 21.5 win 50%

# adani ports 10:00 am Tf 15
# Target 3rs Sl 14rs Total Points 33.25 win 85.71%

# chola finance 930 am Tf 15
# Target 4.5  sl 13 Total Points 36.55 Win 64.29%

# Indusind 10:am TF 15
# Target 3.5rs sl 4.35 Total Points 34.15  Win 79%
