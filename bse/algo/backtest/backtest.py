
import time
import sys
import traceback
from datetime import datetime, timedelta

import pandas as pd

from constants import ACCESS_TOKEN

sys.path.append('../')


# sbin

# sample format
# ongc
# data = {'s': 'ok', 'candles': [[1648784700, 163.9, 166.5, 163.55, 164.0, 5347208], [1648785600, 164.0, 164.95, 163.9, 164.6, 1790112], [1648786500, 164.6, 164.85, 164.2, 164.6, 1019931], [1648787400, 164.6, 164.6, 164.15, 164.3, 1203309], [1648788300, 164.3, 164.95, 164.25, 164.8, 690282], [1648789200, 164.75, 164.8, 164.4, 164.5, 554011], [1648790100, 164.45, 165.35, 164.25, 165.15, 1291477], [1648791000, 165.1, 165.2, 164.85, 165.05, 474940], [1648791900, 165.05, 165.9, 165.05, 165.8, 911635], [1648792800, 165.85, 166.0, 165.2, 165.25, 790500], [1648793700, 165.3, 165.65, 165.2, 165.6, 325790], [1648794600, 165.6, 165.9, 165.3, 165.85, 513699], [1648795500, 165.85, 166.15, 165.45, 165.9, 792240], [1648796400, 165.9, 165.9, 164.7, 164.7, 723279], [1648797300, 164.65, 165.1, 164.5, 164.85, 660367], [1648798200, 164.9, 165.9, 164.9, 165.45, 602136], [1648799100, 165.45, 165.9, 165.45, 165.85, 374463], [1648800000, 165.85, 166.0, 165.5, 166.0, 591365], [1648800900, 166.0, 166.3, 165.45, 166.25, 1162980], [1648801800, 166.25, 167.0, 166.25, 166.8, 1282748], [1648802700, 166.8, 167.2, 166.6, 167.0, 928979], [1648803600, 167.0, 167.5, 166.75, 166.8, 825179], [1648804500, 166.85, 167.35, 166.8, 167.05, 715805], [1648805400, 167.0, 168.2, 167.0, 168.2, 2030178], [1648806300, 168.1, 168.25, 167.7, 167.95, 2401144], [1649043900, 166.95, 167.2, 165.65, 166.75, 1960797], [1649044800, 166.8, 166.85, 166.05, 166.25, 908683], [1649045700, 166.25, 166.3, 165.6, 165.85, 1117426], [1649046600, 165.85, 166.1, 165.35, 165.45, 883396], [1649047500, 165.4, 166.15, 165.35, 166.15, 571324], [1649048400, 166.05, 166.8, 165.8, 166.6, 708415], [1649049300, 166.65, 166.7, 166.45, 166.7, 431301], [1649050200, 166.7, 167.75, 166.7, 167.4, 917213], [1649051100, 167.35, 167.6, 167.3, 167.35, 487765], [1649052000, 167.4, 168.1, 167.35, 167.95, 786211], [1649052900, 167.95, 168.6, 167.9, 168.45, 731888], [1649053800, 168.5, 169.05, 168.25, 168.25, 898129], [1649054700, 168.3, 168.55, 167.9, 168.4, 675002], [1649055600, 168.5, 168.85, 168.4, 168.55, 344621], [1649056500, 168.55, 168.85, 168.4, 168.65, 377976], [1649057400, 168.7, 168.9, 168.45, 168.6, 305386], [1649058300, 168.7, 168.75, 168.15, 168.45, 542119], [1649059200, 168.5, 168.7, 168.35, 168.5, 376739], [1649060100, 168.5, 168.55, 168.4, 168.5, 366437], [1649061000, 168.5, 168.6, 168.35, 168.4, 337637], [1649061900, 168.45, 168.85, 168.35, 168.75, 298486], [1649062800, 168.75, 168.75, 168.25, 168.3, 653170], [1649063700, 168.35, 168.35, 167.8, 168.05, 596495], [1649064600, 168.2, 168.3, 167.8, 167.85, 816901], [1649065500, 167.85, 168.55, 167.65, 168.0, 1499289], [1649130300, 170.25, 171.2, 169.85, 170.5, 3423423], [1649131200, 170.55, 170.75, 169.3, 169.4, 1298362], [1649132100, 169.35, 170.5, 169.35, 170.5, 965865], [1649133000, 170.5, 171.0, 169.8, 170.85, 847220], [1649133900, 170.9, 171.1, 170.4, 170.55, 648774], [1649134800, 170.4, 170.6, 169.9, 170.25, 545561], [1649135700, 170.35, 170.7, 170.2, 170.7, 399681], [1649136600, 170.7, 170.9, 170.4, 170.8, 349528], [1649137500, 170.8, 170.8, 170.6, 170.7, 212224], [1649138400, 170.7, 171.0, 170.5, 170.95, 486377], [1649139300, 171.0, 171.15, 170.7, 170.9, 440993], [1649140200, 170.9, 171.15, 170.8, 171.1, 365137], [1649141100, 171.05, 171.6, 171.05, 171.55, 690131], [1649142000, 171.55, 172.0, 171.45, 171.75, 818847], [1649142900, 171.75, 172.0, 171.4, 171.55, 802607], [1649143800, 171.6, 172.6, 171.55, 172.5, 1008081], [1649144700, 172.55, 172.75, 172.35, 172.5, 836821], [1649145600, 172.5, 172.55, 171.8, 172.15, 598340], [1649146500, 172.15, 172.5, 171.95, 172.0, 566261], [1649147400, 171.8, 172.2, 171.35, 171.95, 636257], [1649148300, 171.9, 171.95, 171.55, 171.75, 376118], [1649149200, 171.75, 172.3, 171.7, 172.3, 663222], [1649150100, 172.25, 172.5, 172.05, 172.3, 875826], [1649151000, 172.25, 172.4, 171.8, 171.8, 878103], [1649151900, 171.8, 171.9, 171.25, 171.35, 1213367], [1649216700, 170.6, 172.3, 170.3, 172.2, 1557653], [1649217600, 172.2, 173.4, 172.0, 173.05, 1301696], [1649218500, 173.05, 173.3, 172.65, 172.85, 645240], [1649219400, 172.85, 172.95, 172.35, 172.65, 452740], [1649220300, 172.6, 172.65, 171.9, 172.45, 473349], [1649221200, 172.45, 173.15, 172.45, 173.15, 858957], [1649222100, 173.05, 173.2, 172.9, 173.15, 310140], [1649223000, 173.1, 173.5, 172.9, 172.95, 512032], [1649223900, 173.0, 173.05, 172.75, 172.85, 293435], [1649224800, 172.85, 173.1, 172.55, 172.55, 362428], [1649225700, 172.5, 172.5, 172.05, 172.3, 526781], [1649226600, 172.3, 172.8, 172.25, 172.75, 265258], [1649227500, 172.7, 173.0, 172.6, 172.95, 254034], [1649228400, 173.0, 173.05, 172.9, 173.0, 227249], [1649229300, 173.0, 173.25, 172.9, 173.0, 276596], [1649230200, 173.0, 173.0, 172.55, 172.95, 291286], [1649231100, 172.95, 173.0, 172.65, 172.65, 247376], [1649232000, 172.55, 173.2, 172.55, 173.15, 321375], [1649232900, 173.2, 173.35, 172.95, 173.05, 342934], [1649233800, 173.05, 173.35, 173.0, 173.25, 319423], [1649234700, 173.25, 173.5, 173.1, 173.2, 477805], [1649235600, 173.3, 173.35, 173.0, 173.05, 337892], [1649236500, 173.05, 173.1, 172.6, 172.75, 447721], [1649237400, 172.7, 173.05, 172.65, 173.05, 576089], [1649238300, 173.05, 173.2, 172.55, 172.75, 1234300], [1649303100, 170.6, 172.7, 169.3, 171.85, 4028589], [1649304000, 171.9, 172.6, 171.7, 171.9, 1109361], [1649304900, 171.9, 172.5, 171.8, 172.45, 1131800], [1649305800, 172.5, 173.8, 172.45, 172.9, 2217193], [1649306700, 172.9, 173.0, 171.85, 171.85, 942235], [1649307600, 171.8, 171.95, 170.9, 171.7, 1069780], [1649308500, 171.75, 171.95, 171.6, 171.9, 416123], [1649309400, 171.95, 172.1, 171.8, 172.0, 383693], [1649310300, 172.0, 172.3, 171.75, 171.75, 522923], [1649311200, 171.85, 172.1, 171.7, 172.1, 309886], [1649312100, 172.1, 172.25, 172.0, 172.1, 312390], [1649313000, 172.15, 172.2, 171.7, 171.85, 392462], [
# 1649313900, 171.9, 172.0, 171.8, 172.0, 427702], [1649314800, 172.0, 172.25, 171.95, 172.25, 455773], [1649315700, 172.25, 172.3, 172.05, 172.05, 277266], [1649316600, 172.05, 172.15, 171.2, 171.3, 391849], [1649317500, 171.25, 171.3, 170.45, 170.45, 461136], [1649318400, 170.35, 170.45, 169.5, 169.65, 1046686], [1649319300, 169.65, 169.7, 168.7, 169.45, 1107847], [1649320200, 169.45, 170.0, 168.55, 168.85, 1017217], [1649321100, 168.85, 169.5, 168.7, 169.4, 761101], [1649322000, 169.4, 169.4, 169.05, 169.1, 666154], [1649322900, 168.95, 169.35, 168.9, 169.1, 691106], [1649323800, 169.15, 169.35, 168.75, 168.9, 1697470], [1649324700, 168.95, 168.95, 168.2, 168.9, 2597241], [1649389500, 169.0, 170.65, 168.95, 169.25, 1178357], [1649390400, 169.25, 169.55, 168.9, 169.15, 521237], [1649391300, 169.15, 169.45, 168.7, 169.3, 354470], [1649392200, 169.25, 169.65, 169.0, 169.05, 502819], [1649393100, 169.1, 169.65, 168.85, 169.65, 568140], [1649394000, 169.55, 170.0, 169.5, 169.85, 396797], [1649394900, 169.85, 169.95, 169.5, 169.8, 183344], [1649395800, 169.85, 169.9, 169.6, 169.7, 190232], [1649396700, 169.75, 170.2, 169.65, 170.15, 266267], [1649397600, 170.15, 170.4, 170.0, 170.15, 341443], [1649398500, 170.15, 170.4, 170.0, 170.35, 238894], [1649399400, 170.35, 170.55, 170.25, 170.55, 228807], [1649400300, 170.5, 170.85, 170.5, 170.75, 277305], [1649401200, 170.75, 170.9, 169.9, 169.95, 536416], [1649402100, 170.0, 170.0, 169.45, 169.6, 251606], [1649403000, 169.6, 170.05, 169.55, 169.95, 140042], [1649403900, 169.9, 170.35, 169.75, 170.35, 114893], [1649404800, 170.4, 170.65, 170.3, 170.55, 198658], [1649405700, 170.6, 170.85, 170.4, 170.55, 218960], [1649406600, 170.6, 170.8, 170.55, 170.75, 204251], [1649407500, 170.7, 170.95, 170.65, 170.85, 267978], [1649408400, 170.9, 170.9, 170.6, 170.65, 200660], [1649409300, 170.65, 171.3, 170.65, 170.85, 503870], [1649410200, 170.85, 171.15, 170.6, 170.75, 337859], [1649411100, 170.8, 171.2, 170.65, 170.65, 1241723], [1649648700, 171.0, 172.75, 169.55, 171.4, 1598510], [1649649600, 171.25, 171.6, 170.8, 170.8, 721218], [1649650500, 170.8, 171.05, 170.55, 170.75, 537917], [1649651400, 170.85, 171.15, 170.35, 170.55, 493496], [1649652300, 170.45, 171.5, 170.45, 171.5, 333171], [1649653200, 171.4, 171.7, 171.05, 171.2, 348775], [1649654100, 171.2, 171.6, 171.1, 171.3, 207446], [1649655000, 171.3, 171.4, 171.15, 171.3, 192234], [1649655900, 171.3, 171.35, 171.0, 171.1, 217842], [1649656800, 171.1, 171.1, 170.85, 171.05, 208561], [1649657700, 171.1, 171.15, 170.55, 170.8, 276069], [1649658600, 170.8, 170.85, 170.65, 170.85, 176169], [1649659500, 170.85, 171.2, 170.75, 171.0, 235522], [1649660400, 171.0, 171.15, 170.75, 170.95, 334073], [1649661300, 171.0, 171.15, 170.85, 171.0, 201097], [1649662200, 171.0, 171.05, 170.8, 170.9, 187166], [1649663100, 170.95, 171.4, 170.9, 171.15, 360766], [1649664000, 171.15, 171.4, 171.05, 171.2, 292441], [1649664900, 171.25, 171.25, 171.0, 171.15, 268784], [1649665800, 171.15, 171.2, 170.95, 171.1, 244419], [1649666700, 171.15, 171.35, 171.0, 171.25, 264156], [1649667600, 171.25, 171.5, 170.95, 170.95, 357908], [1649668500, 170.9, 171.4, 170.8, 171.1, 248217], [1649669400, 171.15, 171.5, 170.9, 171.45, 594996], [1649670300, 171.45, 171.55, 170.9, 170.9, 761485], [1649735100, 171.0, 172.2, 170.85, 171.15, 1686192], [1649736000, 171.15, 171.15, 169.2, 169.5, 1358601], [1649736900, 169.45, 169.95, 168.85, 169.6, 803822], [1649737800, 169.6, 169.95, 169.4, 169.65, 346662], [1649738700, 169.55, 169.75, 169.35, 169.55, 483466], [1649739600, 169.5, 169.65, 169.0, 169.6, 590072], [1649740500, 169.6, 169.7, 169.4, 169.5, 201296], [1649741400, 169.55, 169.95, 169.5, 169.8, 213213], [1649742300, 169.8, 170.25, 169.65, 170.0, 311918], [1649743200, 169.95, 170.1, 169.3, 169.3, 310086], [1649744100, 169.35, 169.7, 169.35, 169.5, 168056], [1649745000, 169.45, 169.7, 169.3, 169.65, 217381], [1649745900, 169.65, 170.15, 169.6, 169.9, 363710], [1649746800, 169.95, 170.3, 169.85, 170.05, 219660], [1649747700, 170.15, 170.15, 169.7, 169.9, 216337], [1649748600, 169.9, 169.9, 169.3, 169.45, 294376], [1649749500, 169.5, 169.5, 168.75, 168.95, 390700], [1649750400, 168.9, 169.15, 168.5, 169.0, 457228], [1649751300, 169.0, 169.4, 168.8, 169.4, 260827], [1649752200, 169.4, 169.55, 169.35, 169.35, 247457], [1649753100, 169.35, 169.65, 169.15, 169.55, 326801], [1649754000, 169.55, 170.0, 169.5, 169.8, 160524], [1649754900, 169.8, 170.2, 169.5, 170.1, 281578], [1649755800, 170.15, 170.15, 169.05, 169.15, 1286850], [1649756700, 169.05, 169.05, 168.2, 168.75, 1926428], [1649821500, 171.4, 173.5, 170.7, 173.1, 3303799], [1649822400, 173.0, 173.35, 172.7, 172.95, 1307036], [1649823300, 173.15, 174.4, 173.1, 173.95, 2594405], [1649824200, 173.95, 174.2, 173.55, 173.9, 1216288], [1649825100, 173.9, 174.05, 173.5, 173.75, 918736], [1649826000, 173.75, 174.5, 173.6, 174.05, 972284], [1649826900, 174.05, 174.05, 173.7, 173.8, 614432], [1649827800, 173.75, 174.3, 173.7, 174.0, 620375], [1649828700, 174.0, 174.1, 173.85, 173.9, 361149], [1649829600, 173.95, 174.05, 173.65, 173.65, 485905], [1649830500, 173.75, 173.75, 173.05, 173.05, 964104], [1649831400, 172.85, 173.55, 172.85, 173.1, 569521], [1649832300, 173.05, 173.6, 173.05, 173.55, 363691], [1649833200, 173.5, 174.2, 173.4, 173.6, 604278], [1649834100, 173.6, 173.65, 173.25, 173.65, 364874], [1649835000, 173.6, 174.1, 173.6, 173.85, 531520], [1649835900, 173.9, 174.0, 173.65, 173.9, 382005], [1649836800, 173.9, 174.35, 173.85, 174.25, 588705], [1649837700, 174.35, 174.35, 173.85, 174.2, 451888], [1649838600, 174.2, 174.4, 174.1, 174.35, 416658], [1649839500, 174.4, 174.4, 173.85, 174.25, 536435], [1649840400, 174.2, 174.85, 174.2, 174.55, 1365073], [1649841300, 174.55, 174.65, 174.25, 174.4, 659060], [1649842200, 174.4, 174.5, 174.0, 174.4, 1063238], [1649843100, 174.4, 174.55, 173.75, 174.0, 2043055]]}

# history = {"symbol": "NSE:ONGC-EQ", "resolution": "15", "date_format": "1",
#            "range_from": "2022-04-01", "range_to": "2022-04-14", "cont_flag": "1"}


# AVERAGE_VOLUME = df['Volume'].mean()
# print(AVERAGE_VOLUME)
# get list of all working days


class Diva(object):

    def __init__(self, SCRIP_NAME="", DAY_RANGE=30, TIME_FRAME=5, START_DELTA=0, SLEEP=0.3) -> None:
        self.SCORE = []
        self.STOP_LOSS = []
        self.TARGET = []
        self.SCRIP_NAME = SCRIP_NAME
        self.BO_CANDLE_HR = ""
        self.BO_CANDLE_MIN = ""
        self.TIME_FRAME = TIME_FRAME
        self.EXECUTED_DAYS = []
        self.DAY_RANGE = DAY_RANGE
        self.START_DELTA = START_DELTA
        self.STOP_LOSS_BUFFER = ""
        self.FIRST_TARGET_SIZE = ""
        self.SECOND_TARGET_SIZE = ""
        self.STOP_LOSS_PERCENTAGE = 0.1
        self.SLEEP = SLEEP
        self.entry_price = ""
        self.TARGET_IN_PERCENTAGE = None
        self.FUND = 100000
        self.ALL_ENTRY_TIME = []
        self.ALL_EXIT_TIME = []
        self.GET_DAILY_DATA = False
        self.DAILY_DATA = {}
        self.QUANTITY = 1
        self.ATR = None
        self.SL_WITH_ATR = []
        self.VALUES = []
        self.df = self.get_data()
        self.WORKING_DAYS = self.get_working_days(self.df)

    def get_date_string(self, date):
        return date.strftime('%Y-%m-%d')

    def get_historical_data(self):
        from client.udun import Udun
        client = Udun(ACCESS_TOKEN)
        today = datetime.now()
        first_date = today - timedelta(self.DAY_RANGE)
        if self.START_DELTA:
            today -= timedelta(self.START_DELTA)
        data = {
            "symbol": self.SCRIP_NAME, "resolution": f"{self.TIME_FRAME}",
            "date_format": "1", "range_from": self.get_date_string(first_date),
            "range_to": self.get_date_string(today), "cont_flag": "1"}
        return client.get_history(data)

    def get_data(self):
        time.sleep(self.SLEEP)
        data = self.get_historical_data()
        df = pd.DataFrame(data['candles'], columns=[
            "Time", "Open Value",
            "Highest Value", "Lowest Value", "Close Value", "Volume"])

        # convert epoch time to normal datetime
        df['Time'] = df['Time'].apply(
            lambda x:  datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
        # convert date string to date time object
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
        df['Candle Body Size'] = df['Close Value'] - df['Open Value']
        df['Candle Size'] = df['Highest Value'] - df['Lowest Value']
        return df

    def get_working_days(self, data_frame):
        days = data_frame['Time'].dt.day
        months = data_frame['Time'].dt.month
        data = list(zip(months, days))
        return list(set((data)))
        # return list(data_frame['Time'].dt.day)

    # get all rows for a given day

    def get_values_for_a_give_day(self, hour, month, day, data_frame):
        return data_frame[(data_frame['Time'].dt.day == day) & (data_frame['Time'].dt.hour >= hour) &
                          (data_frame['Time'].dt.month >= month)]

    # get the row for a given concentration candle

    def get_concentration_candle(self, hour, minute, month, data_frame):
        return data_frame[(data_frame['Time'].dt.hour == hour) & (data_frame['Time'].dt.minute == minute)
                          & (data_frame['Time'].dt.month == month)]

    def floor(self, value):
        return round(value + (0.05 - value) % 0.05, 2)

    def get_quantity(self, price, fund=None):
        if not fund:
            fund = self.FUND
        intra_day_price = price/5
        return round(fund/intra_day_price)

    def get_first_bo(self, candle_max, candle_min, data_frame):
        data = data_frame[(data_frame['Close Value'] > candle_max)
                          | (data_frame['Close Value'] < candle_min)]
        if data.empty:
            return None, None, None, None, None, 0

        # get the first breakout candle
        breakout_candle = data.iloc[0]
        next_data_frame = data_frame.loc[breakout_candle.name + 1:]
        breakout_closing = breakout_candle['Close Value']
        bo_candle_size = float(breakout_candle['Highest Value'] -
                               breakout_candle['Lowest Value'])
        if breakout_closing > candle_min:
            print(
                f"Ref: {candle_max} => Entry in buy side at {breakout_closing} on {breakout_candle['Time']}\n")
            return (1, breakout_closing, (candle_min - self.STOP_LOSS_BUFFER), next_data_frame,
                    breakout_candle['Time'], bo_candle_size)
        print(
            f"Ref: {candle_min} => Entry in sell side at {breakout_closing} on {breakout_candle['Time']}\n")
        return (-1, breakout_closing, self.floor(candle_max + self.STOP_LOSS_BUFFER), next_data_frame,
                breakout_candle['Time'], bo_candle_size)

    def check_target(self, target, stop_loss, data_frame, side, bo_candle_size, atr=None):
        if side == 1:
            data = data_frame[((data_frame['Highest Value'] >= target)
                               | (data_frame['Lowest Value'] <= stop_loss))]

            if data.empty:
                data = data_frame[(data_frame['Time'].dt.hour == 14) &
                                  (data_frame['Time'].dt.minute == 45)]
                # return None, "Range bound day", None, None
                final_candle = data.iloc[0]
                diff = final_candle['Open Value'] - self.entry_price
                return (None, f"Range bound day exited on {final_candle['Open Value']}",
                        final_candle["Time"], diff)

            final_candle = data.iloc[0]
            if final_candle["Lowest Value"] <= stop_loss:
                candle_length = abs(
                    final_candle["Lowest Value"] - final_candle["Highest Value"])
                if atr and bo_candle_size > atr:
                    print(f"ATR was high {bo_candle_size} than ATR {atr}")
                    self.SL_WITH_ATR.append(
                        (atr, round(bo_candle_size, 2), bo_candle_size, final_candle["Time"]))
                return (False, f"{stop_loss} Stop loss hit {final_candle['Time']}",
                        final_candle["Time"], None)
        else:
            data = data_frame[((data_frame['Lowest Value'] <= target)
                               | (data_frame['Highest Value'] >= stop_loss))]
            if data.empty:
                data = data_frame[(data_frame['Time'].dt.hour == 14) &
                                  (data_frame['Time'].dt.minute == 45)]
                print(data_frame)
                final_candle = data.iloc[0]
                diff = self.entry_price - final_candle['Open Value']
                # return (None, f"Range bound day exited on {final_candle['Open Value']}",
                # final_candle["Time"], diff)
                return None, "Range bound day", final_candle["Time"], diff
            final_candle = data.iloc[0]
            if final_candle["Highest Value"] >= stop_loss:
                candle_length = abs(
                    final_candle["Lowest Value"] - final_candle["Highest Value"])
                if atr and bo_candle_size > atr:
                    print(f"ATR was high {bo_candle_size} than ATR {atr}")
                    self.SL_WITH_ATR.append(
                        (atr, round(bo_candle_size, 2), bo_candle_size, final_candle["Time"]))
                return (False, f"{stop_loss} Stop loss hit {final_candle['Time']}",
                        final_candle["Time"], None)

        return (True, f"{target} First target achieved on {final_candle['Time']}",
                final_candle["Time"], None)

    def process(self):
        for month, day in self.WORKING_DAYS:
            print("\\n" * 3)
            print("=" * 50)
            print(f"Date {day}")
            try:
                data = self.get_values_for_a_give_day(
                    self.BO_CANDLE_HR, month, day, self.df)
                concentration_candle = self.get_concentration_candle(
                    self.BO_CANDLE_HR, self.BO_CANDLE_MIN, month, data)
                candle_max = float(concentration_candle['Highest Value'])
                # get concentration candle min
                candle_min = float(concentration_candle['Lowest Value'])
                cc_candle_size = candle_max-candle_min
                cc_candle_open_size = abs(
                    float(concentration_candle['Open Value']-concentration_candle['Close Value']))
                # candle_size = 1.5
                # self.FIRST_TARGET_SIZE  = round(
                #     floor(abs(floor(candle_size - 0.10)) * 1.5), 2)
                if self.TARGET_IN_PERCENTAGE:
                    self.FIRST_TARGET_SIZE = self.floor(
                        round((candle_max*self.TARGET_IN_PERCENTAGE)/100, 2))
                self.STOP_LOSS_BUFFER = self.floor(
                    round((candle_max*self.STOP_LOSS_PERCENTAGE)/100, 2))
                second_target = (
                    self.floor((candle_max - candle_min) * 1.5)-0.10)

                print(
                    f"Target for the concentration candle {self.FIRST_TARGET_SIZE}-{second_target}")
                side, entry_price, stop_loss, new_data, entry_time, bo_candle_size = self.get_first_bo(
                    candle_max, candle_min, data)
                self.entry_price = entry_price
                print(
                    f"side: {side}, entry_price: {entry_price}, stop_loss : {stop_loss}")
                if side is None:
                    self.DAILY_DATA[f"{month}-{day}"] = 0
                    continue
                # print(new_data)
                target_price = round(
                    self.floor(self.FIRST_TARGET_SIZE * side + entry_price), 2)
                status, message, exit_time, diff = self.check_target(
                    target_price, stop_loss, new_data, side, bo_candle_size, self.ATR)
                stop_loss = None
                if status is None:
                    if diff < 1:
                        stop_loss = diff
                        self.STOP_LOSS.append(abs(diff))
                    else:
                        self.FIRST_TARGET_SIZE = diff
                        self.TARGET.append(diff)
                        self.ALL_ENTRY_TIME.append(entry_time)
                        self.ALL_EXIT_TIME.append(exit_time)
                    if self.GET_DAILY_DATA:
                        self.DAILY_DATA[f"{month}-{day}"] = diff * \
                            self.QUANTITY
                if status == False:
                    if side == -1:
                        stop_loss = round(
                            abs(candle_max-entry_price+self.STOP_LOSS_BUFFER), 2)
                    else:
                        stop_loss = round(
                            abs(entry_price-candle_min-self.STOP_LOSS_BUFFER), 2)
                    self.STOP_LOSS.append(stop_loss)
                    if self.GET_DAILY_DATA:
                        self.DAILY_DATA[f"{month}-{day}"] = - \
                            stop_loss * self.QUANTITY
                if status == True:
                    self.TARGET.append(self.FIRST_TARGET_SIZE)
                    self.ALL_ENTRY_TIME.append(entry_time)
                    self.ALL_EXIT_TIME.append(exit_time)
                    if self.GET_DAILY_DATA:
                        self.DAILY_DATA[f"{month}-{day}"] = self.FIRST_TARGET_SIZE * \
                            self.QUANTITY
                self.VALUES.append(
                    (side, round(cc_candle_size, 2), round(cc_candle_open_size, 2),
                     round(cc_candle_size/cc_candle_open_size, 2),
                     round(cc_candle_size-cc_candle_open_size, 2),
                     self.ATR, f"{month-day}", bo_candle_size, self.FIRST_TARGET_SIZE, stop_loss))
                self.SCORE.append(status)
                self.EXECUTED_DAYS.append(day)
            except Exception as error:
                print(error)
                traceback.print_exc()

    def get_avg_time(self, time_list):
        df = pd.to_datetime(pd.Series(time_list))
        df["time"] = df - df.dt.normalize()
        return (df['time'].mean())

    def meow(self):
        self.process()
        print(f"\nWorking days {len(self.WORKING_DAYS)}")
        print(f"Total stop loss points: {sum(self.STOP_LOSS)}")
        print(f"Total target points: {sum(self.TARGET)}")
        print(
            f'Total points captured {round(sum(self.TARGET), 2)-round(sum(self.STOP_LOSS), 2)}')
        print(self.EXECUTED_DAYS, self.WORKING_DAYS)
        ACCURACY = round(self.SCORE.count(
            True)/len(self.WORKING_DAYS) * 100, 2)
        range_bound_days = self.SCORE.count(None)
        sl_hit_days = self.SCORE.count(False)
        print(
            f"Accuracy for the give scrip {self.SCRIP_NAME} trade is {ACCURACY} at {self.BO_CANDLE_HR}-{self.BO_CANDLE_MIN} breakout")
        quantity = self.get_quantity(
            self.entry_price) if self.entry_price else 0
        avg_entry_time = self.get_avg_time(self.ALL_ENTRY_TIME)
        avg_exit_time = self.get_avg_time(self.ALL_EXIT_TIME)
        avg_time_trade = avg_exit_time - avg_entry_time
        return {
            "scrip_name": self.SCRIP_NAME,
            "time_range": f"{self.BO_CANDLE_HR}-{self.BO_CANDLE_MIN}",
            "time_frame": self.TIME_FRAME,
            "boolean": self.SCORE,
            "total_sl_count": round(sum(self.STOP_LOSS), 2),
            "total_target_count": round(sum(self.TARGET), 2),
            "win_%": ACCURACY,
            "loss_%": round(100-ACCURACY, 2),
            "total_sl_days": len(self.STOP_LOSS),
            "trading_dates": self.WORKING_DAYS,
            "executed_on_dates": self.EXECUTED_DAYS,
            "target": self.FIRST_TARGET_SIZE,
            "stop_loss_buffer": self.STOP_LOSS_BUFFER,
            "entry_price": self.entry_price,
            "quantity": quantity,
            "avg_per_trade": round(float(round(sum(self.TARGET), 2)/len(self.WORKING_DAYS)), 2),
            "total_days": len(self.WORKING_DAYS),
            "successful_days": self.SCORE.count(True),
            "sl_hit_days": sl_hit_days,
            "range_bound_days": range_bound_days,
            "Target %": self.TARGET_IN_PERCENTAGE,
            "total_points_captured": round(sum(self.TARGET), 2)-round(sum(self.STOP_LOSS), 2),
            "avg_entry_time": str(f"{avg_entry_time.seconds//3600}:{(avg_entry_time.seconds//60)%60}"),
            "avg_exit_time": str(f"{avg_exit_time.seconds//3600}:{(avg_exit_time.seconds//60)%60}"),
            "avg_time_in_trade": str(f"{avg_time_trade.seconds//3600}:{(avg_time_trade.seconds//60)%60}"),
            "daily_data": self.DAILY_DATA,
            "sl_with_atr": self.SL_WITH_ATR,
            "atr": self.ATR,
            "values": self.VALUES
        }


# diva = Diva(SCRIP_NAME="NSE:SAIL-EQ", DAY_RANGE=21, TIME_FRAME=15)
# diva.BO_CANDLE_HR = 10
# diva.BO_CANDLE_MIN = 15
# diva.STOP_LOSS_BUFFER = .45
# diva.TARGET_IN_PERCENTAGE = 1
# print(diva.meow())


# python concentration.py -tf 15 -hr 10 -m 15 -s JINDALSTEL -tp .5 -sl 0.15 -qt 67
# python concentration.py -tf 10 -hr 9 -m 15 -s ADANIPORTS -tp 0.5 -sl 0.1 -qt 45
# python concentration.py -tf 10 -hr 9 -m 15 -s BIOCON -tp 0.5 -sl 0.1 -qt 109
# python concentration.py -tf 10 -hr 9 -m 15 -s UPL -tp 0.5 -sl 0.1 -qt 46

# python concentration.py -tf 10 -hr 9 -m 15 -s BIOCON -tp 0.5 -sl 0.1 -qt 111
# python concentration.py -tf 9 -hr 15 -m 15 -s UPL -tp 0.5 -sl 0.1 -qt 51
# python concentration.py -tf 9 -hr 15 -m 15 -s SBICARD -tp 0.5 -sl 0.1 -qt 33


# SAIL 10400-1-511
# CHOLAFIN 10100-0.5-210
# HDFC 9700-0.5-180
# ADANIPORTS 10650-0.5-240


# 511+210+180+240

# Target .5% minimum

# 13:15 10min TF
# CHOLAFIN
# BIOCON
# INDUSTOWER

# 9:30 15min TF
# LUPIN

# 10 15min TF
# COALINDIA

# 10:15 10min TF
# JINDALSTEL
