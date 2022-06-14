from pprint import pprint

from bsedata.bse import BSE

from config import DB
from models import update


def get_scrip_codes(bse):
    results = []
    scrip_codes = bse.getScripCodes()
    for scrip_id, company in scrip_codes.items():
        results.append({'Firm Name': scrip_id, 'Company': company})

    pprint(results)
    print("\nUpdating scrip IDs in MongoDB")
    # update("scrip", results)


if __name__ == '__main__':
    bse = BSE(update_codes=True)
    get_scrip_codes(bse)
