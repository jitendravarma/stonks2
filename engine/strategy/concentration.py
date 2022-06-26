from argparse import ArgumentParser
import traceback

import pandas as pd

import time
from datetime import datetime, timedelta

import schedule

import sys
sys.path.append('..')  # nopep8

from client.udun import Udun
from logs.loggin import get_logger

from backtest.constants import ACCESS_TOKEN, TIME_FRAME_INTERVAL


# python concentration.py -tf 15 -hr 9 -m 15 -s HINDALCO -tp 0.5 -sl 0.1 -qt 1
# ConcentrationWatcher(7, 15, 5, "HINDALCO", 0.5, 0.1, 1)

logger = get_logger('logs/concentration/')


class ConcentrationWatcher(object):
    def __init__(self, START_HOUR, START_MIN, TIME_FRAME, TAKE_PROFIT,
                 STOPLOSS_BUFFER, QUANTITY, SCRIP) -> None:
        self.START_HOUR = START_HOUR
        self.START_MIN = START_MIN
        self.TIME_FRAME = TIME_FRAME
        self.TAKE_PROFIT = TAKE_PROFIT
        self.STOPLOSS_BUFFER = STOPLOSS_BUFFER
        self.QUANTITY = QUANTITY
        self.SCRIP = f"NSE:{SCRIP}-EQ"
        self.ORDER_ID = None
        self.TRADE_EXECUTED = False
        self.HAS_DATA = False
        self.CONCENTRATION_CANDLE = {}
        self.CLIENT = Udun(ACCESS_TOKEN)
        self.INTERVALS = TIME_FRAME_INTERVAL[self.TIME_FRAME]

    def floor(self, value):
        return round(value + (0.05-value) % 0.05, 2)

    def get_date_string(self, date):
        return date.strftime('%Y-%m-%d')

    def get_histroy(self, symbol, timeframe):
        today = datetime.now()
        data = {
            "symbol": symbol, "resolution": f"{timeframe}",
            "date_format": "1", "range_from":  self.get_date_string(today),
            "range_to":  self.get_date_string(today), "cont_flag": "1"}
        return self.CLIENT.get_history(data)

    def get_data(self, start_hour, start_min, symbol, timeframe=15):
        try:
            # data = get_historical_data(symbol, timeframe, barsize)
            data = self.get_histroy(symbol, timeframe)
            df = pd.DataFrame(data['candles'], columns=[
                "time", "o", "h", "l", "c", "v"])

            # convert epoch time to normal datetime
            df['time'] = df['time'].apply(
                lambda x:  datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
            # convert date string to date time object
            df['time'] = pd.to_datetime(df['time'], errors='coerce')
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

    def place_order(self, client_code, stop_loss, current_value, side, take_profit):
        response = self.CLIENT.place_order(
            symbol=client_code, side=side, limit_price=current_value, sl=stop_loss,
            quantity=self.QUANTITY, take_profit=take_profit)
        print(response)
        logger.critical(response)
        if response["s"] == 'ok':
            self.ORDER_ID = response["id"]
            logger.critical(self.ORDER_ID)
            self.TRADE_EXECUTED = True
            exit()
        return response

    def caller(self, side, fyers_code,  current_price, candle_max_or_min):
        take_profit_in_rs = self.floor(current_price * (self.TAKE_PROFIT/100))
        # it can be either side sell or buy
        stop_loss = self.floor(
            abs(current_price - candle_max_or_min) + (self.STOPLOSS_BUFFER * current_price)/100)

        self.place_order(fyers_code, abs(stop_loss),
                         current_price, side, take_profit_in_rs)
        print(
            f"Side {side} breakout {current_price} at {'low' if side == -1 else 'high'} of concentration candle take profit {take_profit_in_rs}")
        logger.critical(
            f"Side {side} breakout {current_price} at {'low' if side == -1 else 'high'}  of concentration candle take profit {take_profit_in_rs}")

    def start(self):

        now = datetime.now()
        if now.hour < self.START_HOUR:
            logger.warning("its no time to start work")
            return

        if not self.HAS_DATA:
            self.CONCENTRATION_CANDLE = self.get_data(
                self.START_HOUR, self.START_MIN, self.SCRIP, timeframe=15)
            if not self.CONCENTRATION_CANDLE:
                logger.critical(
                    f"no data found for {now.hour}  {now.minute} 1 ")
                return
            print(self.CONCENTRATION_CANDLE, "concentration candle \n")
            self.HAS_DATA = True
            logger.critical("logged data for concentration candle")
            return

        if now.minute in self.INTERVALS:
            print("\n")
            print({"START_HOUR": self.START_HOUR, "START_MIN": self.START_MIN, "TIME_FRAME": TIME_FRAME,
                   "TAKE_PROFIT": self.TAKE_PROFIT, "STOPLOSS_BUFFER": self.STOPLOSS_BUFFER, "QUANTITY": QUANTITY})
            self.CONCENTRATION_CANDLE = self.get_data(
                self.START_HOUR, self.START_MIN, self.SCRIP, timeframe=15)
            check_minute = self.INTERVALS[self.INTERVALS.index(now.minute)-1]
            data = self.get_data(
                now.hour, check_minute, self.SCRIP, timeframe=15)
            if not data:
                print(
                    f"no data found for {now.hour}  {now.minute} 2")
                logger.critical(
                    f"no data found for {now.hour}  {now.minute} 2")
                return
            current_price = data['close']
            concentration_min = self.CONCENTRATION_CANDLE['low']
            concentration_max = self.CONCENTRATION_CANDLE['high']
            print("\n")
            print("\n", concentration_min, concentration_max, current_price)
            print(self.TAKE_PROFIT, "=="*10)

            if current_price < concentration_min:
                self.caller(-1, self.SCRIP, current_price, concentration_max)
                # take_profit_in_rs = floor(current_price * (TAKE_PROFIT/100))
                # stop_loss = floor(concentration_max -
                #                   current_price + (STOPLOSS_BUFFER * current_price)/100)
                # place_order(fyers_code, abs(stop_loss),
                #             current_price, -1, take_profit_in_rs)
                # print(
                #     f"breakout {current_price} at low of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
                # logger.critical(
                #     f"breakout {current_price} at low of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
            elif current_price > concentration_max:
                self.caller(1, self.SCRIP, current_price, concentration_min)
                # take_profit_in_rs = floor(current_price * (TAKE_PROFIT/100))
                # stop_loss = floor(
                #     current_price - concentration_min + (STOPLOSS_BUFFER * current_price)/100)
                # place_order(
                #     fyers_code, abs(stop_loss), current_price, 1, take_profit_in_rs)
                # print(
                #     f"breakout {current_price} at high of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
                # logger.critical(
                #     f"breakout {current_price} at high of concentration candle {concentration_min}-{concentration_max}, take profit {take_profit_in_rs}")
            else:
                logger.info(
                    f"price {current_price} still in range of {concentration_min}-{concentration_max}")
        else:
            logger.info("skipping: current time is not in time frame")


# start()
main = ConcentrationWatcher(START_HOUR=7, START_MIN=15, TIME_FRAME=5,
                            TAKE_PROFIT=0.5, STOPLOSS_BUFFER=0.1,
                            QUANTITY=1, SCRIP="HINDALCO")


# def __init__(self, START_HOUR, START_MIN, TIME_FRAME, TAKE_PROFIT,
#              STOPLOSS_BUFFER, QUANTITY, SCRIP) -> None:


try:

    print(
        f"\nStarted for {main.SCRIP} Time: {main.START_HOUR}-{main.START_MIN}, TF: {main.TIME_FRAME} \
            Take profit:{main.TAKE_PROFIT} SL:{main.STOPLOSS_BUFFER}")
except Exception as error:
    print("Error getting profile, issue with token")
    traceback.print_exc()
    exit()

schedule.every(10).seconds.do(main.start)

while True:
    schedule.run_pending()
    time.sleep(1)
