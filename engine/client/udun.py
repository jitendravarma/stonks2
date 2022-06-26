from fyers_api import fyersModel

# 1. Data
#   1. Time frame
#    2. Candle
#       1. Start
#        2. End
#         3. High
#         4. Low
#     3. Entry
#       1. Check BO at every 15min
#            1. high
#             2. low
#     4. Exit
#       1. As soon as traget hits

{
    "companyName": "STATE BANK OF INDIA",
    "currentValue": "517.90",
    "change": "1.80",
    "pChange": "0.35",
    "updatedOn": "11 Apr 22 | 12:48 PM",
    "priceBand": "",
    "securityID": "SBIN",
    "scripCode": "500112",
    "group": "A  / S&P BSE SENSEX",
    "faceValue": "1.00",
    "industry": "Financial Services",
    "previousClose": "516.10",
    "previousOpen": "514.00",
    "dayHigh": "522.00",
    "dayLow": "513.05",
    "52weekHigh": "549.05",
    "52weekLow": "321.15",
    "weightedAvgPrice": "519.09",
    "totalTradedValue": "22.19 Cr.",
    "totalTradedQuantity": "4.28 Lakh",
    "2WeekAvgQuantity": "6.76 Lakh",
    "marketCapFull": "4,62,205.63 Cr.",
    "marketCapFreeFloat": "1,98,748.42 Cr.",
    "upperPriceBand": "",
    "lowerPriceBand": "",
    "buy": {
        "1": {
            "quantity": "170",
            "price": "517.70"
        },
        "2": {
            "quantity": "4",
            "price": "517.65"
        },
        "3": {
            "quantity": "169",
            "price": "517.60"
        },
        "4": {
            "quantity": "465",
            "price": "517.55"
        },
        "5": {
            "quantity": "671",
            "price": "517.50"
        }
    },
    "sell": {
        "1": {
            "price": "517.95",
            "quantity": "1"
        },
        "2": {
            "price": "518.00",
            "quantity": "238"
        },
        "3": {
            "price": "518.05",
            "quantity": "134"
        },
        "4": {
            "price": "518.10",
            "quantity": "80"
        },
        "5": {
            "price": "518.15",
            "quantity": "196"
        }
    }
}


class Udun(object):
    def __init__(self, access_token, log_path="logs"):
        self.client_id = "LSCTXIM2YP-100"
        self.udun = fyersModel.FyersModel(
            token=access_token,
            is_async=False, client_id=self.client_id, log_path=log_path)

    def get_profile(self):
        return self.udun.get_profile()

    def get_funds(self):
        return self.udun.funds()

    def get_holdings(self):
        return self.udun.holdings()

    def get_positions(self):
        return self.udun.positions()

    def get_cancel_basket(self, scrips):
        if not scrips:
            return False, "Nothing to cancel"
        data = [{"id": item} for item in scrips]
        return True, self.udun.cancel_basket_orders(data)

    def get_exit_positions(self, scrips):
        if not scrips:
            return False, "Nothing to exit"
        data = [{"id": item} for item in scrips]
        return self.udun.exit_position(data)

    def place_order(self, symbol, side, limit_price, sl, quantity, take_profit=2):
        # def place_order(self):

        # product_type = ["CNC", "INTRADAY", "MARGIN", "CO", "BO"]
        # order_type = [{"LIMIT ORDER": 1, "MARKET ORDER": 2, "STOP ORDER": 3, "STOP LIMIT ORDER": 4}]
        # order = {
        #     "symbol": "NSE:AXISBANK-EQ",
        #     "qty": 1,
        #     "type": 1,
        #     "side": -1,
        #     "productType": "BO",
        #     "limitPrice": 805,
        #     "stopPrice": -1,
        #     "validity": "DAY",
        #     "disclosedQty": 0,
        #     "offlineOrder": "False",
        #     "stopLoss": 2,
        #     "takeProfit": 2
        # }
        order = {
            "symbol": symbol,
            "qty": quantity,
            "type": 1,
            "side": side,
            "productType": "BO",
            "limitPrice": limit_price,
            "stopPrice": 0,
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": "False",
            "stopLoss": sl,
            "takeProfit": take_profit
        }
        print(order)
        return self.udun.place_order(order)

    def get_quote(self):
        data = {"symbols": "NSE:AXISBANK-EQ"}
        return self.udun.quotes(data)

    def get_history(self, data):
        return self.udun.history(data)


def main():
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDQ5ODMyMTcsImV4cCI6MTY0NTA1Nzg1NywibmJmIjoxNjQ0OTgzMjE3LCJhdWQiOlsieDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaURIT3hjczRVZFNHQmJ6Wkh6M0dheE1tcDIycTJpcVlMQnlnd2tZaGZKLU9aVVN2dHY4WGdzZUczMjZybGdLOUlQaVByYW85U18wMEJsRGJZejBiR2FBNEpKVnhDSnpETF9tX3E1R3FzbW92WVh1MD0iLCJkaXNwbGF5X25hbWUiOiJBS0FOS1NIQSBBTklSVURIQSBWQVJNQSIsImZ5X2lkIjoiWEEwMDI5OCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.-AkUDPly90_CsuDlkfzI6guQ0hQNuVA3sa42oSaxWEs"
    udun = Udun(access_token)
    print(udun.place_order())


if __name__ == '__main__':
    main()


# # After this point you can call the relevant apis and get started with

# ####################################################################################################################
# """
# 1. User Apis : This includes (Profile,Funds,Holdings)
# """

# print(fyers.get_profile())  # This will provide us with the user related data

# print(fyers.funds())  # This will provide us with the funds the user has

# print(fyers.holdings())  # This will provide the available holdings the user has


# ########################################################################################################################

# """
# 2. Transaction Apis : This includes (Tradebook,Orderbook,Positions)
# """

# print(fyers.tradebook())  # This will provide all the trade related information

# print(fyers.orderbook())  # This will provide the user with all the order realted information

# print(fyers.positions())  # This will provide the user with all the positions the user has on his end


# ######################################################################################################################

# """
# 3. Order Placement  : This Apis helps to place order.
# There are two ways to place order
# a. single order : wherein you can fire one order at a time
# b. multi order : this is used to place a basket of order but the basket size can max be 10 symbols
# """

# # SINGLE ORDER

# data = {
#     "symbol": "NSE:ONGC-EQ",
#     "qty": 1,
#     "type": 1,
#     "side": 1,
#     "productType": "INTRADAY",
#     "limitPrice": 0,
#     "stopPrice": 0,
#     "validity": "DAY",
#     "disclosedQty": 0,
#     "offlineOrder": "False",
#     "stopLoss": 0,
#     "takeProfit": 0
# }  # This is a sample example to place a limit order you can make the further changes based on your requriements

# print(fyers.place_order(data))

# # MULTI ORDER

# data = [{"symbol": "NSE:SBIN-EQ",
#          "qty": 1,
#          "type": 1,
#          "side": 1,
#          "productType": "INTRADAY",
#          "limitPrice": 61050,
#          "stopPrice": 0,
#          "disclosedQty": 0,
#          "validity": "DAY",
#          "offlineOrder": "False",
#          "stopLoss": 0,
#          "takeProfit": 0
#          },
#         {
#     "symbol": "NSE:HDFC-EQ",
#     "qty": 1,
#     "type": 2,
#     "side": 1,
#     "productType": "INTRADAY",
#     "limitPrice": 0,
#     "stopPrice": 0,
#     "disclosedQty": 0,
#     "validity": "DAY",
#     "offlineOrder": "False",
#     "stopLoss": 0,
#     "takeProfit": 0
# }]  # This takes input as a list containing multiple single order data into it and the execution of the orders goes in the same format as mentioned.

# print(fyers.place_basket_orders(data))


# ###################################################################################################################

# """
# 4. Other Transaction : This includes (modify_order,exit_position,cancel_order,convert_positions)
# """

# # Modify_order request
# data = {
#     "id": 7574657627567,
#     "type": 1,
#     "limitPrice": 61049,
#     "qty": 1
# }

# print(fyers.modify_order(data))

# # Modify Multi Order

# data = [
#     {"id": 8102710298291,
#      "type": 1,
#      "limitPrice": 61049,
#      "qty": 0
#      },
#     {
#         "id": 8102710298292,
#         "type": 1,
#         "limitPrice": 61049,
#         "qty": 1
#     }]

# print(fyers.modify_basket_orders(data))


# # Cancel_order
# data = {"id": '808058117761'}
# print(fyers.cancel_order(data))

# # cancel_multi_order
# data = [
#     {
#         "id": '808058117761'
#     },
#     {
#         "id": '808058117762'
#     }]

# print(fyers.cancel_basket_orders(data))


# # Exit Position
# data = {
#     "id": "NSE:SBIN-EQ-INTRADAY"
# }
# print(fyers.cancel_basket_orders(data))
# print(fyers.exit_positions(data))


# # Convert Position

# data = {
#     "symbol": "MCX:SILVERMIC20NOVFUT",
#     "positionSide": 1,
#     "convertQty": 1,
#     "convertFrom": "INTRADAY",
#     "convertTo": "CNC"
# }

# print(fyers.convert_position(data))


# #################################################################################################################

# """
# DATA APIS : This includes following Apis(History,Quotes,MarketDepth)
# """

# # Historical Data

# data = {"symbol": "NSE:SBIN-EQ", "resolution": "D", "date_format": "0",
#         "range_from": "1622097600", "range_to": "1622097685", "cont_flag": "1"}

# print(fyers.history(data))

# # Quotes

# data = {"symbols": "NSE:SBIN-EQ"}
# print(fyers.quotes(data))


# # Market Depth

# data = {"symbol": "NSE:SBIN-EQ", "ohlcv_flag": "1"}
# print(fyers.depth(data))
