import os
import requests

from datetime import datetime


URL = 'https://www1.nseindia.com/products/content/sec_bhavdata_full.csv'

BASE_DIR = 'bhav_full_download'

today = datetime.now()


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def check_or_create_dir():
    make_dir(BASE_DIR)
    make_dir(f'{BASE_DIR}/{today.strftime("%Y")}')


def download_file():
    path = f'{BASE_DIR}/{today.strftime("%Y")}/{today.strftime("%d-%a")}'
    r = requests.get(URL, allow_redirects=True)
    open(path, 'wb').write(r.content)


if __name__ == '__main__':
    day = today.isoweekday()
    if day in list(range(1, 6, 1)):
        check_or_create_dir()
        download_file()
