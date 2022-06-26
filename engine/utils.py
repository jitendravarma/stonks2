from models import Scrip


def get_indices(bse, category):
    return bse.getIndices(category=category)


def get_losers_gainers(bse):
    return bse.topLosers()


def get_stock_quote(bse, scrip):
    return bse.getQuote(scrip)


def get_top_gainers(bse):
    return bse.topGainers()


def find_scrip(bse, firm_name):
    return Scrip.find({'Firm Name': firm_name})


def verify_scrip(bse, scrip, firm_name):
    result = bse.verifyScripCode(scrip)
    if firm_name == result:
        return True
    return False
