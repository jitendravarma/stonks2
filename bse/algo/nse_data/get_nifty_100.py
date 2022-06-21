import requests

cookies = {
    'AKA_A2': 'A',
    'nsit': 'DvXP2qEHEIighxrDq05io7a5',
    'nseappid': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY0OTM1MzU3MSwiZXhwIjoxNjQ5MzU3MTcxfQ.1wlE6nAprZdwra8fjBtJneg2mDOV9CsSoJlcjPhFEVQ',
    'bm_mi': '19C4F0733C7C085FAD487AF2DBBC2CA0~OxqNTy6VGuf/hyHac11peDoq8GlcBIko6SD+tzM50NPf/f8x0reoplVePeVRhpErAu14d5ir1O2lPYjHi+GikKMOXgp5J5y/4cpGgB8JFbI1lq3PRDnhRD4E1B/IWWaVlP26nwTEtY73ztYp1PBBOxw4/FSaEhOysABurWAW3FRrFCD0AtHGbS7dliZv9XbwnmmyKDGtzYJ0UA+k7omga4ATajqI2Lw7t1b4TWD3Sq2eO/bHgzZK3OPwRzrJVkvkReikqe9U93Jqua00MUgZ7cyQQP3XT/V3Mo9MAJ3oz8CO/djCyANQ+O9aEgcXtn4l',
    'ak_bmsc': '4F29B53FA8E7AD64B43871F0B1E8A2B7~000000000000000000000000000000~YAAQpv3UF9woNQCAAQAAu1EiBQ9CZiSmnznq+2WIiza81Im6vSy0/j8FnbcJFhr4Y7+jEXHz7EEQuTO+4ysXSbYYVAF9fQ1u3mal4bDVNTwJRw/ixnTCsldYESejM9/y1FsbsCiIhc0MT0bd2KqGjmfRfOWY4Qa+CqdNtx5sTKWfPJvcPkHgyj91kSNGP1bOFvT6S7G3fQfeZH63JFwMdxCuu+15iDkFrMOzK8V6zsZDdF4nZYm5H2RaWhciu+71olxZxKzET/jxA+TNYxsulY6lBRGp2gIROro3fwW+YqlkcCJtZLelhJlydkuCIDpFJGnbtcolEe4INrjgI7qsRAkbtNazLs0b3ZFJKrDZi1LuZ2b5OUK/LhB4X04M/tYgDnwTMAOLQOh+UuhF4CoaLft7lrfylTxCV0snopqW30ryOPJZ6ANnPrCutsVpHiI3FXuj2ZE5mYvFM/9eHBU=',
    'bm_sv': '13EF92EE6DFBBA11718EE00DEB2B53A7~eF/cNAjedHm4IS6f1EKli35QXYJPEGSU6sOqESuqaQTDRynbb401GdBbYNRI201Mhd+f+VFaZWarcL3oyvAvVOPGTMPKBnGMNbRPNjbKAQXzXTJob3KyMIwiQabH+cp96Z+62CJclWPMmqdbjjSyfluJGEW0IaWBZVMFAoldpjQ=',
}

headers = {
    'authority': 'www.nseindia.com',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20100',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'AKA_A2=A; nsit=DvXP2qEHEIighxrDq05io7a5; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY0OTM1MzU3MSwiZXhwIjoxNjQ5MzU3MTcxfQ.1wlE6nAprZdwra8fjBtJneg2mDOV9CsSoJlcjPhFEVQ; bm_mi=19C4F0733C7C085FAD487AF2DBBC2CA0~OxqNTy6VGuf/hyHac11peDoq8GlcBIko6SD+tzM50NPf/f8x0reoplVePeVRhpErAu14d5ir1O2lPYjHi+GikKMOXgp5J5y/4cpGgB8JFbI1lq3PRDnhRD4E1B/IWWaVlP26nwTEtY73ztYp1PBBOxw4/FSaEhOysABurWAW3FRrFCD0AtHGbS7dliZv9XbwnmmyKDGtzYJ0UA+k7omga4ATajqI2Lw7t1b4TWD3Sq2eO/bHgzZK3OPwRzrJVkvkReikqe9U93Jqua00MUgZ7cyQQP3XT/V3Mo9MAJ3oz8CO/djCyANQ+O9aEgcXtn4l; ak_bmsc=4F29B53FA8E7AD64B43871F0B1E8A2B7~000000000000000000000000000000~YAAQpv3UF9woNQCAAQAAu1EiBQ9CZiSmnznq+2WIiza81Im6vSy0/j8FnbcJFhr4Y7+jEXHz7EEQuTO+4ysXSbYYVAF9fQ1u3mal4bDVNTwJRw/ixnTCsldYESejM9/y1FsbsCiIhc0MT0bd2KqGjmfRfOWY4Qa+CqdNtx5sTKWfPJvcPkHgyj91kSNGP1bOFvT6S7G3fQfeZH63JFwMdxCuu+15iDkFrMOzK8V6zsZDdF4nZYm5H2RaWhciu+71olxZxKzET/jxA+TNYxsulY6lBRGp2gIROro3fwW+YqlkcCJtZLelhJlydkuCIDpFJGnbtcolEe4INrjgI7qsRAkbtNazLs0b3ZFJKrDZi1LuZ2b5OUK/LhB4X04M/tYgDnwTMAOLQOh+UuhF4CoaLft7lrfylTxCV0snopqW30ryOPJZ6ANnPrCutsVpHiI3FXuj2ZE5mYvFM/9eHBU=; bm_sv=13EF92EE6DFBBA11718EE00DEB2B53A7~eF/cNAjedHm4IS6f1EKli35QXYJPEGSU6sOqESuqaQTDRynbb401GdBbYNRI201Mhd+f+VFaZWarcL3oyvAvVOPGTMPKBnGMNbRPNjbKAQXzXTJob3KyMIwiQabH+cp96Z+62CJclWPMmqdbjjSyfluJGEW0IaWBZVMFAoldpjQ=',
}

params = {
    'csv': 'true',
    'index': 'NIFTY 100',
}

response = requests.get(
    'https://www.nseindia.com/api/equity-stockIndices', headers=headers, params=params)

print('here')
print(response.status_code

      )
with open('NIFTY_100.csv', 'w') as csv_file:
    csv_file.write(response.content)
