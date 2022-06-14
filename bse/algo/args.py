from argparse import ArgumentParser

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

parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

args = parser.parse_args()

print(args)
