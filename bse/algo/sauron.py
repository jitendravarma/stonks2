import time
from datetime import datetime
from pprint import pprint

from bsedata.bse import BSE

from client.udun import Udun
from models import update
from utils import (get_indices, get_losers_gainers, get_stock_quote,
                   get_top_gainers, verify_scrip)

bse = BSE()

CLOCK_MIN = {
    5: [0, 15, 30, 45],
    10: [5, 15, 25, 35, 45, 55],
    15: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
}

ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDQ5ODMyMTcsImV4cCI6MTY0NTA1Nzg1NywibmJmIjoxNjQ0OTgzMjE3LCJhdWQiOlsieDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaURIT3hjczRVZFNHQmJ6Wkh6M0dheE1tcDIycTJpcVlMQnlnd2tZaGZKLU9aVVN2dHY4WGdzZUczMjZybGdLOUlQaVByYW85U18wMEJsRGJZejBiR2FBNEpKVnhDSnpETF9tX3E1R3FzbW92WVh1MD0iLCJkaXNwbGF5X25hbWUiOiJBS0FOS1NIQSBBTklSVURIQSBWQVJNQSIsImZ5X2lkIjoiWEEwMDI5OCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.-AkUDPly90_CsuDlkfzI6guQ0hQNuVA3sa42oSaxWEs"


class Sauron(object):
    def __init__(self, scrip_code, client_code, time_frame, hour, start_candle_min,
                 end_candle_min, take_profit, take_profit_sell, quantity=10, stop_loss=1):
        self.scrip_data = {
            "price_at_candle_start": "",
            "price_at_candle_end": "",
            "trade_enter_time": "",
            "trade_exit_time": "",
            "entry_price": "",
            "exit_price": "",
            "stop_loss": "",
            "stop_loss_price": "",
            "quantity": quantity,
            "scrip_no": "",
            "name": "",
            "previous_close": "",
            "max_session_price": "",
            "min_session_price": "",
            "order": "",
            "take_profit": "",
            "trade_complete": False
        }
        self.quantity = quantity
        self.scrip_code = scrip_code
        self.start_candle_min = start_candle_min
        self.end_candle_min = end_candle_min
        self.time_frame = time_frame
        self.take_profit = take_profit
        self.hour = hour
        self.minute_range = CLOCK_MIN[time_frame]
        self.price_range_of_session = []
        self.stop_loss = stop_loss
        self.client = Udun(ACCESS_TOKEN)
        self.client_code = client_code
        self.order_id = None
        self.take_profit_sell = take_profit_sell

    def analyze_scrip(self):
        now = datetime.now()
        pprint(f"Time to get quote: {now.hour}, {now.minute}, {now}")
        quote = get_stock_quote(bse, self.scrip_code)
        current_value = quote["currentValue"]
        pprint("*"*50)
        print(f"current value: {current_value}")
        pprint(self.scrip_data)
        pprint(self.client.get_profile())
        pprint(self.price_range_of_session)
        print(now.hour, self.hour, now.minute, self.minute_range,
              self.start_candle_min, self.end_candle_min)
        if now.hour == self.hour and now.minute in self.minute_range:
            pprint("*"*50)
            pprint(quote)
            self.price_range_of_session.append(quote["currentValue"])
            if now.minute == self.start_candle_min:
                self.scrip_data["name"] = quote["companyName"]
                self.scrip_data["scrip_no"] = quote["scripCode"]
                self.scrip_data["previous_close"] = quote["previousClose"]
                self.scrip_data["price_at_candle_start"] = quote["currentValue"]
            if now.minute == self.end_candle_min:
                self.scrip_data["price_at_candle_end"] = quote["currentValue"]
                self.scrip_data["max_session_price"] = max(self.price_range_of_session)
                self.scrip_data["min_session_price"] = min(self.price_range_of_session)
                pprint(f"end of last concentration candle: {self.scrip_data } \n")
            return

        if self.scrip_data["price_at_candle_end"] and not self.scrip_data["trade_enter_time"] and \
                now.minute in [5, 15, 25, 35, 45, 55]:
            print(self.scrip_data["max_session_price"])
            print(self.scrip_data["min_session_price"])
            print("checking trade cnd1", current_value > self.scrip_data["max_session_price"])
            print("checking trade cdn2", current_value < self.scrip_data["min_session_price"],
                  "should trigger sell")
            # if current candles last price breaks 1035 candles high then buy
            if current_value > self.scrip_data["max_session_price"]:
                pprint(current_value, self.scrip_data["max_session_price"],
                       "should trigger buy")
                # define stop loss for buy side
                stop_loss = float(self.scrip_data["min_session_price"]) - self.stop_loss
                target = current_value + self.take_profit
                # place buy order on fyers

                # symbol, side, limit_price, sl, quantity, take_profit=2
                response = self.client.place_order(
                    symbol=self.client_code, side=1, limit_price=current_value, sl=self.stop_loss,
                    quantity=self.quantity, take_profit=self.take_profit)
                # {
                #     "s": "ok",
                #     "code": 1101,
                #     "message": "Order submitted successfully. Your Order Ref. No.808058117761",
                #     "id": "808058117761"
                # }
                print(f"client response\n {response}")
                if response["s"] == 'ok':
                    self.order_id = response["id"]

                self.scrip_data["order"] = "BUY"
                self.scrip_data["stop_loss_price"] = stop_loss
                self.scrip_data["take_profit"] = float(current_value) + self.take_profit

            # if current candles last price breaks 1035 candles low then short sell
            if current_value < self.scrip_data["min_session_price"]:
                pprint(current_value, self.scrip_data["min_session_price"],
                       "should trigger sell")
                # define stop loss for sell side
                stop_loss = float(self.scrip_data["max_session_price"]) + self.stop_loss
                target = current_value - self.take_profit_sell
                # place sell order on fyers
                response = self.client.place_order(
                    symbol=self.client_code, side=-1, limit_price=current_value,
                    sl=self.stop_loss, quantity=self.quantity,
                    take_profit=self.take_profit_sell)
                print(f"client response\n {response}")
                if response["s"] == 'ok':
                    self.order_id = response["id"]

                self.scrip_data["order"] = "SELL"
                self.scrip_data["stop_loss_price"] = stop_loss
                self.scrip_data["take_profit"] = float(current_value) - self.take_profit_sell
            # setting take_profit
            self.scrip_data["entry_price"] = current_value
            self.scrip_data["trade_enter_time"] = datetime.now()
            pprint(f"scrip data afer trade taken: {self.scrip_data } \n")

        # if self.scrip_data["trade_enter_time"]:

            # if self.scrip_data["order"] == "SELL":
            #     if float(self.scrip_data["entry_price"]) - \
            #             float(current_value) >= self.take_profit:
            #         pprint("take_profit achieved for short selling")
            #         pprint(self.scrip_data["entry_price"], current_value)
            #         self.scrip_data["trade_exit_time"] = datetime.now()
            #         self.scrip_code["trade_complete"] = True
            #     if float(self.scrip_data["stop_loss_price"]) > float(current_value):
            #         self.scrip_data["trade_exit_time"] = datetime.now()
            #         self.scrip_data["stop_loss_price"] = current_value
            #         pprint("stop loss hit for sell side")
            #         pprint(self.scrip_data["entry_price"], current_value)
            #         self.scrip_code["trade_complete"] = True
            # else:
            #     if float(current_value) - \
            #             float(self.scrip_data["entry_price"]) >= self.take_profit:
            #         pprint("take_profit achieved for buying")
            #         pprint(current_value, self.scrip_data["entry_price"])
            #         self.scrip_data["trade_exit_time"] = datetime.now()
            #         self.scrip_code["trade_complete"] = True
            #     if float(current_value) > float(self.scrip_data["stop_loss_price"]):
            #         self.scrip_data["trade_exit_time"] = datetime.now()
            #         self.scrip_data["stop_loss_price"] = current_value
            #         pprint("stop loss hit for sell side")
            #         pprint(self.scrip_data["entry_price"], current_value)
            #         self.scrip_code["trade_complete"] = True
        if self.scrip_data["trade_complete"]:
            update("udun", self.scrip_code)
            exit()
