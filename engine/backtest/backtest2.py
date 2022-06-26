from datetime import datetime

import pandas as pd

# sbin


# ongc
# data = {'s': 'ok', 'candles': [[1648784700, 163.9, 166.5, 163.55, 164.0, 5347208], [1648785600, 164.0, 164.95, 163.9, 164.6, 1790112], [1648786500, 164.6, 164.85, 164.2, 164.6, 1019931], [1648787400, 164.6, 164.6, 164.15, 164.3, 1203309], [1648788300, 164.3, 164.95, 164.25, 164.8, 690282], [1648789200, 164.75, 164.8, 164.4, 164.5, 554011], [1648790100, 164.45, 165.35, 164.25, 165.15, 1291477], [1648791000, 165.1, 165.2, 164.85, 165.05, 474940], [1648791900, 165.05, 165.9, 165.05, 165.8, 911635], [1648792800, 165.85, 166.0, 165.2, 165.25, 790500], [1648793700, 165.3, 165.65, 165.2, 165.6, 325790], [1648794600, 165.6, 165.9, 165.3, 165.85, 513699], [1648795500, 165.85, 166.15, 165.45, 165.9, 792240], [1648796400, 165.9, 165.9, 164.7, 164.7, 723279], [1648797300, 164.65, 165.1, 164.5, 164.85, 660367], [1648798200, 164.9, 165.9, 164.9, 165.45, 602136], [1648799100, 165.45, 165.9, 165.45, 165.85, 374463], [1648800000, 165.85, 166.0, 165.5, 166.0, 591365], [1648800900, 166.0, 166.3, 165.45, 166.25, 1162980], [1648801800, 166.25, 167.0, 166.25, 166.8, 1282748], [1648802700, 166.8, 167.2, 166.6, 167.0, 928979], [1648803600, 167.0, 167.5, 166.75, 166.8, 825179], [1648804500, 166.85, 167.35, 166.8, 167.05, 715805], [1648805400, 167.0, 168.2, 167.0, 168.2, 2030178], [1648806300, 168.1, 168.25, 167.7, 167.95, 2401144], [1649043900, 166.95, 167.2, 165.65, 166.75, 1960797], [1649044800, 166.8, 166.85, 166.05, 166.25, 908683], [1649045700, 166.25, 166.3, 165.6, 165.85, 1117426], [1649046600, 165.85, 166.1, 165.35, 165.45, 883396], [1649047500, 165.4, 166.15, 165.35, 166.15, 571324], [1649048400, 166.05, 166.8, 165.8, 166.6, 708415], [1649049300, 166.65, 166.7, 166.45, 166.7, 431301], [1649050200, 166.7, 167.75, 166.7, 167.4, 917213], [1649051100, 167.35, 167.6, 167.3, 167.35, 487765], [1649052000, 167.4, 168.1, 167.35, 167.95, 786211], [1649052900, 167.95, 168.6, 167.9, 168.45, 731888], [1649053800, 168.5, 169.05, 168.25, 168.25, 898129], [1649054700, 168.3, 168.55, 167.9, 168.4, 675002], [1649055600, 168.5, 168.85, 168.4, 168.55, 344621], [1649056500, 168.55, 168.85, 168.4, 168.65, 377976], [1649057400, 168.7, 168.9, 168.45, 168.6, 305386], [1649058300, 168.7, 168.75, 168.15, 168.45, 542119], [1649059200, 168.5, 168.7, 168.35, 168.5, 376739], [1649060100, 168.5, 168.55, 168.4, 168.5, 366437], [1649061000, 168.5, 168.6, 168.35, 168.4, 337637], [1649061900, 168.45, 168.85, 168.35, 168.75, 298486], [1649062800, 168.75, 168.75, 168.25, 168.3, 653170], [1649063700, 168.35, 168.35, 167.8, 168.05, 596495], [1649064600, 168.2, 168.3, 167.8, 167.85, 816901], [1649065500, 167.85, 168.55, 167.65, 168.0, 1499289], [1649130300, 170.25, 171.2, 169.85, 170.5, 3423423], [1649131200, 170.55, 170.75, 169.3, 169.4, 1298362], [1649132100, 169.35, 170.5, 169.35, 170.5, 965865], [1649133000, 170.5, 171.0, 169.8, 170.85, 847220], [1649133900, 170.9, 171.1, 170.4, 170.55, 648774], [1649134800, 170.4, 170.6, 169.9, 170.25, 545561], [1649135700, 170.35, 170.7, 170.2, 170.7, 399681], [1649136600, 170.7, 170.9, 170.4, 170.8, 349528], [1649137500, 170.8, 170.8, 170.6, 170.7, 212224], [1649138400, 170.7, 171.0, 170.5, 170.95, 486377], [1649139300, 171.0, 171.15, 170.7, 170.9, 440993], [1649140200, 170.9, 171.15, 170.8, 171.1, 365137], [1649141100, 171.05, 171.6, 171.05, 171.55, 690131], [1649142000, 171.55, 172.0, 171.45, 171.75, 818847], [1649142900, 171.75, 172.0, 171.4, 171.55, 802607], [1649143800, 171.6, 172.6, 171.55, 172.5, 1008081], [1649144700, 172.55, 172.75, 172.35, 172.5, 836821], [1649145600, 172.5, 172.55, 171.8, 172.15, 598340], [1649146500, 172.15, 172.5, 171.95, 172.0, 566261], [1649147400, 171.8, 172.2, 171.35, 171.95, 636257], [1649148300, 171.9, 171.95, 171.55, 171.75, 376118], [1649149200, 171.75, 172.3, 171.7, 172.3, 663222], [1649150100, 172.25, 172.5, 172.05, 172.3, 875826], [1649151000, 172.25, 172.4, 171.8, 171.8, 878103], [1649151900, 171.8, 171.9, 171.25, 171.35, 1213367], [1649216700, 170.6, 172.3, 170.3, 172.2, 1557653], [1649217600, 172.2, 173.4, 172.0, 173.05, 1301696], [1649218500, 173.05, 173.3, 172.65, 172.85, 645240], [1649219400, 172.85, 172.95, 172.35, 172.65, 452740], [1649220300, 172.6, 172.65, 171.9, 172.45, 473349], [1649221200, 172.45, 173.15, 172.45, 173.15, 858957], [1649222100, 173.05, 173.2, 172.9, 173.15, 310140], [1649223000, 173.1, 173.5, 172.9, 172.95, 512032], [1649223900, 173.0, 173.05, 172.75, 172.85, 293435], [1649224800, 172.85, 173.1, 172.55, 172.55, 362428], [1649225700, 172.5, 172.5, 172.05, 172.3, 526781], [1649226600, 172.3, 172.8, 172.25, 172.75, 265258], [1649227500, 172.7, 173.0, 172.6, 172.95, 254034], [1649228400, 173.0, 173.05, 172.9, 173.0, 227249], [1649229300, 173.0, 173.25, 172.9, 173.0, 276596], [1649230200, 173.0, 173.0, 172.55, 172.95, 291286], [1649231100, 172.95, 173.0, 172.65, 172.65, 247376], [1649232000, 172.55, 173.2, 172.55, 173.15, 321375], [1649232900, 173.2, 173.35, 172.95, 173.05, 342934], [1649233800, 173.05, 173.35, 173.0, 173.25, 319423], [1649234700, 173.25, 173.5, 173.1, 173.2, 477805], [1649235600, 173.3, 173.35, 173.0, 173.05, 337892], [1649236500, 173.05, 173.1, 172.6, 172.75, 447721], [1649237400, 172.7, 173.05, 172.65, 173.05, 576089], [1649238300, 173.05, 173.2, 172.55, 172.75, 1234300], [1649303100, 170.6, 172.7, 169.3, 171.85, 4028589], [1649304000, 171.9, 172.6, 171.7, 171.9, 1109361], [1649304900, 171.9, 172.5, 171.8, 172.45, 1131800], [1649305800, 172.5, 173.8, 172.45, 172.9, 2217193], [1649306700, 172.9, 173.0, 171.85, 171.85, 942235], [1649307600, 171.8, 171.95, 170.9, 171.7, 1069780], [1649308500, 171.75, 171.95, 171.6, 171.9, 416123], [1649309400, 171.95, 172.1, 171.8, 172.0, 383693], [1649310300, 172.0, 172.3, 171.75, 171.75, 522923], [1649311200, 171.85, 172.1, 171.7, 172.1, 309886], [1649312100, 172.1, 172.25, 172.0, 172.1, 312390], [1649313000, 172.15, 172.2, 171.7, 171.85, 392462], [
# 1649313900, 171.9, 172.0, 171.8, 172.0, 427702], [1649314800, 172.0, 172.25, 171.95, 172.25, 455773], [1649315700, 172.25, 172.3, 172.05, 172.05, 277266], [1649316600, 172.05, 172.15, 171.2, 171.3, 391849], [1649317500, 171.25, 171.3, 170.45, 170.45, 461136], [1649318400, 170.35, 170.45, 169.5, 169.65, 1046686], [1649319300, 169.65, 169.7, 168.7, 169.45, 1107847], [1649320200, 169.45, 170.0, 168.55, 168.85, 1017217], [1649321100, 168.85, 169.5, 168.7, 169.4, 761101], [1649322000, 169.4, 169.4, 169.05, 169.1, 666154], [1649322900, 168.95, 169.35, 168.9, 169.1, 691106], [1649323800, 169.15, 169.35, 168.75, 168.9, 1697470], [1649324700, 168.95, 168.95, 168.2, 168.9, 2597241], [1649389500, 169.0, 170.65, 168.95, 169.25, 1178357], [1649390400, 169.25, 169.55, 168.9, 169.15, 521237], [1649391300, 169.15, 169.45, 168.7, 169.3, 354470], [1649392200, 169.25, 169.65, 169.0, 169.05, 502819], [1649393100, 169.1, 169.65, 168.85, 169.65, 568140], [1649394000, 169.55, 170.0, 169.5, 169.85, 396797], [1649394900, 169.85, 169.95, 169.5, 169.8, 183344], [1649395800, 169.85, 169.9, 169.6, 169.7, 190232], [1649396700, 169.75, 170.2, 169.65, 170.15, 266267], [1649397600, 170.15, 170.4, 170.0, 170.15, 341443], [1649398500, 170.15, 170.4, 170.0, 170.35, 238894], [1649399400, 170.35, 170.55, 170.25, 170.55, 228807], [1649400300, 170.5, 170.85, 170.5, 170.75, 277305], [1649401200, 170.75, 170.9, 169.9, 169.95, 536416], [1649402100, 170.0, 170.0, 169.45, 169.6, 251606], [1649403000, 169.6, 170.05, 169.55, 169.95, 140042], [1649403900, 169.9, 170.35, 169.75, 170.35, 114893], [1649404800, 170.4, 170.65, 170.3, 170.55, 198658], [1649405700, 170.6, 170.85, 170.4, 170.55, 218960], [1649406600, 170.6, 170.8, 170.55, 170.75, 204251], [1649407500, 170.7, 170.95, 170.65, 170.85, 267978], [1649408400, 170.9, 170.9, 170.6, 170.65, 200660], [1649409300, 170.65, 171.3, 170.65, 170.85, 503870], [1649410200, 170.85, 171.15, 170.6, 170.75, 337859], [1649411100, 170.8, 171.2, 170.65, 170.65, 1241723], [1649648700, 171.0, 172.75, 169.55, 171.4, 1598510], [1649649600, 171.25, 171.6, 170.8, 170.8, 721218], [1649650500, 170.8, 171.05, 170.55, 170.75, 537917], [1649651400, 170.85, 171.15, 170.35, 170.55, 493496], [1649652300, 170.45, 171.5, 170.45, 171.5, 333171], [1649653200, 171.4, 171.7, 171.05, 171.2, 348775], [1649654100, 171.2, 171.6, 171.1, 171.3, 207446], [1649655000, 171.3, 171.4, 171.15, 171.3, 192234], [1649655900, 171.3, 171.35, 171.0, 171.1, 217842], [1649656800, 171.1, 171.1, 170.85, 171.05, 208561], [1649657700, 171.1, 171.15, 170.55, 170.8, 276069], [1649658600, 170.8, 170.85, 170.65, 170.85, 176169], [1649659500, 170.85, 171.2, 170.75, 171.0, 235522], [1649660400, 171.0, 171.15, 170.75, 170.95, 334073], [1649661300, 171.0, 171.15, 170.85, 171.0, 201097], [1649662200, 171.0, 171.05, 170.8, 170.9, 187166], [1649663100, 170.95, 171.4, 170.9, 171.15, 360766], [1649664000, 171.15, 171.4, 171.05, 171.2, 292441], [1649664900, 171.25, 171.25, 171.0, 171.15, 268784], [1649665800, 171.15, 171.2, 170.95, 171.1, 244419], [1649666700, 171.15, 171.35, 171.0, 171.25, 264156], [1649667600, 171.25, 171.5, 170.95, 170.95, 357908], [1649668500, 170.9, 171.4, 170.8, 171.1, 248217], [1649669400, 171.15, 171.5, 170.9, 171.45, 594996], [1649670300, 171.45, 171.55, 170.9, 170.9, 761485], [1649735100, 171.0, 172.2, 170.85, 171.15, 1686192], [1649736000, 171.15, 171.15, 169.2, 169.5, 1358601], [1649736900, 169.45, 169.95, 168.85, 169.6, 803822], [1649737800, 169.6, 169.95, 169.4, 169.65, 346662], [1649738700, 169.55, 169.75, 169.35, 169.55, 483466], [1649739600, 169.5, 169.65, 169.0, 169.6, 590072], [1649740500, 169.6, 169.7, 169.4, 169.5, 201296], [1649741400, 169.55, 169.95, 169.5, 169.8, 213213], [1649742300, 169.8, 170.25, 169.65, 170.0, 311918], [1649743200, 169.95, 170.1, 169.3, 169.3, 310086], [1649744100, 169.35, 169.7, 169.35, 169.5, 168056], [1649745000, 169.45, 169.7, 169.3, 169.65, 217381], [1649745900, 169.65, 170.15, 169.6, 169.9, 363710], [1649746800, 169.95, 170.3, 169.85, 170.05, 219660], [1649747700, 170.15, 170.15, 169.7, 169.9, 216337], [1649748600, 169.9, 169.9, 169.3, 169.45, 294376], [1649749500, 169.5, 169.5, 168.75, 168.95, 390700], [1649750400, 168.9, 169.15, 168.5, 169.0, 457228], [1649751300, 169.0, 169.4, 168.8, 169.4, 260827], [1649752200, 169.4, 169.55, 169.35, 169.35, 247457], [1649753100, 169.35, 169.65, 169.15, 169.55, 326801], [1649754000, 169.55, 170.0, 169.5, 169.8, 160524], [1649754900, 169.8, 170.2, 169.5, 170.1, 281578], [1649755800, 170.15, 170.15, 169.05, 169.15, 1286850], [1649756700, 169.05, 169.05, 168.2, 168.75, 1926428], [1649821500, 171.4, 173.5, 170.7, 173.1, 3303799], [1649822400, 173.0, 173.35, 172.7, 172.95, 1307036], [1649823300, 173.15, 174.4, 173.1, 173.95, 2594405], [1649824200, 173.95, 174.2, 173.55, 173.9, 1216288], [1649825100, 173.9, 174.05, 173.5, 173.75, 918736], [1649826000, 173.75, 174.5, 173.6, 174.05, 972284], [1649826900, 174.05, 174.05, 173.7, 173.8, 614432], [1649827800, 173.75, 174.3, 173.7, 174.0, 620375], [1649828700, 174.0, 174.1, 173.85, 173.9, 361149], [1649829600, 173.95, 174.05, 173.65, 173.65, 485905], [1649830500, 173.75, 173.75, 173.05, 173.05, 964104], [1649831400, 172.85, 173.55, 172.85, 173.1, 569521], [1649832300, 173.05, 173.6, 173.05, 173.55, 363691], [1649833200, 173.5, 174.2, 173.4, 173.6, 604278], [1649834100, 173.6, 173.65, 173.25, 173.65, 364874], [1649835000, 173.6, 174.1, 173.6, 173.85, 531520], [1649835900, 173.9, 174.0, 173.65, 173.9, 382005], [1649836800, 173.9, 174.35, 173.85, 174.25, 588705], [1649837700, 174.35, 174.35, 173.85, 174.2, 451888], [1649838600, 174.2, 174.4, 174.1, 174.35, 416658], [1649839500, 174.4, 174.4, 173.85, 174.25, 536435], [1649840400, 174.2, 174.85, 174.2, 174.55, 1365073], [1649841300, 174.55, 174.65, 174.25, 174.4, 659060], [1649842200, 174.4, 174.5, 174.0, 174.4, 1063238], [1649843100, 174.4, 174.55, 173.75, 174.0, 2043055]]}

# history = {"symbol": "NSE:ONGC-EQ", "resolution": "15", "date_format": "1",
#            "range_from": "2022-04-01", "range_to": "2022-04-14", "cont_flag": "1"}


# AVERAGE_VOLUME = df['Volume'].mean()
# print(AVERAGE_VOLUME)
# get list of all working days


class Diva(object):

    def __init__(self) -> None:
        self.SCORE = []
        self.STOP_LOSS = []
        self.TARGET = []
        self.SCRIP_NAME = "NSE:SBIN-EQ"
        self.BO_CANDLE_HR = 10
        self.BO_CANDLE_MIN = 15
        self.TIME_FRAME = 15
        self.df = self.get_data()

    def get_data(self):
        data = {'s': 'ok', 'candles': [[1648784700, 491.0, 496.25, 491.0, 494.6, 1079545], [1648785600, 494.6, 495.65, 494.1, 495.2, 298327], [1648786500, 495.05, 495.95, 494.7, 495.9, 323662], [1648787400, 495.75, 497.2, 495.75, 496.95, 624972], [1648788300, 496.95, 499.6, 496.7, 498.9, 831323], [1648789200, 498.9, 498.95, 497.9, 498.45, 342340], [1648790100, 498.45, 499.95, 498.3, 498.55, 633562], [1648791000, 498.5, 501.65, 498.3, 499.55, 1137561], [1648791900, 499.7, 499.95, 498.8, 499.05, 249545], [1648792800, 499.0, 499.55, 498.35, 499.1, 247375], [1648793700, 499.1, 499.8, 498.85, 499.5, 225075], [1648794600, 499.5, 502.75, 499.5, 502.45, 1203969], [1648795500, 502.35, 505.6, 501.65, 504.65, 1622477], [1648796400, 504.65, 507.0, 504.4, 506.75, 1412512], [1648797300, 506.7, 507.0, 504.9, 505.2, 792716], [1648798200, 505.3, 505.8, 504.75, 505.0, 392298], [1648799100, 505.0, 507.5, 505.0, 506.9, 723065], [1648800000, 506.85, 507.8, 506.05, 506.3, 522419], [1648800900, 506.3, 506.95, 505.5, 505.75, 376041], [1648801800, 505.7, 507.8, 505.7, 507.3, 593492], [1648802700, 507.2, 508.55, 507.15, 507.45, 844544], [1648803600, 507.4, 508.75, 507.15, 507.5, 706001], [1648804500, 507.55, 507.7, 506.15, 507.0, 642026], [1648805400, 506.9, 508.0, 506.65, 507.9, 997744], [1648806300, 507.9, 509.75, 507.65, 508.45, 1672625], [1649043900, 509.3, 513.7, 506.0, 512.75, 3676051], [1649044800, 512.5, 514.0, 510.75, 511.9, 1561376], [1649045700, 511.9, 512.1, 510.8, 511.15, 600742], [1649046600, 511.0, 511.5, 509.5, 511.0, 787907], [1649047500, 511.2, 512.0, 510.35, 511.5, 465352], [1649048400, 511.5, 514.4, 511.15, 511.75, 950800], [1649049300, 511.75, 512.55, 510.6, 511.05, 404085], [1649050200, 511.2, 512.25, 510.5, 510.85, 375619], [1649051100, 510.8, 512.25, 510.8, 511.65, 245623], [1649052000, 511.55, 511.75, 509.3, 510.7, 607560], [1649052900, 510.65, 512.75, 510.65, 512.1, 504955], [1649053800, 512.15, 512.25, 511.3, 511.45, 220983], [1649054700, 511.3, 512.65, 511.05, 512.35, 264752], [1649055600, 512.35, 512.35, 510.15, 510.5, 271075], [1649056500, 510.55, 511.75, 510.4, 511.45, 257306], [1649057400, 511.45, 512.65, 511.4, 511.85, 277000], [1649058300, 512.0, 512.5, 511.7, 512.35, 224713], [1649059200, 512.2, 512.4, 511.5, 511.85, 156889], [1649060100, 511.8, 511.95, 511.2, 511.75, 157854], [1649061000, 511.8, 512.3, 510.6, 511.3, 317703], [1649061900, 511.35, 513.8, 511.1, 513.65, 727145], [1649062800, 513.7, 514.5, 513.3, 514.4, 783768], [1649063700, 514.4, 514.9, 512.65, 513.05, 657184], [1649064600, 513.15, 513.35, 511.65, 512.75, 746355], [1649065500, 512.85, 513.05, 511.75, 512.05, 911258], [1649130300, 514.4, 514.4, 509.3, 512.0, 1684409], [1649131200, 511.9, 513.1, 510.45, 510.65, 839573], [1649132100, 510.75, 511.6, 509.5, 511.0, 658680], [1649133000, 511.0, 512.0, 510.0, 511.15, 570044], [1649133900, 511.0, 512.7, 510.8, 512.3, 401022], [1649134800, 512.3, 512.4, 511.0, 511.55, 263397], [1649135700, 511.5, 513.2, 511.5, 512.8, 448175], [1649136600, 512.75, 514.75, 512.75, 513.85, 783720], [1649137500, 513.8, 516.0, 513.7, 515.65, 750232], [1649138400, 515.65, 515.7, 513.55, 514.8, 404620], [1649139300, 514.8, 515.5, 513.7, 513.75, 302238], [1649140200, 513.75, 514.65, 513.0, 514.15, 348032], [1649141100, 514.2, 514.35, 513.2, 513.8, 236476], [1649142000, 513.55, 513.95, 512.7, 513.9, 368032], [1649142900, 513.95, 514.8, 513.8, 514.3, 219439], [1649143800, 514.3, 515.4, 514.15, 515.3, 392697], [1649144700, 515.4, 516.4, 514.8, 515.8, 607296], [1649145600, 515.65, 516.15, 514.8, 515.25, 332013], [1649146500, 515.4, 515.6, 513.3, 513.3, 377856], [1649147400, 513.1, 513.65, 511.6, 512.0, 725656], [1649148300, 512.1, 513.0, 511.15, 511.65, 376690], [1649149200, 511.7, 512.95, 511.55, 512.55, 285131], [1649150100, 512.55, 512.75, 511.0, 511.8, 434805], [1649151000, 511.75, 512.0, 508.7, 509.1, 825042], [1649151900, 508.9, 509.3, 507.7, 508.0, 921234], [1649216700, 507.0, 509.9, 506.0, 508.6, 1365666], [1649217600, 508.8, 510.9, 508.1, 508.9, 765691], [1649218500, 508.8, 509.25, 507.0, 507.5, 622957], [1649219400, 507.35, 508.5, 506.4, 508.35, 502020], [1649220300, 508.2, 508.8, 507.75, 507.8, 224447], [1649221200, 507.85, 509.0, 507.8, 508.4, 295252], [1649222100, 508.4, 509.4, 508.0, 508.5, 269344], [1649223000, 508.4, 510.2, 508.2, 509.65, 550174], [1649223900, 509.65, 509.9, 508.4, 508.5, 302008], [1649224800, 508.55, 508.9, 507.5, 508.4, 346906], [1649225700, 508.35, 510.0, 508.05, 509.9, 324725], [1649226600, 509.9, 510.1, 509.3, 509.75, 306132], [1649227500, 509.75, 511.4, 509.55, 509.95, 552331], [1649228400, 509.5, 512.5, 509.5, 511.9, 634098], [1649229300, 511.9, 512.25, 510.25, 510.25, 386816], [1649230200, 510.1, 510.7, 508.65, 509.7, 396958], [1649231100, 509.7, 511.6, 509.65, 509.75, 841200], [1649232000, 509.7, 510.7, 509.5, 510.65, 209709], [1649232900, 510.6, 511.4, 509.8, 510.9, 258419], [1649233800, 510.8, 511.0, 510.1, 510.35, 223982], [1649234700, 510.6, 513.6, 510.35, 513.6, 782277], [1649235600, 513.6, 515.0, 512.55, 513.0, 830033], [1649236500, 512.9, 514.3, 511.6, 512.15, 625362], [1649237400, 512.0, 515.2, 511.95, 513.95, 1072353], [1649238300, 513.9, 514.35, 512.7, 512.7, 999109], [1649303100, 510.05, 513.2, 510.05, 511.9, 1115628], [1649304000, 511.85, 513.65, 511.4, 512.7, 1056200], [1649304900, 512.7, 512.9, 511.3, 512.0, 698070], [1649305800, 511.95, 512.25, 511.1, 512.25, 427945], [1649306700, 512.2, 514.0, 512.0, 512.6, 967241], [1649307600, 512.6, 513.65, 511.75, 513.1, 531297], [1649308500, 513.1, 513.5, 512.8, 513.05, 275279], [1649309400, 513.0, 515.7, 513.0, 514.6, 807175], [1649310300, 514.6, 515.95, 513.8, 515.6, 609219], [1649311200, 515.75, 517.4, 515.5, 516.65, 1003796], [1649312100, 516.65, 519.2, 516.55, 519.15, 1069875], [1649313000, 519.2, 519.9, 518.5, 519.25, 1123991], [
            1649313900, 519.35, 519.8, 518.15, 519.6, 593774], [1649314800, 519.55, 519.75, 518.65, 519.1, 402310], [1649315700, 519.1, 519.2, 518.0, 518.75, 435524], [1649316600, 518.9, 519.5, 518.1, 519.0, 380523], [1649317500, 519.0, 519.15, 517.1, 517.35, 401462], [1649318400, 517.2, 517.5, 513.7, 513.8, 1806726], [1649319300, 513.8, 513.95, 511.4, 513.35, 1427490], [1649320200, 513.45, 515.0, 512.75, 513.15, 644317], [1649321100, 513.2, 515.7, 512.15, 515.1, 674926], [1649322000, 515.1, 516.4, 514.0, 514.7, 645342], [1649322900, 514.7, 515.7, 514.2, 514.9, 445118], [1649323800, 514.9, 515.65, 513.7, 513.85, 709885], [1649324700, 513.75, 517.0, 513.45, 516.55, 1318996], [1649389500, 519.5, 519.5, 515.0, 515.8, 1432164], [1649390400, 515.8, 516.95, 515.1, 516.3, 637507], [1649391300, 516.3, 517.65, 513.8, 516.0, 949591], [1649392200, 516.0, 518.45, 514.9, 517.65, 1361065], [1649393100, 517.55, 517.7, 512.35, 515.65, 1331368], [1649394000, 515.75, 517.1, 515.5, 516.3, 857697], [1649394900, 516.4, 516.75, 515.65, 516.2, 230688], [1649395800, 516.2, 516.45, 513.5, 513.85, 399219], [1649396700, 513.95, 514.85, 513.5, 514.55, 339131], [1649397600, 514.55, 515.5, 514.0, 515.15, 213249], [1649398500, 515.15, 516.2, 514.75, 515.6, 241204], [1649399400, 515.75, 516.35, 514.5, 515.7, 347036], [1649400300, 515.7, 516.6, 515.5, 515.95, 374724], [1649401200, 516.0, 516.5, 515.45, 516.1, 192007], [1649402100, 516.1, 517.05, 515.0, 515.7, 423367], [1649403000, 515.7, 516.8, 515.0, 516.3, 306949], [1649403900, 516.3, 516.5, 515.6, 516.3, 165664], [1649404800, 516.3, 517.65, 516.0, 516.95, 450163], [1649405700, 516.95, 517.65, 515.75, 516.95, 398108], [1649406600, 516.95, 517.95, 516.85, 517.2, 405995], [1649407500, 517.3, 517.5, 515.8, 516.15, 347400], [1649408400, 516.1, 516.8, 515.5, 515.9, 295937], [1649409300, 515.9, 516.9, 515.9, 516.6, 381108], [1649410200, 516.7, 516.75, 515.2, 515.9, 647529], [1649411100, 515.9, 516.5, 515.5, 516.1, 767951], [1649648700, 513.5, 519.5, 513.2, 519.05, 1622846], [1649649600, 519.05, 522.0, 517.8, 520.1, 1444497], [1649650500, 520.1, 521.15, 518.65, 519.65, 728015], [1649651400, 519.6, 519.75, 518.25, 519.45, 464117], [1649652300, 519.4, 520.45, 519.0, 520.1, 657347], [1649653200, 520.15, 520.2, 518.8, 518.9, 467981], [1649654100, 518.9, 519.0, 518.0, 518.9, 406914], [1649655000, 518.85, 519.35, 518.25, 518.9, 168024], [1649655900, 518.9, 519.3, 518.35, 519.0, 193164], [1649656800, 518.95, 519.0, 518.5, 518.85, 124026], [1649657700, 518.95, 519.15, 518.35, 518.5, 171732], [1649658600, 518.6, 519.3, 517.2, 518.1, 480670], [1649659500, 518.1, 518.7, 517.6, 518.0, 290510], [1649660400, 517.85, 518.45, 517.0, 517.05, 368164], [1649661300, 517.0, 519.5, 516.75, 519.4, 408455], [1649662200, 519.4, 519.95, 518.6, 519.5, 366974], [1649663100, 519.6, 520.0, 518.5, 518.65, 536654], [1649664000, 518.7, 519.3, 517.75, 517.9, 302634], [1649664900, 517.9, 518.85, 517.35, 518.05, 315275], [1649665800, 518.2, 518.8, 517.65, 518.75, 188035], [1649666700, 518.8, 518.85, 517.8, 518.35, 202472], [1649667600, 518.5, 518.6, 517.25, 517.5, 245603], [1649668500, 517.5, 517.5, 515.45, 515.75, 599966], [1649669400, 515.75, 515.75, 514.05, 515.15, 752843], [1649670300, 515.15, 515.6, 514.35, 515.0, 812657], [1649735100, 512.75, 513.0, 510.15, 510.2, 1499290], [1649736000, 510.3, 510.3, 505.0, 507.65, 1532838], [1649736900, 507.4, 508.25, 506.5, 508.1, 478846], [1649737800, 508.1, 508.1, 505.95, 506.15, 602388], [1649738700, 506.1, 506.25, 504.35, 506.1, 546739], [1649739600, 506.2, 507.95, 506.05, 507.5, 342351], [1649740500, 507.3, 507.75, 506.8, 507.35, 215598], [1649741400, 507.4, 508.75, 507.3, 508.4, 393652], [1649742300, 508.45, 510.3, 508.3, 509.55, 498378], [1649743200, 509.5, 510.45, 508.7, 509.95, 498479], [1649744100, 510.0, 510.5, 509.4, 510.3, 388719], [1649745000, 510.25, 510.9, 509.85, 510.45, 327595], [1649745900, 510.4, 510.8, 509.3, 509.5, 318288], [1649746800, 509.6, 510.4, 508.6, 510.2, 426199], [1649747700, 510.2, 510.5, 509.3, 510.2, 339771], [1649748600, 510.35, 510.4, 508.9, 509.25, 285992], [1649749500, 509.25, 510.5, 509.0, 509.2, 357194], [1649750400, 509.1, 509.45, 507.1, 507.75, 437805], [1649751300, 507.7, 510.0, 507.35, 509.95, 284575], [1649752200, 510.0, 514.4, 509.9, 513.6, 1215793], [1649753100, 513.9, 514.15, 512.45, 513.55, 500165], [1649754000, 513.75, 516.7, 513.6, 515.15, 948119], [1649754900, 515.15, 515.55, 513.55, 514.5, 391528], [1649755800, 514.5, 514.8, 512.2, 512.9, 804260], [1649756700, 512.8, 513.2, 512.0, 512.5, 768917], [1649821500, 514.3, 516.75, 514.25, 515.5, 810021], [1649822400, 515.5, 516.25, 515.4, 515.85, 460284], [1649823300, 515.8, 517.35, 515.45, 516.8, 524308], [1649824200, 516.85, 516.95, 514.7, 515.05, 577243], [1649825100, 515.05, 516.05, 514.6, 515.35, 283292], [1649826000, 515.35, 516.0, 515.0, 515.4, 235647], [1649826900, 515.4, 516.8, 515.2, 516.55, 328957], [1649827800, 516.55, 517.6, 516.0, 516.5, 424083], [1649828700, 516.5, 516.95, 516.15, 516.9, 154250], [1649829600, 516.9, 517.45, 516.5, 516.5, 300991], [1649830500, 516.4, 516.5, 515.35, 515.7, 367002], [1649831400, 515.6, 516.75, 513.75, 514.75, 1431847], [1649832300, 514.55, 516.0, 514.55, 515.85, 1332948], [1649833200, 515.85, 519.35, 515.05, 518.3, 1118185], [1649834100, 518.35, 518.5, 517.2, 517.7, 292284], [1649835000, 517.7, 520.4, 517.15, 520.2, 869903], [1649835900, 520.25, 520.9, 518.1, 518.5, 733584], [1649836800, 518.35, 519.2, 517.35, 517.8, 368778], [1649837700, 517.8, 518.1, 516.7, 517.4, 394010], [1649838600, 517.4, 518.5, 516.75, 517.8, 252282], [1649839500, 517.8, 518.35, 517.0, 518.05, 799410], [1649840400, 517.95, 518.7, 517.5, 518.1, 236627], [1649841300, 518.05, 518.15, 517.25, 517.3, 404091], [1649842200, 517.35, 518.0, 516.65, 516.7, 1231615], [1649843100, 516.7, 518.45, 516.5, 517.7, 1476846]]}
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
        return set(data_frame['Time'].dt.day)

    # get all rows for a given day

    def get_values_for_a_give_day(self, hour, minute, day, data_frame):
        return data_frame[(data_frame['Time'].dt.day == day) & (data_frame['Time'].dt.hour >= hour)
                          & (data_frame['Time'].dt.minute >= minute)]

    # get the row for a given concentration candle

    def get_concentration_candle(self, hour, minute, data_frame):
        return data_frame[(data_frame['Time'].dt.hour == hour) & (data_frame['Time'].dt.minute == minute)]

    def floor(self, value):
        return round(value + (0.05 - value) % 0.05, 2)

    def get_first_bo(self, candle_max, candle_min, data_frame):
        data = data_frame[(data_frame['Close Value'] > candle_max)
                          | (data_frame['Close Value'] < candle_min)]
        if data.empty:
            return None, None, None, None, None

        # get the first breakout candle
        breakout_candle = data.iloc[0]
        print(breakout_candle)
        breakout_closing = breakout_candle['Close Value']
        if breakout_closing > candle_min:
            print(
                f"Ref: {candle_max} => Entry in buy side at {breakout_closing} on {breakout_candle['Time']}\n")
            return (1, breakout_closing, (candle_min - 0.50), data.iloc[1:],
                    breakout_candle['Time'])
        print(
            f"Ref: {candle_min} => Entry in sell side at {breakout_closing} on {breakout_candle['Time']}\n")
        return (-1, breakout_closing, self.floor(candle_max + 0.50), data.iloc[1:],
                breakout_candle['Time'])

    def check_target(self, target, stop_loss, data_frame, side):
        if side == 1:
            data = data_frame[((data_frame['Highest Value'] >= target)
                               | (data_frame['Lowest Value'] <= stop_loss))]
            final_candle = data.iloc[0]
            if data.empty:
                return (None, f"Range bound day", None, None)
            if final_candle["Lowest Value"] <= stop_loss:
                return (False, f"{stop_loss} Stop loss hit {final_candle['Time']}", final_candle['Lowest Value'],
                        final_candle["Time"])
            return (True, f"{target} First target achieved on {final_candle['Time']}", final_candle['Highest Value'],
                    final_candle["Time"])
        else:
            data = data_frame[((data_frame['Lowest Value'] <= target)
                               | (data_frame['Highest Value'] >= stop_loss))]
            if data.empty:
                return (None, f"Range bound day", None, None)
            final_candle = data.iloc[0]
            if final_candle["Highest Value"] >= stop_loss:
                return (False, f"{stop_loss} Stop loss hit {final_candle['Time']}", final_candle['Lowest Value'],
                        final_candle["Time"])
            return (True, f"{target} First target achieved on {final_candle['Time']}", final_candle['Highest Value'],
                    final_candle["Time"])

    def process(self):
        working_days = self.get_working_days(self.df)
        for day in working_days:
            print(f"\n"*3)
            print(f"="*50)
            print(f"Date {day}")
            try:
                data = self.get_values_for_a_give_day(
                    self.BO_CANDLE_HR, self.BO_CANDLE_MIN, day, self.df)
                concentration_candle = self.get_concentration_candle(
                    self.BO_CANDLE_HR, self.BO_CANDLE_MIN, data)
                # get concentration candle max
                candle_max = max(
                    float(concentration_candle['Close Value']), float(concentration_candle['Open Value']))
                # get concentration candle min
                candle_min = min(
                    float(concentration_candle['Close Value']), float(concentration_candle['Open Value']))
                print(candle_max, candle_min)
                # get candle body size
                candle_size = abs(self.floor(candle_max - candle_min))

                # candle_size = 1.5
                # first_target_size = round(
                #     floor(abs(floor(candle_size - 0.10)) * 1.5), 2)
                first_target_size = 1.5
                second_target = (
                    self.floor((candle_max - candle_min) * 1.5)-0.10)

                print(
                    f"Target for the concentration candle {first_target_size}-{second_target}")
                side, entry_price, stop_loss, new_data, entry_time = self.get_first_bo(
                    candle_max, candle_min, data)
                print(side, entry_price, stop_loss)

                # print(new_data)
                target_price = round(
                    self.floor(first_target_size * side + entry_price), 2)
                print(target_price, stop_loss)
                status, message, exit_at_price, exit_time = self.check_target(
                    target_price, stop_loss, new_data, side)
                if status == False:
                    self.STOP_LOSS.append(round(abs(stop_loss-entry_price), 2))
                print("Results:")
                print({
                    "status": status, "candle_size": candle_size,
                    "side": side, "entry_price": entry_price, "target_price": target_price,
                    "stop_loss": stop_loss,
                    "first_target_size": first_target_size,
                    "message": message, "entry_time": entry_time, "exit_time": exit_time
                })
                print(data)
                if status is not None:
                    self.SCORE.append(status)
                # break
            except Exception as error:
                print(error)
                break

    def meow(self):
        self.process()
        print(f"Total stop loss: {self.STOP_LOSS}")
        print(self.SCORE)

        ACCURACY = round(self.SCORE.count(True)/len(self.SCORE) * 100, 2)
        print(
            f"Accuracy for the give scrip {self.SCRIP_NAME} trade is {ACCURACY} at {self.BO_CANDLE_HR}-{self.BO_CANDLE_MIN} breakout")

        self.SCORE = []
        self.STOP_LOSS = []
        self.TARGET = []
        self.SCRIP_NAME = "NSE:SBIN-EQ"
        self.BO_CANDLE_HR = 10
        self.BO_CANDLE_MIN = 15


diva = Diva()
diva.SCRIP_NAME = "NSE:SBIN-EQ"
diva.BO_CANDLE_HR = 10
diva.BO_CANDLE_MIN = 15
diva.TIME_FRAME = 15
diva.meow()
