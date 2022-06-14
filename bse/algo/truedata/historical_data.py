# Historical Data - Using TrueData Websocket Python Library

from truedata_ws.websocket.TD import TD


username = 'FYERS1637'
password = 'SGJG4Roj'

history_port = 8092
# live_port to be set to None in case subscribed only for Historical data
# Default ports are live_port=8082 & Historical_port=8092

history_client = TD(username, password, live_port=None)

# symbol = 'SBIN'
# barsize = '15min'
# barsize = 'EOD'

# Gets current day 1 min data - Note if market not started / holiday, you will get a No Data ! return
# hist_data_3 = history_client.get_historic_data(symbol)

# Gets current day data with the bar size of your choice - Note if market not started / holiday, you will get a No Data ! return
# hist_data_3 = history_client.get_historic_data(symbol, bar_size=barsize)

# Specify Bar size and duration in No. of Days


def get_historical_data(symbol, duration="1 D", bar_size="15min"):
    return history_client.get_historic_data(
        symbol, duration=duration, bar_size=bar_size)

# Get Data for specified bar size for any start & end date-time. Default end time = now
# hist_data_3 = history_client.get_historic_data("SBIN", start_time=datetime.datetime(2020, 9, 17, 15, 28, 0),bar_size="10min", end_time=datetime.datetime(2020, 9, 19, 23, 59, 0))

# Get last n bars data for specific bar size. Works best with & recommended for 1/5 min bars.
# hist_data_3=history_client.get_n_historical_bars(symbol, no_of_bars=30, bar_size=barsize)


# df_hist_data = pd.DataFrame(hist_data_3)

# print('\nSymbol > %s' % symbol)
# print('Bar Interval > %s\n' % barsize)

# print(df_hist_data)

# history_client.disconnect()
