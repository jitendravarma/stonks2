from datetime import datetime

import pandas as pd

from eq_archive import GenerateEQArchive
from vreport import GenerateVolitalityReport


class MergeReports(object):

    def get_archive_report(self):
        archive = GenerateEQArchive()
        archive.get_report()
        archive.save_report()

    def get_vreport(self):
        vreport = GenerateVolitalityReport()
        vreport.get_report()
        vreport.save_report()

    def highlight_greaterthan(self, data):
        if data.Descripency == 1:
            return ['background-color: yellow'] * len(data)
        else:
            return ['background-color: white'] * len(data)
        # is_max = pd.Series(data=False, index=data.index)
        # is_max["Descripency"] = data.loc["Descripency"] == 1
        # return ['background-color: yellow' if is_max.any() else '' for v in is_max]

    def merge(self):
        vreport_csv = pd.read_csv(f'{datetime.now().strftime("%b-%d-%Y")}-vreport.csv')
        archive_csv = pd.read_csv(f'{datetime.now().strftime("%b-%d-%Y")}-archive.csv')

        final_report = archive_csv.merge(vreport_csv[['V AVERAGE', 'SYMBOL']], on='SYMBOL', how='left')
        final_report = final_report.sort_values(by=["Descripency", "V AVERAGE"],  ascending=False)
        # final_report.style.apply(lambda x: ['background: lightgreen' if x.name in [2, 4]
        #                                     else '' for i in x],
        #                          axis=1)
        final_report.style.apply(self.highlight_greaterthan, axis=1)
        final_report.to_csv(f'{datetime.now().strftime("%b-%d-%Y")}-final.csv')
        print("Done merging")


if __name__ == '__main__':
    merger = MergeReports()
    merger.get_archive_report()
    merger.get_vreport()
    merger.merge()
