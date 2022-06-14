from apscheduler.schedulers.blocking import BlockingScheduler

from sauron import Sauron

stocks = [
    {
        'scrip': '532215', 'fyers_code': "NSE:AXISBANK-EQ", 'quantity': 10,
        'take_profit': 5, "stop_loss": 1, 'take_profit_sell': 3.2
    }]

CLOCK_MIN = {
    5: [0, 15, 30, 45],
    10: [5, 15, 25, 35, 45, 55],
    15: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
}


def analyze_scrip():
    for item in stocks:
        # scrip_code, client_code, time_frame, hour, start_candle_min,
        #          end_candle_min, take_profit, take_profit_sell, quantity=10, stop_loss=1,
        stonk = Sauron(scrip_code=item['scrip'], client_code=item['fyers_code'],
                       time_frame=10, hour=10, start_candle_min=5,
                       end_candle_min=15, take_profit=item["take_profit"],
                       take_profit_sell=item["take_profit_sell"],
                       quantity=item["quantity"], stop_loss=item["stop_loss"])
        stonk.analyze_scrip()


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(analyze_scrip, 'interval', minutes=1)
    scheduler.start()
