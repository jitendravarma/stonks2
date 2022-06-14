from datetime import datetime
import itertools
from backtest import Diva
from pprint import pprint
from operator import itemgetter
from pprint import pprint
from constants import VSCRIPS, format_data

import pandas as pd


final_result = []
min_percent = 50

TIME_FRAME = [
    (10, 9, 15), (10, 9, 25), (10, 9, 35), (10, 9, 45),
    (10, 9, 55), (10, 10, 5), (10, 10, 15), (10, 13, 15), (10, 13, 25),
    (15, 9, 15), (15, 9, 30), (15, 9, 45), (15, 10, 0), (15, 10, 15),
    (15, 13, 15), (15, 13, 30)
]

# TIME_FRAME = [
#     (10, 9, 15), (10, 9, 25), (10, 9, 35), (10, 9, 45),
# ]

# VSCRIPS = [
#     # {'name': 'JSWSTEEL', 'atr': 4.29, 'price': 726.35},
#     # {'name': 'TITAN', 'atr': 10.26, 'price': 2507.0},
#     {'name': 'ICICIBANK', 'atr': 3.14, 'price': 747.5},
#     {'name': 'WIPRO', 'atr': 0.65, 'price': 164.7},
# ]


def generator(DAY_RANGE=18, STOP_LOSS_PERCENTAGE=0.1, TARGET_IN_PERCENTAGE=0.5,
              SLEEP=0.4, scripts=VSCRIPS):
    for tf in TIME_FRAME:
        temp_result = []
        for scrip in scripts:
            diva = Diva(SCRIP_NAME=f"NSE:{scrip['name']}-EQ", DAY_RANGE=DAY_RANGE,
                        TIME_FRAME=tf[0], START_DELTA=0, SLEEP=0.3)
            diva.BO_CANDLE_HR = tf[1]
            diva.BO_CANDLE_MIN = tf[2]
            diva.STOP_LOSS_PERCENTAGE = STOP_LOSS_PERCENTAGE
            diva.TARGET_IN_PERCENTAGE = TARGET_IN_PERCENTAGE
            diva.GET_DAILY_DATA = True
            diva.ATR = None
            diva.SLEEP = SLEEP
            # diva.FIRST_TARGET_SIZE = 3

            result = diva.meow()
            if result['win_%'] >= min_percent and result['total_target_count'] > result['total_sl_count']:
                temp_result.append(format_data(result))
        final_result.extend(temp_result)


generator()
# pprint(final_result)
df = pd.DataFrame(sorted(final_result, key=itemgetter('FinalAmt')))
df.to_csv(f'{datetime.now().strftime("%b-%d-%Y")}-final.csv')


best_of_first = df.iloc[-20:]
best_of_first = [{'name': item.replace("NSE:", "").replace(
    "-EQ", "")} for item in best_of_first['Name']]

final_result = []
generator(DAY_RANGE=18, STOP_LOSS_PERCENTAGE=0.1, TARGET_IN_PERCENTAGE=1,
          SLEEP=0.4, scripts=best_of_first)

df = pd.DataFrame(sorted(final_result, key=itemgetter('FinalAmt')))
print(df)
df.to_csv(f'{datetime.now().strftime("%b-%d-%Y")}-one.csv')
