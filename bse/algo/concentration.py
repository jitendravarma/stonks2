from argparse import ArgumentParser
import traceback
import pandas as pd


import time
from datetime import datetime

import schedule

from client.udun import Udun

from loggin import get_logger

from backtest.constants import ACCESS_TOKEN

parser = ArgumentParser()
parser.add_argument("-tf", "--timeframe", dest="time_frame",
                    help="Please provide timeframe as 5,10 and 15 min", metavar="TIMEFRAME",
                    required=True,)
parser.add_argument("-hr", "--hour", dest="start_hour",
                    help="Please provide start hour", metavar="HOUR", required=True)
parser.add_argument("-m", "--minute", dest="start_minute",
                    help="Please provide timeframe as 5,10 and 15 min", metavar="MINUTE", required=True)
parser.add_argument("-s", "--scrip", dest="scrip_name",
                    help="Scrip names like SBIN, TATASTEEL", metavar="TAKEPROFIT", required=True)
parser.add_argument("-tp", "--takeprofit", dest="take_profit",
                    help="Add what amount of profit you will like to take home", metavar="SCRIP", required=True)
parser.add_argument("-sl", "--stoploss_buffer", dest="stoploss_buffer",
                    help="Whats the stop loss buffer for your concentration candle", metavar="SL_BUFFER", required=True)
parser.add_argument("-qt", "--quantity", dest="quantity",
                    help="Quantity to trade for", metavar="SL_BUFFER", required=True)
parser.add_argument("-atr", "--atr", dest="atr" or 0,
                    help="ATR for the script", metavar="ATR", required=False or 0)


parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

args = parser.parse_args()

logger = get_logger('logs/concentration/')

TIME_FRAME_INTERVAL = {
    5: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    10: [5, 15, 25, 35, 45, 55],
    15: [0, 15, 30, 45],
}

# start hour and start minute for the candle to observe
START_HOUR = int(args.start_hour)

# START_MIN = 15
START_MIN = int(args.start_minute)

# time frame for the concentration method
TIME_FRAME = int(args.time_frame)
TAKE_PROFIT = float(args.take_profit)
STOPLOSS_BUFFER = float(args.stoploss_buffer)

ATR = float(args.atr or 0)

QUANTITY = int(args.quantity)

SCRIP = args.scrip_name

print("\nStarting........")
print({"START_HOUR": START_HOUR, "START_MIN": START_MIN, "TIME_FRAME": TIME_FRAME,
      "TAKE_PROFIT": TAKE_PROFIT, "STOPLOSS_BUFFER": STOPLOSS_BUFFER, "QUANTITY": QUANTITY})

INTERVALS = TIME_FRAME_INTERVAL[TIME_FRAME]
BAR_SIZE = {5: "5min", 10: "10min", 15: "15min"}
# to store values for a given candle at x time frame
CANDLE = []
ORDER_ID = ""


CONCENTRATION_CANDLE = {}
HAS_DATA = False

client = Udun(ACCESS_TOKEN)

# python concentration.py -tf 15 -hr 9 -m 15 -s HINDALCO -tp 0.5 -sl 0.1 -qt 1


def place_order(client_code, stop_loss, current_value, side, take_profit):
    global ORDER_ID
    response = client.place_order(
        symbol=client_code, side=side, limit_price=current_value, sl=stop_loss,
        quantity=QUANTITY, take_profit=take_profit)
    print(response)
    logger.critical(response)
    if response["s"] == 'ok':
        ORDER_ID = response["id"]
        logger.critical(ORDER_ID)
        exit()
    return response


def floor(value):
    return round(value + (0.05-value) % 0.05, 2)


def get_date_string(date):
    return date.strftime('%Y-%m-%d')


def get_histroy(symbol, timeframe):
    today = datetime.now()
    data = {
        "symbol": symbol, "resolution": f"{timeframe.strip('min')}",
        "date_format": "1", "range_from": get_date_string(today),
        "range_to": get_date_string(today), "cont_flag": "1"}
    return client.get_history(data)


def get_data(start_hour, start_min, symbol, timeframe="1 D", barsize="15min"):
    try:
        # data = get_historical_data(symbol, timeframe, barsize)
        data = get_histroy(symbol, timeframe)
        df = pd.DataFrame(data['candles'], columns=[
                          "time", "o", "h", "l", "c", "v"])

        # convert epoch time to normal datetime
        df['time'] = df['time'].apply(
            lambda x:  datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
        # convert date string to date time object
        df['time'] = pd.to_datetime(df['time'], errors='coerce')

        print(df)
        df = df[(df['time'].dt.hour == start_hour)
                & (df['time'].dt.minute == start_min)]
        if df.empty:
            return None
        return {"open": float(df['o']), "close": float(df['c']), "high": float(df['h']), "low": float(df['l']),
                "volume": float(df['v']), "time": df['time']}
    except Exception as error:
        print(error)
        print(traceback.print_exc())
        # exit()
        return None


def start():
    global CONCENTRATION_CANDLE
    global HAS_DATA
    global ORDER_ID
    td_code = SCRIP
    fyers_code = f"NSE:{SCRIP}-EQ"
    now = datetime.now()
    bar_size = BAR_SIZE[TIME_FRAME]
    if now.hour < START_HOUR:
        logger.warning("its no time to start work")
        return

    if ORDER_ID:
        logger.warning(
            f"Already in trade with Order id {ORDER_ID}")
        return
    print(get_histroy(fyers_code, bar_size), "\n")
    if not HAS_DATA:
        CONCENTRATION_CANDLE = get_data(
            START_HOUR, START_MIN, td_code, timeframe="1 D", barsize=bar_size)
        if not CONCENTRATION_CANDLE:
            logger.critical(
                f"no data found for {now.hour}  {now.minute} 1 ")
            return
        print(CONCENTRATION_CANDLE, "concentration candle \n")
        HAS_DATA = True
        logger.critical("logged data for concentration candle")
        return
    print("\n", CONCENTRATION_CANDLE)
    print("")
    print(now.minute, INTERVALS, fyers_code)
    if now.minute in INTERVALS:
        print("\n")
        print({"START_HOUR": START_HOUR, "START_MIN": START_MIN, "TIME_FRAME": TIME_FRAME,
               "TAKE_PROFIT": TAKE_PROFIT, "STOPLOSS_BUFFER": STOPLOSS_BUFFER, "QUANTITY": QUANTITY})
        CONCENTRATION_CANDLE = get_data(
            START_HOUR, START_MIN, td_code, timeframe="1 D", barsize=bar_size)
        check_minute = INTERVALS[INTERVALS.index(now.minute)-1]
        print(now.hour, check_minute, now.minute)
        data = get_data(
            now.hour, check_minute, td_code, timeframe="1 D", barsize=bar_size)
        print(data)
        if not data:
            print(
                f"no data found for {now.hour}  {now.minute} 2")
            logger.critical(
                f"no data found for {now.hour}  {now.minute} 2")
            return
        current_price = data['close']
        concentration_min = CONCENTRATION_CANDLE['low']
        concentration_max = CONCENTRATION_CANDLE['high']
        print("\n")
        print(concentration_min, concentration_max, current_price)
        print(TAKE_PROFIT, "=="*10)
        if current_price < concentration_min:
            stop_loss = floor(concentration_max -
                              current_price + (STOPLOSS_BUFFER * current_price)/100)
            take_profit_in_rs = floor(current_price * (TAKE_PROFIT/100))
            place_order(fyers_code, abs(stop_loss),
                        current_price, -1, take_profit_in_rs)
            print(
                f"breakout {current_price} at low of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
            logger.critical(
                f"breakout {current_price} at low of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
        elif current_price > concentration_max:
            take_profit_in_rs = floor(current_price * (TAKE_PROFIT/100))
            stop_loss = floor(
                current_price - concentration_min + (STOPLOSS_BUFFER * current_price)/100)
            place_order(
                fyers_code, abs(stop_loss), current_price, 1, take_profit_in_rs)
            print(
                f"breakout {current_price} at high of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
            logger.critical(
                f"breakout {current_price} at high of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
        else:
            logger.info(
                f"price {current_price} still in range of {concentration_min}-{concentration_max}")
    else:
        logger.info("skipping: current time is not in time frame")


# start()
try:
    print(client.get_profile())
    print(
        f"\nStarted for {SCRIP} Time: {START_HOUR}-{START_MIN}, TF: {TIME_FRAME} \
            Take profit:{TAKE_PROFIT} SL:{STOPLOSS_BUFFER}")
except Exception as error:
    print("Error getting profile, issue with token")
    traceback.print_exc()
    exit()

schedule.every(10).seconds.do(start)

while True:
    schedule.run_pending()
    time.sleep(1)
