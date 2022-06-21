ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NTU3ODM3NTAsImV4cCI6MTY1NTg1Nzg1MCwibmJmIjoxNjU1NzgzNzUwLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaXNVRkc3dzVGV2NDMXJ5ZVRMTncxNnl1c1dySS1Ga2dhc3N5VkFZeW1pS1V5UmhGUkxJdjRpYk9xaHpqcnVOS0pjdnBZQXEyX3Rkam5nOElMSDlVdzVEWmIyeTRFMDZfaWl1TXdiYzdBQ2hxdGVuQT0iLCJkaXNwbGF5X25hbWUiOiJBS0FOS1NIQSBBTklSVURIQSBWQVJNQSIsImZ5X2lkIjoiWEEwMDI5OCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.TKU1jtXcPKIAjDBYf-ImEB1GAbpb-sY6XyLZRKuxCtY"


VSCRIPS = [
    {'name': 'SUNPHARMA', 'atr': 4.29, 'price': 726.35},
    {'name': 'POWERGRID', 'atr': 4.29, 'price': 726.35},
    {'name': 'ITC', 'atr': 4.29, 'price': 726.35},
    {'name': 'KOTAKBANK', 'atr': 4.29, 'price': 726.35},
    {'name': 'BHARTIARTL', 'atr': 4.29, 'price': 726.35},
    {'name': 'HCLTECH', 'atr': 4.29, 'price': 726.35},
    {'name': 'TITAN', 'atr': 10.26, 'price': 2507.0},
    {'name': 'ICICIBANK', 'atr': 3.14, 'price': 747.5},
    {'name': 'ONGC', 'atr': 0.65, 'price': 164.7},
    {'name': 'CHOLAFIN', 'atr': 4.48, 'price': 743.1},
    {'name': 'BANDHANBNK', 'atr': 2.17, 'price': 336.0},
    {'name': 'AXISBANK', 'atr': 3.79, 'price': 777.55},
    {'name': 'GRASIM', 'atr': 8.18, 'price': 1713.3},
    {'name': 'SAIL', 'atr': 0.55, 'price': 97.95},
    {'name': 'TECHM', 'atr': 5.93, 'price': 1271.55},
    {'name': 'HINDALCO', 'atr': 3.01, 'price': 489.0},
    {'name': 'UPL', 'atr': 3.74, 'price': 826.05},
    {'name': 'INDUSINDBK', 'atr': 4.66, 'price': 988.0},
    {'name': 'GAIL', 'atr': 0.84, 'price': 158.05},
    {'name': 'LUPIN', 'atr': 3.52, 'price': 746.0},
    {'name': 'TATAMOTORS', 'atr': 2.06, 'price': 435.5},
    {'name': 'IOC', 'atr': 0.6, 'price': 129.9},
    {'name': 'JINDALSTEL', 'atr': 3.5, 'price': 547.0},
    {'name': 'BIOCON', 'atr': 2.27, 'price': 375.45},
    {'name': 'BPCL', 'atr': 1.66, 'price': 367.75},
    {'name': 'INDIGO', 'atr': 10.09, 'price': 1860.0},
    {'name': 'CIPLA', 'atr': 4.4, 'price': 980.1},
    {'name': 'TATASTEEL', 'atr': 6.91, 'price': 1258.7},
    {'name': 'HDFC', 'atr': 10.66, 'price': 2222.0},
    {'name': 'BANKBARODA', 'atr': 0.66, 'price': 115.95},
    {'name': 'COALINDIA', 'atr': 1.26, 'price': 192.2},
    {'name': 'SBIN', 'atr': 2.0, 'price': 507.7},
    {'name': 'ADANIPORTS', 'atr': 5.44, 'price': 890.75},
    {'name': 'MARICO', 'atr': 2.39, 'price': 537.4},
    {'name': 'DLF', 'atr': 2.15, 'price': 379.0},
    {'name': 'M&M', 'atr': 4.19, 'price': 922.0},
    {'name': 'WIPRO', 'atr': 2.02, 'price': 522.5}
]


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
