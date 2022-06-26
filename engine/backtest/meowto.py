from concentration import BTConcentration

import pandas as pd

# Sail 1k 82 117
# HDFC 22 52 82
# adna 60 56 86
# chola 70 56 85
# sbin 100 53 83

# 230+110+120+120+120
VSCRIPS = [
    {
        "name": 'UPL', "target": .5,
        "hr": 9, "min": 15, "tf": 10,
        "sl_percentage": .1, "quantity": 64  # 10047
    },
    {
        "name": 'BIOCON', "target": .5,
        "hr": 9, "min": 15, "tf": 10,
        "sl_percentage": .1, "quantity": 145  # 10110
    },
    {
        "name": 'JINDALSTEL', "target": .5,
        "hr": 10, "min": 5, "tf": 10,
        "sl_percentage": .1, "quantity": 100  # 10110
    },
    {
        "name": 'LUPIN', "target": .5,
        "hr": 9, "min": 30, "tf": 15,
        "sl_percentage": 1, "quantity": 69  # 10110
    },
]


daily_data = []
custom_index = []


for scrip in VSCRIPS:
    diva = BTConcentration(
        SCRIP_NAME=f"NSE:{scrip['name']}-EQ", DAY_RANGE=18, TIME_FRAME=scrip['tf'])
    diva.BO_CANDLE_HR = scrip['hr']
    diva.BO_CANDLE_MIN = scrip['min']
    diva.STOP_LOSS_PERCENTAGE = scrip['sl_percentage']
    diva.TARGET_IN_PERCENTAGE = scrip['target']
    diva.GET_DAILY_DATA = True
    diva.QUANTITY = scrip["quantity"]
    # diva.FIRST_TARGET_SIZE = 3

    data = diva.meow()
    daily_data.append(data['daily_data'])
    custom_index.append(data['scrip_name'])

point_df = pd.DataFrame(daily_data, index=custom_index)
point_df['GT'] = point_df.sum(axis=1)
point_df.loc['Total'] = point_df.sum(axis=0, skipna=True)

print("\n")
print("Printing points df")
print(print(point_df))
print("\n")
