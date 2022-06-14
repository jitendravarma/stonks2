import os

from flask import Flask, render_template

from pta.activity.activity import DailyAcitivityReport
from pta.vreport.vreport import GenerateVolitalityReport

app = Flask(__name__)


template_dir = os.path.abspath('templates')

@app.route('/')
def home():
    report = DailyAcitivityReport()
    report.get_daily_active_sectors()
    report.get_performing_stocks()
    return render_template('your_file.html')

@app.route('/areport/', methods=['GET'])
def get_vreport():
    report = DailyAcitivityReport()
    report.get_daily_active_sectors()
    report.get_performing_stocks()
    return "Acitiviy report generated"


@app.route('/vreport/', methods=['GET'])
def get_activity():
    vreport = GenerateVolitalityReport()
    vreport.get_report()
    vreport.save_report()
    return "Volitality Report generated!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
