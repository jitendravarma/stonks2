ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NTYwNDM4MTcsImV4cCI6MTY1NjExNzAxNywibmJmIjoxNjU2MDQzODE3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaXRUa3BBNVRUSmFQVGkySHRkQmxITTZkS0RjMC16V1BBSVhKVjVyVjJpZTYwcXZ4cjNiOTI2ZFNISUJlRFRBSFBEbkFlekxWa1VDcTVYbkxNNThvcUt4ZE9wYnFiNDZOZkp2Rl85SC1seVZKYVEtQT0iLCJkaXNwbGF5X25hbWUiOiJBS0FOS1NIQSBBTklSVURIQSBWQVJNQSIsImZ5X2lkIjoiWEEwMDI5OCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.FkYt8u7JVKZ5nx9i2l6AkBtmzhL_xtMIHoqkCVd6Vg4"


VSCRIPS = [{
    'name': 'SUNPHARMA', 'atr': 3.68, 'price': 825.0},
    {'name': 'POWERGRID', 'atr': 1.01, 'price': 208.15},
    {'name': 'ITC', 'atr': 1.02, 'price': 266.4},
    {'name': 'KOTAKBANK', 'atr': 6.9, 'price': 1688.9},
    {'name': 'BHARTIARTL', 'atr': 3.2, 'price': 660.8},
    {'name': 'HCLTECH', 'atr': 4.36, 'price': 974.45},
    {'name': 'TITAN', 'atr': 11.85, 'price': 2040.0},
    {'name': 'ICICIBANK', 'atr': 3.03, 'price': 699.95},
    {'name': 'ONGC', 'atr': 0.92, 'price': 135.4},
    {'name': 'CHOLAFIN', 'atr': 4.62, 'price': 637.0},
    {'name': 'BANDHANBNK', 'atr': 2.32, 'price': 278.2},
    {'name': 'AXISBANK', 'atr': 2.93, 'price': 630.5},
    {'name': 'GRASIM', 'atr': 7.0, 'price': 1317.9},
    {'name': 'TECHM', 'atr': 5.64, 'price': 991.95},
    {'name': 'HINDALCO', 'atr': 2.52, 'price': 318.0},
    {'name': 'UPL', 'atr': 3.75, 'price': 633.05},
    {'name': 'INDUSINDBK', 'atr': 5.22, 'price': 787.0},
    {'name': 'LUPIN', 'atr': 3.14, 'price': 627.85},
    {'name': 'TATAMOTORS', 'atr': 2.49, 'price': 407.15},
    {'name': 'JINDALSTEL', 'atr': 2.68, 'price': 309.8},
    {'name': 'BIOCON', 'atr': 1.88, 'price': 326.5},
    {'name': 'BPCL', 'atr': 1.78, 'price': 307.5},
    {'name': 'CIPLA', 'atr': 4.49, 'price': 933.55},
    {'name': 'TATASTEEL', 'atr': 5.99, 'price': 840.8},
    {'name': 'HDFC', 'atr': 9.41, 'price': 2169.25},
    {'name': 'BANKBARODA', 'atr': 0.65, 'price': 96.25},
    {'name': 'COALINDIA', 'atr': 1.04, 'price': 177.2},
    {'name': 'SBIN', 'atr': 2.07, 'price': 451.25},
    {'name': 'ADANIPORTS', 'atr': 4.37, 'price': 676.0},
    {'name': 'MARICO', 'atr': 2.38, 'price': 477.0},
    {'name': 'M&M', 'atr': 4.73, 'price': 1028.0},
    {'name': 'WIPRO', 'atr': 2.13, 'price': 420.8},
    {'name': 'HDFCBANK', 'atr': 4.95, 'price': 1336.6},
    {'name': 'INFY', 'atr': 6.18, 'price': 1456.95},
    {'name': 'LT', 'atr': 6.91, 'price': 1496.05},
    {'name': 'SBILIFE', 'atr': 5.13, 'price': 1072.1},
    {'name': 'RELIANCE', 'atr': 12.68, 'price': 2469.0},
    {'name': 'HINDUNILVR', 'atr': 9.01, 'price': 2250.0}]


def format_data(data):
    return {
        "TF": data['time_frame'],
        "Time": data['time_range'],
        "Name": data['scrip_name'],
        'SlBuffer': data['stop_loss_buffer'],
        "WinPoints": data['total_target_count'],
        "SlPoints": data['total_sl_count'],
        "PointsAfterSL": round(data['total_points_captured'], 2),
        'AppxPrice': data['entry_price'],
        "AvgPntPerTrade": data["avg_per_trade"],
        "Target %": data["Target %"],
        "Target in Rs": data['target'],
        "Days": data["total_days"],
        "WinDays": data["successful_days"],
        "SLHitDays": data['sl_hit_days'],
        "SLAboveATR": len(data['sl_with_atr']),
        "ATR": data['atr'],
        "RBD": data['range_bound_days'],
        'Win%': data['win_%'],
        "AvgEntry": data["avg_entry_time"],
        "AvgExit": data["avg_exit_time"],
        "AvgTime": data["avg_time_in_trade"],
        "Quantity": data['quantity'],
        "FinalAmt":  round(data['quantity']*data['total_points_captured'], 2)
    }


1023.00 - 1643.85 + 156.00 + 34.00
